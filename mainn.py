import sys
import os
from pathlib import Path
import logging
from dotenv import load_dotenv
from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from AnalyzeReport.analyze_report import HealthReportAnalyzer
from Chatbot.chatbot import Chatbot

def FileAnalysis(user_id: int, file_path: str, report_type: str):
    try:
        analyzer = HealthReportAnalyzer(user_id, report_type=report_type)
        results = analyzer.analyze_report(file_path)

        return results
        
    except Exception as e:
        logger.error(f"Error analyzing report: {str(e)}")
        sys.exit(1)

def start_qa(user_id: int, user_input:str, chatbot_type: str, history_msgs, survey):
    """Handle QA session."""
    try:
        # Initialize chatbot with appropriate type
        qa = Chatbot(chatbot_type=chatbot_type, user_id=user_id, history_msgs=history_msgs)
        response = qa.start_interactive_session(user_input, survey)
        
        if response["status"] == "success":
            return response
        else:
            return response
            
    except Exception as e:
        error_response = {
            "status": "error",
            "error": str(e),
            "chatbot_type": chatbot_type
        }
        logger.error(f"Error in QA session: {str(e)}")
        return error_response

def main(user_id, user_input,file_path, report_type, chatbot_type, history_msgs, survey):
    print(survey, 'survey is this')
    print(history_msgs, 'history is this')
    # Load environment variables
    load_dotenv()

    # Decision logic:
    if file_path:
        analysis_report_data = analyze_report(user_id, file_path, report_type=report_type)
        return analysis_report_data
    else:
        print(f"Starting QA session for user: {user_id} with input: {user_input}")
        response = start_qa(user_id, user_input=user_input, chatbot_type=chatbot_type, history_msgs=history_msgs, survey=survey)
        return response


user_id = "hamza@gmail.com"
file_path = ""
# file_path = "https://ocr-tests-bucket.s3.amazonaws.com/e754f460-b0e3-4c1e-aab0-6390c2f98210/Test Folder new/Urine Test Walter Harris profile 7 Jan24.pdf"           #    "https://ocr-tests-bucket.s3.amazonaws.com/295727ff-107a-45d8-91c2-96891fa2f1b7/BloodReport.pdf"                "https://ocr-tests-bucket.s3.us-east-2.amazonaws.com/profile%2FDNA%20Test%20Report%20Profile%208%20Margaret.pdf"            "https://ocr-tests-bucket.s3.amazonaws.com/2e2da856-612c-4a1b-a417-9104226938c0/DNA Test Report Profile 7 Walter.pdf"                "https://ocr-tests-bucket.s3.amazonaws.com/2e2da856-612c-4a1b-a417-9104226938c0/image%20(2).png"     
report_type = "nutrition" #lab
user_input = "What is airplane" #What is the Hemoglobin value?
chatbot_type = "lab" # lab, dna, nutrition, therapist, workout
# chatbot_type = "" 
history_msgs = [
    {"role": "user", "content": "Hi, I need some help."},
    {"role": "assistant", "content": "Hello! I'm here for you. Tell me what's going on."},
    {"role": "user", "content": "what is machine learning?"},
    {"role": "assistant", "content": """Machine learning is a field of artificial intelligence focused on enabling systems to learn from data and improve their performance on specific tasks without explicit programming."""}
]
survey = [
  {
    "question": "How are you feeling today when it comes to food and nourishment?",
    "answer": "I'm off track today. I ate fast food for lunch and skipped breakfast."
  },
  {
    "question": "Would you like to tell me more about today’s meals or any struggles?",
    "answer": "I’ve been stress-eating and haven’t had any fruits or vegetables yet."
  },
  {
    "question": "Quick check — how’s your body feeling right now?",
    "answer": "I feel heavy and a bit bloated."
  },
  {
    "question": "What would support you best right now?",
    "answer": "A simple healthy dinner idea would help."
  }
]

