import sys
from pathlib import Path
import logging
from dotenv import load_dotenv
from pprint import pprint

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

def start_qa(user_id: int, user_input:str, chatbot_type: str, history_msgs, survey, report_text):
    """Handle QA session."""
    try:
        # Initialize chatbot with appropriate type
        qa = Chatbot(chatbot_type=chatbot_type, user_id=user_id, history_msgs=history_msgs)
        response = qa.start_interactive_session(user_input, survey, report_text)
        
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

def main(user_id, user_input,file_path, report_type, chatbot_type, history_msgs, survey, report_text):
    # Load environment variables
    load_dotenv()

    # Decision logic:
    if file_path:
        analysis_report_data  = FileAnalysis(user_id, file_path, report_type=report_type)
        return analysis_report_data
    else:
        print(f"Starting QA session for user: {user_id} with input: {user_input}")
        response = start_qa(user_id, user_input=user_input, chatbot_type=chatbot_type, history_msgs=history_msgs, survey=survey, report_text=report_text)
        return response


user_id = "hamza@gmail.com"
# file_path = ""
file_path = "https://ocr-tests-bucket.s3.amazonaws.com/295727ff-107a-45d8-91c2-96891fa2f1b7/BloodReport.pdf"                                  #         "https://ocr-tests-bucket.s3.amazonaws.com/e754f460-b0e3-4c1e-aab0-6390c2f98210/Test Folder new/Urine Test Walter Harris profile 7 Jan24.pdf"                        "https://ocr-tests-bucket.s3.us-east-2.amazonaws.com/profile%2FDNA_Profile3_Corrected_v1%20(2).pdf"                    "https://ocr-tests-bucket.s3.us-east-2.amazonaws.com/profile%2FDNA_Test_Report_Lisa_Raymond_Profile4.pdf"                              "https://ocr-tests-bucket.s3.us-east-2.amazonaws.com/profile%2FDNA_Test_Report_Profiel2_Julia_Martinez.pdf"                     "https://ocr-tests-bucket.s3.us-east-2.amazonaws.com/profile%2FCarlos_Profile5_DNA_Results_v1%20(1).pdf"                 "https://ocr-tests-bucket.s3.us-east-2.amazonaws.com/profile%2FDNA%20Test%20Report%20Profile%208%20Margaret.pdf"                     "https://ocr-tests-bucket.s3.amazonaws.com/2e2da856-612c-4a1b-a417-9104226938c0/DNA Test Report Profile 7 Walter.pdf"                "https://ocr-tests-bucket.s3.amazonaws.com/2e2da856-612c-4a1b-a417-9104226938c0/image%20(2).png"     
report_type = "lab" #lab


user_input = "What is my score" 
chatbot_type = "lab" # lab, dna, nutrition, therapist, workout
history_msgs = [
    # {"role": "user", "content": "Hi, I need some help."},
    # {"role": "assistant", "content": "Hello! I'm here for you. Tell me what's going on."},
    # {"role": "user", "content": "what is machine learning?"},
    # {"role": "assistant", "content": """Machine learning is a field of artificial intelligence focused on enabling systems to learn from data and improve their performance on specific tasks without explicit programming."""}
]
survey = {
        "health_score_summary": {
        "wisehealthscore_3days": 85,
        "wisehealthscore_week": 82,
        "wisehealthscore_month": 80,
        "blood_score": 78,
        "urine_score": 83,
        "dna_score": 86,
        "mental_score": 66,
        "nutrition_score": 72,
        "workout_score": 74,
        "age":38,
        "bmi":24.7
        },
        "insights": [
        "No bacteria detected on microscopy, mconsistent with absence of infection.",
        "Aligns with negative leukocyte esterase and nitrite results.",
        "No evidence of asymptomatic bacteriuria at time of test.",
        "Reduces concern for UTI or contamination.",
        "Consistent with good urinary tract health."
        ]
      }


