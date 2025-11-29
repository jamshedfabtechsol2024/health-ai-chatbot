# model.py
import os
import logging
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

report_analysis_model = ChatOpenAI(
                model=os.getenv("OPEN_API_MODEL"),
                api_key=openai_api_key
            )

chatbot_model = ChatOpenAI(
                model=os.getenv("OPEN_API_MODEL"),
                api_key=openai_api_key,
                streaming=True
            )

embedding_model = OpenAIEmbeddings(
            model=EMBEDDING_MODEL,  # Using small model which has 1536 dimensions
            api_key=openai_api_key
        )

class ModelManager:
    def __init__(self):
        """Initialize the model manager with OpenAI integration."""
        # Load environment variables
        load_dotenv()
        
        # Get API key
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        
    def get_chat_model(self, temperature: float = 0) -> ChatOpenAI:

        try:
            model = ChatOpenAI(
                model=os.getenv("OPEN_API_MODEL"),
                temperature=temperature,
                max_retries=2,    # Retry failed requests
                api_key=self.openai_api_key
            )
            logger.info("OpenAI chat model initialized successfully")
            return model
        except Exception as e:
            logger.error(f"Error initializing OpenAI chat model: {str(e)}")
            raise