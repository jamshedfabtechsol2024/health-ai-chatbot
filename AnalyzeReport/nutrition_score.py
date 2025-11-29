import sys
from pathlib import Path

# Add the project root to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))


import json
import logging
from Models.models import report_analysis_model
from AnalyzeReport.prompt import Prompts
from pprint import pprint


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class NutritionScore:

    def nutrition_score(self, nutrition_input_data):
        prompt = Prompts.nutrition_score_prompt.format(input_data_to_calculate_nutrition_score=nutrition_input_data)
        output = report_analysis_model.invoke(prompt)
        return output.content










nutrition_input_data = """{
 "age": 42,
 "sex": "female",
 "height_centimeters": 168,
 "weight_kilograms": 72,
 "body_mass_index": 25.5,
 "dietary_preference": "omnivore",
 "conditions": ["diabetes"],
 "nutrition_summary_28_day": {
   "meal_logging_completeness_percent": 85
 },
 "streaks_28_day": {
   "meal_logging_days_ratio_28_day": 0.75,
   "max_consecutive_offplan_days": 3
 },
 "clinical_bands": {
   "hemoglobin_a1c_band": "orange",
   "ldl_cholesterol_band": "red",
   "hdl_cholesterol_band": "green",
   "triglycerides_band": "orange",
   "apolipoprotein_b_band": "orange",
   "estimated_glomerular_filtration_rate_band": "green",
   "urine_albumin_to_creatinine_ratio_band": "green",
   "ferritin_band": "orange",
   "vitamin_d_band": "orange",
   "calcium_band": "green",
   "iron_band": "orange"
 }
}"""






score = NutritionScore()
output = score.nutrition_score(nutrition_input_data)
pprint(output)
