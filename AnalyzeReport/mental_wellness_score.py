import sys
from pathlib import Path

# Add the project root to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))


import json
from Models.models import report_analysis_model
from AnalyzeReport.prompt import Prompts
from pprint import pprint


class MentalWellnessScore:

    def mental_wellness_score(self, mental_wellness_input_data):
        prompt = Prompts.mental_wellness_score_prompt.format(input_data_to_calculate_mental_wellness_score=mental_wellness_input_data)
        output = report_analysis_model.invoke(prompt)
        return json.loads(output.content)










mental_wellness_input_data = """
{
  "age": 29,
  "sex": "male",
  "history_flags": ["none"],
  "therapy_status": "not_in_therapy",
  "plan_targets": {
    "check_in_days_target_ratio": 0.7
  },
  "wisehealth_general_score_28_day": 80,
  "workout_score_28_day": 72,
  "nutrition_score_28_day": 78,
  "mood_average_7_day": 6.2,
  "stress_average_7_day": 5.1,
  "mood_average_28_day": 6.5,
  "stress_average_28_day": 4.8,
  "check_in_days_ratio_28_day": 0.75,
  "longest_inactive_streak_days_28_day": 4,
  "adherence_score_tools": 0.68,
  "baseline_mood_average_90_day": 6.0,
  "baseline_stress_average_90_day": 5.2
}
"""






score = MentalWellnessScore()
output = score.mental_wellness_score(mental_wellness_input_data)
pprint(output)