report_text = {
  "tests": {
    "Kidney Function": [
      {
        "name": "Protein",
        "value": "Negative",
        "status": "Normal",
        "analysis": [
          "Absence of protein in urine suggests normal glomerular filtration barrier integrity.",
          "No evidence of proteinuria, which is associated with kidney disease.",
          "Normal result decreases likelihood of nephrotic syndrome.",
          "Regular monitoring is prudent given patient's advanced age.",
          "This result supports preserved kidney function."
        ],
        "recommendations": [
          "Continue periodic urine screening due to age-related risk.",
          "Maintain optimal blood pressure to protect kidney health.",
          "Monitor for new symptoms such as edema or foamy urine.",
          "Encourage adequate hydration.",
          "Review medications for nephrotoxic potential."
        ]
      },
      {
        "name": "Creatinine (Random)",
        "value": "111 mg/dL",
        "status": "Normal",
        "analysis": [
          "Creatinine falls within age-adjusted normal limits.",
          "Stable creatinine suggests preserved glomerular filtration rate.",
          "No signs of acute or chronic renal dysfunction.",
          "Creatinine may increase with muscle mass loss but is appropriate for this patient.",
          "Regular trend monitoring is especially important in elderly."
        ],
        "recommendations": [
          "Monitor renal function at least annually.",
          "Encourage renal-protective lifestyle (limit NSAIDs, avoid dehydration).",
          "Review for urinary symptoms or changes.",
          "Evaluate all new medications for renal clearance impact.",
          "Consider assessment of eGFR in context of overall health."
        ]
      },
      {
        "name": "Microalbumin",
        "value": "16 mg/L",
        "status": "Normal",
        "analysis": [
          "Microalbumin is below the threshold for microalbuminuria.",
          "Low albumin excretion indicates absence of early kidney damage.",
          "Important parameter in diabetes/hypertension; normal here.",
          "Supports the absence of diabetic nephropathy.",
          "Persistent normal levels indicate good vascular and renal health."
        ],
        "recommendations": [
          "Screen periodically if any risk factors for nephropathy develop.",
          "Control blood glucose and blood pressure if applicable.",
          "Educate on signs of early kidney disease.",
          "Maintain heart-healthy lifestyle.",
          "Repeat testing in case of new risk factors (e.g. diabetes diagnosis)."
        ]
      },
      {
        "name": "Albumin/Creatinine Ratio (ACR)",
        "value": "14.4 mg/g",
        "status": "Normal",
        "analysis": [
          "Ratio is well below threshold for albuminuria.",
          "No evidence of chronic kidney disease (CKD) or progression.",
          "Indicates proper filtration function of kidneys.",
          "Supports absence of glomerular damage.",
          "Good parameter for longitudinal monitoring in elderly."
        ],
        "recommendations": [
          "Continue with ACR screening yearly.",
          "Monitor for changes if comorbidities arise.",
          "Maintain cardiovascular and renal health.",
          "Address any new onset of urinary symptoms rapidly.",
          "Educate about importance of ongoing monitoring with age."
        ]
      }
    ],
    "Hydration & Electrolytes": [
      {
        "name": "Specific Gravity",
        "value": "1.022",
        "status": "Normal",
        "analysis": [
          "Specific gravity indicates urine is appropriately concentrated.",
          "No signs of dehydration or overhydration.",
          "Kidneys are actively concentrating or diluting urine as needed.",
          "Test eliminates concern for diabetes insipidus or SIADH.",
          "Supports normal hydration status, adjusted for age."
        ],
        "recommendations": [
          "Encourage continued adequate fluid intake.",
          "Monitor specific gravity if symptoms of dehydration/overhydration occur.",
          "Be vigilant for acute illnesses impacting fluid status.",
          "Assess for medication impacts on hydration.",
          "Educate on aligning fluid intake according to environmental needs."
        ]
      }
    ],
    "Liver & Metabolism": [
      {
        "name": "Glucose",
        "value": "Negative",
        "status": "Normal",
        "analysis": [
          "No glucose present, ruling out glucosuria.",
          "Absence suggests no severe hyperglycemia at time of test.",
          "No evidence of uncontrolled diabetes.",
          "Supports normal carbohydrate metabolism.",
          "No renal threshold exceeded for glucose."
        ],
        "recommendations": [
          "Encourage routine blood glucose monitoring if diabetic risk exists.",
          "Maintain healthy diet to support normal glucose metabolism.",
          "Repeat test if symptoms of polyuria, polydipsia, or unexplained weight loss develop.",
          "Assess fasting glucose if indicated clinically.",
          "Educate on symptoms of hyper- or hypoglycemia."
        ]
      },
      {
        "name": "Ketones",
        "value": "Negative",
        "status": "Normal",
        "analysis": [
          "No ketone bodies detected, ruling out ketosis or ketoacidosis.",
          "No significant fat breakdown or prolonged fasting present.",
          "Rules out diabetic ketoacidosis.",
          "Normal in absence of diet-induced ketogenesis.",
          "Supports stable energy metabolism."
        ],
        "recommendations": [
          "Maintain regular, balanced nutrition.",
          "Monitor for signs of metabolic imbalance.",
          "Important to recheck if unintentional weight loss occurs.",
          "Avoid prolonged fasting unless medically required.",
          "Educate about risks of dehydration or excessive diuresis."
        ]
      },
      {
        "name": "Bilirubin",
        "value": "Negative",
        "status": "Normal",
        "analysis": [
          "No bilirubin detected in urine, ruling out liver pathology.",
          "Supports proper hepatic clearance of bilirubin.",
          "No conjugated hyperbilirubinemia present.",
          "No evidence of obstructive or hepatocellular jaundice.",
          "Unlikely to have significant hemolysis."
        ],
        "recommendations": [
          "Monitor for jaundice, dark urine, or pale stools.",
          "Repeat liver function tests periodically in elderly.",
          "Maintain healthy lifestyle to protect hepatic function.",
          "Avoid hepatotoxic substances or medications.",
          "Seek prompt evaluation if hepatic symptoms develop."
        ]
      },
      {
        "name": "Urobilinogen",
        "value": "Normal",
        "status": "Normal",
        "analysis": [
          "Normal urobilinogen indicates effective bilirubin breakdown.",
          "No evidence of hemolysis, liver dysfunction, or biliary obstruction.",
          "No excessive hepatic or hemolytic activity.",
          "Supports intact enterohepatic circulation.",
          "Consistent with other normal markers of liver/blood function."
        ],
        "recommendations": [
          "Maintain routine monitoring.",
          "Assess if any changes in stool color or frequency develop.",
          "Consider comprehensive liver panel if risk factors increase.",
          "Continue to avoid hepatotoxic agents.",
          "Educate on liver disease warning signs."
        ]
      }
    ],
    "Urinary Tract Health": [
      {
        "name": "Leukocyte Esterase",
        "value": "Negative",
        "status": "Normal",
        "analysis": [
          "No leukocyte esterase means no significant white blood cell activity in urine.",
          "Unlikely to have urinary tract infection (UTI).",
          "No evidence of pyuria.",
          "No ongoing inflammation of urinary tract.",
          "Normal immune response locally."
        ],
        "recommendations": [
          "Monitor for UTI symptoms (pain, frequency, urgency).",
          "Practice proper perineal hygiene.",
          "Instruct on prompt reporting of urinary symptoms.",
          "Avoid unnecessary use of urinary catheters.",
          "Encourage hydration to reduce UTI risk."
        ]
      },
      {
        "name": "Nitrites",
        "value": "Negative",
        "status": "Normal",
        "analysis": [
          "No nitrites indicate absence of significant gram-negative bacterial activity.",
          "Reduces concern for bacteriuria.",
          "Negative nitrites reduce likelihood of infection with nitrate-reducing bacteria.",
          "Supports clear urinary tract.",
          "Aligns with absence of leukocytes and bacteria."
        ],
        "recommendations": [
          "Continue to monitor for infection signs.",
          "Advise increased water intake as appropriate.",
          "Seek evaluation for new onset urinary symptoms.",
          "Avoid excessive use of antibiotics.",
          "Periodic urine checks if risk factors arise."
        ]
      },
      {
        "name": "Blood (Microscopic)",
        "value": "Negative",
        "status": "Normal",
        "analysis": [
          "No microscopic hematuria detected.",
          "Reduces likelihood of trauma, stones, or infection.",
          "No glomerulonephritis or malignancy signs.",
          "Normal for age; unchanged from baseline.",
          "Supports urinary tract mucosal integrity."
        ],
        "recommendations": [
          "Monitor for any visible blood in urine.",
          "Annual urinalysis for hematuria screening.",
          "Promptly evaluate gross hematuria.",
          "Consider urology referral if new microscopic hematuria detected.",
          "Support kidney health through risk factor management."
        ]
      },
      {
        "name": "pH",
        "value": "6.0",
        "status": "Normal",
        "analysis": [
          "Urine pH is within normal physiologic range.",
          "Slightly acidic, typical for omnivorous diet.",
          "No metabolic acidosis/alkalosis indicated.",
          "Supports normal acid-base balance.",
          "No suggestion of renal tubular acidosis."
        ],
        "recommendations": [
          "Encourage balanced nutrition to sustain pH.",
          "Monitor pH if recurrent urinary stones are a concern.",
          "Hydrate well to maintain optimal pH.",
          "Evaluate pH in context of repeated abnormal results.",
          "Assess for dietary factors influencing urine pH."
        ]
      }
    ],
    "Microscopic & Physical": [
      {
        "name": "Color",
        "value": "Yellow",
        "status": "Normal",
        "analysis": [
          "Clear yellow color reflects adequate hydration and normal pigment excretion.",
          "No evidence of hematuria or concentrated/dilute urine issues.",
          "No abnormal discoloration from foods, medications, or bile pigments.",
          "Typical color for healthy urine.",
          "Consistent with normal specific gravity."
        ],
        "recommendations": [
          "Monitor for changes to dark, red, brown, or cloudy urine.",
          "Stay adequately hydrated to maintain color.",
          "Assess if dietary or medication changes alter color.",
          "Consult provider if persistent discoloration develops.",
          "Document any symptomatic color changes."
        ]
      },
      {
        "name": "Appearance (Clarity)",
        "value": "Clear",
        "status": "Normal",
        "analysis": [
          "Clear urine implies absence of pus, blood, or excessive crystals.",
          "No sediment or cloudiness from infection or protein.",
          "Healthy renal and urinary tract functioning.",
          "No signs of phosphaturia or hyperoxaluria.",
          "Suggests low bacterial/particulate load."
        ],
        "recommendations": [
          "Prompt review if urine becomes cloudy or murky.",
          "Maintain hygiene to reduce infection risks.",
          "Increase fluid intake during illness.",
          "Repeat urinalysis if gross sediment noted.",
          "Avoid dehydration for optimal clarity."
        ]
      },
      {
        "name": "WBCs",
        "value": "0-2 /HPF",
        "status": "Normal",
        "analysis": [
          "White cells are within normal low count.",
          "No significant pyuria.",
          "No evidence for infection or inflammation.",
          "Healthy mucosal immunity.",
          "Consistent with negative leukocyte esterase."
        ],
        "recommendations": [
          "Continue to monitor if new urinary symptoms occur.",
          "Retest WBC in urine if fever, pain, or dysuria arise.",
          "Reinforce hygiene habits.",
          "Periodic urinalysis is appropriate.",
          "Consult for persistent elevation on repeat."
        ]
      },
      {
        "name": "RBCs",
        "value": "0-1 /HPF",
        "status": "Normal",
        "analysis": [
          "Very low red cell count, considered normal.",
          "No gross or microscopic hematuria concern.",
          "Stable finding for advanced age.",
          "Supports absence of trauma or stone.",
          "Matches negative blood and normal clarity."
        ],
        "recommendations": [
          "Continue routine screening.",
          "Evaluate for new hematuria if trauma/infection suspected.",
          "Recheck if any unexplained renal symptoms appear.",
          "Patient education on hematuria signs.",
          "Consider imaging only if new findings emerge."
        ]
      },
      {
        "name": "Epithelial Cells",
        "value": "Few /HPF",
        "status": "Normal",
        "analysis": [
          "Few epithelial cells is common and within acceptable range for age.",
          "No sign of severe desquamation or urothelial shedding.",
          "Possible mild age-related sloughing.",
          "No suggestion of urinary tract malignancy or irritation.",
          "Not indicative of contamination in this context."
        ],
        "recommendations": [
          "Continue age-appropriate monitoring.",
          "Reinforce good perineal hygiene.",
          "Recheck if large increase in future samples.",
          "Correlate with any genitourinary symptoms.",
          "Educate on significance of increased epithelial count."
        ]
      },
      {
        "name": "Bacteria",
        "value": "None observed",
        "status": "Normal",
        "analysis": [
          "No bacteria seen microscopically.",
          "Unlikely to have asymptomatic bacteriuria.",
          "No evidence of active infection.",
          "Concordant with negative nitrites and leukocyte esterase.",
          "Supports aseptic technique during collection."
        ],
        "recommendations": [
          "No need for antibiotics or further culture.",
          "Monitor for UTI signs, especially in elderly.",
          "Maintain good personal hygiene.",
          "Recheck if symptoms suggest infection.",
          "Educate about risk factors for infection due to advanced age."
        ]
      }
    ],
    "Advanced Biomarkers": []
  },
  "score_data": {
    "file_type": "urine"
  }
}


output = main(user_id=user_id, user_input=user_input ,file_path=file_path, report_type=report_type, chatbot_type=chatbot_type, history_msgs=history_msgs, survey=survey, report_text=report_text)
pprint(output)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         