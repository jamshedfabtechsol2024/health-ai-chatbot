import sys
from pathlib import Path

# Add the project root to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))


import json
from Models.models import report_analysis_model
from AnalyzeReport.prompt import Prompts
from pprint import pprint


class WorkoutScore:

    def workout_score(self, workout_input_data):
        prompt = Prompts.workout_score_prompt.format(input_data_to_calculate_workout_score=workout_input_data)
        output = report_analysis_model.invoke(prompt)
        return json.loads(output.content)










workout_input_data = """
{
"age": 34,
"sex": "male",
"height_centimeters": 178,
"weight_kilograms": 78,
"body_mass_index": 24.6,
"training_age": "intermediate",
"primary_goal": "Hybrid",
"plan_targets": {
"weekly_sessions_target": 4,
"strength_sessions_target": 3,
"mobility_minutes_target": 90,
"steps_target_band": [8000,12000],
"mvpa_target_band_minutes": [180,320],
"intensity_mix_target_share":{
"zone_1":0.55,"zone_2":0.25,"zone_3":0.12,"zone_4":0.06,"zone_5":0.02
}
},
"wisehealth_general_score_7_day": 82,
"wisehealth_general_score_28_day": 84,
"nutrition_score_7_day": 79,
"nutrition_score_28_day": 81,
"workout_summary_7_day": {
"sessions_completed": 4,
"moderate_to_vigorous_physical_activity_minutes": 220,
"long_sessions_count": 2,
"strength_sessions_completed": 3,
"mobility_minutes": 90,
"average_daily_steps": 9800,
"high_intensity_sessions_count": 1
},
"workout_summary_28_day": {
"sessions_completed": 16,
"moderate_to_vigorous_physical_activity_minutes": 880,
"long_sessions_count": 7,
"strength_sessions_completed": 12,
"mobility_minutes": 340,
"average_daily_steps": 9600
},
"streaks_28_day": {
"current_active_streak_days": 9,
"maximum_consecutive_inactive_days_28_day": 2,
"streak_rule_ok_days_ratio_28_day": 0.93
},
"clinical_bands": {
"hemoglobin_a1c_band": "orange",
"low_density_lipoprotein_cholesterol_band": "orange",
"high_density_lipoprotein_cholesterol_band": "green",
"triglycerides_band": "orange",
"apolipoprotein_b_band": "orange",
"estimated_glomerular_filtration_rate_band": "green",
"urine_albumin_to_creatinine_ratio_band": "green",
"urine_specific_gravity_band": "orange",
"hemoglobin_band": "green",
"ferritin_band": "orange",
"high_sensitivity_c_reactive_protein_band": "green",
"thyroid_stimulating_hormone_band": "green",
"alanine_aminotransferase_band": "green",
"aspartate_aminotransferase_band": "green",
"urinary_tract_infection_flag_band": "green"
}
}
"""






score = WorkoutScore()
output = score.workout_score(workout_input_data)
pprint(output)
