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


class Plans_without_report:

    def nutrition_plan_without_report(self, start_date, start_day, end_date, end_day, skip_dates, user_profile):

        prompt = Prompts.NUTRITION_PLAN_WITHOUT_REPORT.format(user_profile=user_profile, current_date=start_date, current_day=start_day, end_date=end_date, end_day=end_day, skip_dates=skip_dates)
        output = report_analysis_model.invoke(prompt)
        return output.content

    def workout_plan_without_report(self, current_date, current_day, end_date, end_day, skip_dates, user_profile):
        prompt = Prompts.WORKOUT_PLAN_WITHOUT_REPORT.format(user_profile=user_profile, current_date=current_date, current_day=current_day, end_date=end_date, end_day=end_day, skip_dates=skip_dates)
        output = report_analysis_model.invoke(prompt)
        return output.content







start_date="1/10/2025"
start_day="Wednesday"
end_date="5/10/2025"
end_day="Sunday"
skip_dates = ["02/10/2025", "03/10/2025", "04/10/2025"]

user_profile = {
  "gender": "Male",
  "date_of_birth": "1990-05-14",
  "weight_kg": "75",
  "height_cm": "180",
  "blood_group": "O+",
  "chronic_condition": "Hypertension",
  "major_illness": "Appendicitis (surgery in 2010)",
  "allergies": "Peanuts, Dust",
  "medication_allergies": "Penicillin",
  "hospitalization_history": "Hospitalized in 2018 for pneumonia",
  "daily_calorie_goal": 2200,
  "diet_type": "balanced",
  "activity_level": "moderate",
  "water_intake_goal_liters": 2.5
}


plan = Plans_without_report()
output = plan.nutrition_plan_without_report(start_date, start_day, end_date, end_day, skip_dates, user_profile)
pprint(output)
