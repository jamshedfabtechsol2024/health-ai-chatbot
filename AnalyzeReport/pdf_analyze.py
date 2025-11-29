################################# S3 PDF

import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")


pdf_url = "https://ocr-tests-bucket.s3.amazonaws.com/e754f460-b0e3-4c1e-aab0-6390c2f98210/Test Folder new/Urine Test Walter Harris profile 7 Jan24.pdf"


import base64
import requests


# Read and encode the PDF file
pdf_response = requests.get(pdf_url)

base64_pdf = base64.b64encode(pdf_response.content).decode("utf-8")

# Prepare the request payload
payload = {
    "model": "gpt-4.1",
    "input": [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "filename": "Urine Test Walter Harris profile 7 Jan24.pdf",
                    "file_data": f"data:application/pdf;base64,{base64_pdf}",
                },
                {
                    "type": "input_text",
                    "text": (
                        "This is a medical test report. Please tell me if it is related to blood, urine, or DNA. "
                        "Return only a JSON in this format:\n{\"file_type\": \"blood\"} or \"urine\" or \"dna\""
                    ),
                },
            ],
        },
    ],
    
}

# Set up the request headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

# Send the request to OpenAI's API
response = requests.post("https://api.openai.com/v1/responses", headers=headers, json=payload)


# Extract and print JSON
try:
    print(response.json()['output'][0]['content'][0]['text'])
except (KeyError, IndexError):
    print(f"Error: {response.status_code} - {response.text}")










###################################  local File

# import os
# from dotenv import load_dotenv
# load_dotenv()
# api_key=os.getenv("OPENAI_API_KEY")
# pdf_path = r"B:\Fabtechsol\Backend_wiseHealth\health-ai-chatbot\AnalyzeReport\BloodReport.pdf"


# import base64
# import requests


# # Read and encode the PDF file
# with open(pdf_path, "rb") as f:
#     pdf_data = f.read()
#     base64_pdf = base64.b64encode(pdf_data).decode("utf-8")

# # Prepare the request payload
# payload = {
#     "model": "gpt-4.1",
#     "input": [
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_file",
#                     "filename": "Urine Test Walter Harris profile 7 Jan24.pdf",
#                     "file_data": f"data:application/pdf;base64,{base64_pdf}",
#                 },
#                 {
#                     "type": "input_text",
#                     "text": (
#                         "This is a medical test report. Please tell me if it is related to blood, urine, or DNA. "
#                         "Return only a JSON in this format:\n{\"file_type\": \"blood\"} or \"urine\" or \"dna\""
#                     ),
#                 },
#             ],
#         },
#     ],
    
# }

# # Set up the request headers
# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json",
# }

# # Send the request to OpenAI's API
# response = requests.post("https://api.openai.com/v1/responses", headers=headers, json=payload)

# # Extract and print JSON
# try:
#     print(response.json()['output'][0]['content'][0]['text'])
# except (KeyError, IndexError):
#     print(f"Error: {response.status_code} - {response.text}")