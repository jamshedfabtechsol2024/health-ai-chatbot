from typing import Dict, Any, List
import os
import requests
import logging
from AnalyzeReport.prompt import Prompts
from pinecone import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
import io
from dotenv import load_dotenv
from Models.models import embedding_model, report_analysis_model
from datetime import datetime
from langchain.schema import SystemMessage, HumanMessage
import json

from sqlalchemy.orm import Session
from sqlalchemy import update
from app.models import User
from fastapi import HTTPException

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HealthReportUtils:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Get API keys and configuration
        self.upstage_api_key = os.getenv("UPSTAGE_API_KEY")
        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")
        self.pinecone_index_name = os.getenv("PINECONE_INDEX_NAME")
        self.upstage_ocr_url = os.getenv("UPSTAGE_OCR_URL")

        # Initialize services
        self.embedding_model = embedding_model

        pc = Pinecone(api_key=self.pinecone_api_key)
        self.index = pc.Index(host=self.pinecone_index_name)

    # def extract_text_from_pdf(self, file_path: bytes) -> str:
    #     try:
    #         response = requests.get(file_path, stream=True)
    #         response.raise_for_status()

    #         # Load file into memory
    #         file_bytes = io.BytesIO(response.content)

    #         files = {
    #             "document": ("document.pdf", file_bytes, "application/pdf")
    #         }

    #         url = self.upstage_ocr_url
    #         headers = {"Authorization": f"Bearer {self.upstage_api_key}"}

    #         data = {"model": "ocr"}
    #         response = requests.post(url, headers=headers, files=files, data=data)

    #         return response.json()["text"]

    #     except requests.exceptions.RequestException as e:
    #         logger.error(f"Error in OCR API call: {str(e)}")
    #         raise Exception(f"OCR API call failed: {str(e)}")

    def extract_text_from_pdf(self, file_path: bytes) -> str:
        try:
            url = "https://api.upstage.ai/v1/document-digitization"

            response = requests.get(file_path, stream=True)
            response.raise_for_status()
            
            headers = {"Authorization": f"Bearer {self.upstage_api_key}"}
            # Load file into memory
            file_bytes = io.BytesIO(response.content)
            
            files = {
                "document": ("document.pdf", file_bytes, "application/pdf")
            }

            data = {
            "model": "document-parse-nightly",
            "ocr": "auto",
            "chart_recognition": True,
            "coordinates": True,
            "output_formats": '["markdown"]',
            "base64_encoding": '["figure"]',
        }

            response = requests.post(url, headers=headers, files=files, data=data)
 
            
            pdf_data = response.json()["content"]["markdown"]
            # print("-------------------------------------------------------------")
            # print(response)
            # print("-------------------------------------------------------------")
            return pdf_data

        except requests.exceptions.RequestException as e:
            logger.error(f"Error in OCR API call: {str(e)}")
            raise Exception(f"OCR API call failed: {str(e)}")

    def split_text_into_chunks(
        self, text: str, chunk_size: int = 1000, chunk_overlap: int = 300) -> List[str]:
        try:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
            )
            chunks = text_splitter.split_text(text)
            logger.info(f"Split text into {len(chunks)} chunks")
            return chunks
        except Exception as e:
            logger.error(f"Error splitting text into chunks: {str(e)}")
            raise


    def store_embeddings(
        self, extracted_text: str, user_id: int, source_file: str, pdf_type: str) -> bool:
        try:
            # Split text into chunks
            chunks = self.split_text_into_chunks(extracted_text)
            print("---------------------", chunks)
            embeddings = self.embedding_model.embed_documents(chunks)
            print("DEBUG: embedding size:", len(embeddings[0]))

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            records = []
            for i, (embedding_vector, chunk_text) in enumerate(zip(embeddings, chunks)):
                record_id = f"{source_file}-1-chunk-{i}"
                records.append(
                    {
                        "id": record_id,
                        "values": embedding_vector,
                        "metadata": {
                            "text": chunk_text,
                            "date_time": timestamp,
                            "pdf_type": pdf_type,
                            "pdf_id": source_file + timestamp,
                        },
                    }
                )

            # Upsert into Pinecone
            self.index.upsert(vectors=records, namespace=user_id)

            logger.info(f"Successfully stored {len(records)} vectors for user {user_id}")
            return True

        except Exception as e:
            logger.error(f"Error storing embeddings: {str(e)}")
            return False


    def retrieve_data_from_pinecone(
        self, user_input: str, namespace: str, report_type: str
    ) -> List[str]:
        query_embedding = self.embedding_model.embed_query(user_input)

        query_results = self.index.query(
            namespace=namespace,
            vector=query_embedding,
            top_k=5,
            include_metadata=True,
            filter={"pdf_type": report_type},
        )

        data = [match["metadata"]["text"] for match in query_results["matches"]]

        return data

    def analyze_text(self, text: str = "", file_type: str = "", current_date: str = "", current_day: str = "", prompt: str = "") -> Dict[str, Any]:
        try:
            # Add values in prompt
            if file_type in ["blood","urine","dna"]:
                prompt = prompt.format(text=text)
            else:
                prompt = prompt.format(text=text, current_date=current_date, current_day=current_day) 

            response = report_analysis_model.invoke([{"role": "user", "content": prompt}])
            return {
                "raw_analysis": response.content if hasattr(response, "content") else str(response),
                "status": "success"
            }
        except Exception as e:
            logger.error(f"Error analyzing text: {str(e)}")
            raise
                                                                                                                                                                                                                                                             
    def blood_health_analysis(self, blood_reports_data):

        prompt = Prompts.blood_box_related_prompt.format(blood_reports_data=blood_reports_data)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        response_last_test = report_analysis_model.invoke(prompt)                                                                                                                                                                             
        return json.loads(response_last_test.content)
                                   
    def urine_health_analysis(self, urine_reports_data):

        prompt = Prompts.urine_box_related_prompt.format(urine_reports_data=urine_reports_data)
        response = report_analysis_model.invoke(prompt)
        return response.content
    
    def check_report_type(self,file_data):
        messages = [
            SystemMessage(content=Prompts.file_type_checker_prompt),
            HumanMessage(content=f"Here is the Latest Report: {file_data}"),
        ]
        response = report_analysis_model.invoke(messages)
        
        return json.loads(response.content)

class TokenService:
    @staticmethod
    def deduct_chat_token(user_id: int, db: Session):
        """
        Deduct 1 chat token for the user and return remaining tokens.
        """
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Skip deduction for unlimited users
        if user.unlimited_chats:
            return {"remaining_tokens": "unlimited"}

        if user.chat_limit <= 0:
            raise HTTPException(status_code=403, detail="No chat tokens left")

        user.chat_limit -= 1
        db.commit()
        db.refresh(user)

        return {"remaining_tokens": user.chat_limit}
