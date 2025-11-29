import sys
import json
import logging
from pathlib import Path
from json_repair import repair_json


from Models.models import report_analysis_model
from AnalyzeReport.prompt import Prompts
from utils.utils import HealthReportUtils
from AnalyzeReport.prompt import Prompts
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))


class HealthReportAnalyzer:
    def __init__(self, user_id: int, report_type: str):
        self.user_id = user_id
        self.report_type = report_type.lower()
        self.utils = HealthReportUtils()

    def analyze_report(self, file_path: str) -> dict:
        try:
            # Extract text
            extracted_text = self.utils.extract_text_from_pdf(file_path)
            # Check the Which reletd the report (blood, urine, dna)
            file_type = self.utils.check_report_type(extracted_text)

            if file_type['file_type'] in ["blood","urine","dna"]:
                # Analyze the text
                # print(f"Analyzing {self.report_type} report")
                analysis_results = self.utils.analyze_text(
                    text=extracted_text,
                    file_type=file_type['file_type'],
                    prompt = getattr(Prompts, f"{file_type['file_type'].upper()}_ANALYSIS_PROMPT")
                )

                raw_analysis_str = analysis_results.get("raw_analysis", "{}")

                cleaned_str = raw_analysis_str.strip()

                repaired = repair_json(cleaned_str)
                raw_analysis = json.loads(repaired)
    
                raw_analysis["score_data"] = {}
                raw_analysis["score_data"]["file_type"] = file_type['file_type']
                
                analysis_results["raw_analysis"] = json.dumps(raw_analysis, indent=4, ensure_ascii=False)
                
                # print("----------------------")
                # print(analysis_results, "-------------------------------")
                return analysis_results
                
            else:
                return {}

        except Exception as e:
            logger.error(f"Error analyzing {self.report_type} report: {str(e)}")
            raise