previous_reports_data=[
{
  "score_data": {
    "report_name": "blood",
    "score": 50,
    "status": "Fair"
  },
  "tests": [
    {
      "name": "Hemoglobin",
      "value": "13.0 g/dL",
      "status": "Low",
      "analysis": [
        "Hemoglobin is slightly low, which may suggest mild anemia or blood loss."
      ]
    },
    {
      "name": "RBC Count",
      "value": "4.20 million/amm",
      "status": "Low",
      "analysis": [
        "Low RBC count may indicate anemia or a bone marrow issue."
      ]
    },
    {
      "name": "WBC Count",
      "value": "12500 /cmm",
      "status": "High",
      "analysis": [
        "High WBC count may indicate infection or inflammation."
      ]
    },
    {
      "name": "Platelet Count",
      "value": "135000 /cmm",
      "status": "Low",
      "analysis": [
        "Low platelet count may indicate a risk of bleeding or bone marrow disorder."
      ]
    },
    {
      "name": "MPV",
      "value": "14.5 fL",
      "status": "High",
      "analysis": [
        "High MPV may suggest increased platelet production due to inflammation."
      ]
    }
  ]
},
{
  "score_data": {
    "report_name": "blood",
    "score": 50,
    "status": "improving"
  },
  "tests": [
    {
      "name": "Hemoglobin",
      "value": "13.8 g/dL",
      "status": "Normal",
      "analysis": [
        "Hemoglobin is within the normal range, indicating improved oxygen-carrying capacity."
      ]
    },
    {
      "name": "RBC Count",
      "value": "4.50 million/amm",
      "status": "Normal",
      "analysis": [
        "RBC count is near the normal range, suggesting recovery from anemia."
      ]
    },
    {
      "name": "WBC Count",
      "value": "11500 /cmm",
      "status": "High",
      "analysis": [
        "WBC count remains slightly elevated, possibly due to ongoing mild infection."
      ]
    },
    {
      "name": "Platelet Count",
      "value": "140000 /cmm",
      "status": "Normal",
      "analysis": [
        "Platelet count is at the lower end of normal, which is acceptable but should be monitored."
      ]
    },
    {
      "name": "MPV",
      "value": "14.2 fL",
      "status": "High",
      "analysis": [
        "High MPV still indicates active platelet production, possibly due to recovery."
      ]
    }
  ]
},
{
  "score_data": {
    "report_name": "blood",
    "score": 69,
    "status": "good"
  },
  "tests": [
    {
      "name": "Hemoglobin",
      "value": "14.2 g/dL",
      "status": "Normal",
      "analysis": [
        "Hemoglobin is in the normal range."
      ]
    },
    {
      "name": "RBC Count",
      "value": "4.70 million/amm",
      "status": "Normal",
      "analysis": [
        "RBC count is in the normal range."
      ]
    },
    {
      "name": "WBC Count",
      "value": "10900 /cmm",
      "status": "Slightly High",
      "analysis": [
        "WBC count is slightly above normal, may indicate resolving infection."
      ]
    },
    {
      "name": "Platelet Count",
      "value": "145000 /cmm",
      "status": "Normal",
      "analysis": [
        "Platelet count is normal."
      ]
    },
    {
      "name": "MPV",
      "value": "14.0 fL",
      "status": "High",
      "analysis": [
        "High MPV could still reflect residual inflammation or healing."
      ]
    }
  ]
},
{
  "score_data": {
    "report_name": "blood",
    "score": 85,
    "status": "very good"
  },
  "tests": [
    {
      "name": "Hemoglobin",
      "value": "14.7 g/dL",
      "status": "Normal",
      "analysis": [
        "Hemoglobin is at a healthy level."
      ]
    },
    {
      "name": "RBC Count",
      "value": "4.85 million/amm",
      "status": "Normal",
      "analysis": [
        "RBC count is normal."
      ]
    },
    {
      "name": "WBC Count",
      "value": "9900 /cmm",
      "status": "Normal",
      "analysis": [
        "WBC count is now in normal range, indicating recovery."
      ]
    },
    {
      "name": "Platelet Count",
      "value": "150000 /cmm",
      "status": "Normal",
      "analysis": [
        "Platelet count is normal and stable."
      ]
    },
    {
      "name": "MPV",
      "value": "13.5 fL",
      "status": "Normal",
      "analysis": [
        "MPV is back in normal range, suggesting reduced inflammation."
      ]
    }
  ]
},
{
  "score_data": {
    "report_name": "blood",
    "score": 91,
    "status": "Excellent"
  }, 
  "tests": [
    {
      "name": "Hemoglobin",
      "value": "15.0 g/dL",
      "status": "Normal",
      "analysis": [
        "Hemoglobin is excellent, indicating optimal oxygen-carrying capacity."
      ]
    },
    {
      "name": "RBC Count",
      "value": "4.90 million/amm",
      "status": "Normal",
      "analysis": [
        "RBC count is at a healthy level."
      ]
    },
    {
      "name": "WBC Count",
      "value": "8900 /cmm",
      "status": "Normal",
      "analysis": [
        "WBC count is completely normal."
      ]
    },
    {
      "name": "Platelet Count",
      "value": "160000 /cmm",
      "status": "Normal",
      "analysis": [
        "Platelet count is strong and stable."
      ]
    },
    {
      "name": "MPV",
      "value": "11.5 fL",
      "status": "Normal",
      "analysis": [
        "MPV is within the normal range, no signs of inflammation."
      ]
    }
  ]
}
]


# db = next(get_db())
# output = main(user_id=user_id, user_input=user_input ,file_path=file_path, report_type=report_type, chatbot_type=chatbot_type,history_msgs=history_msgs, db=db)
# print(output)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         