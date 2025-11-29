import sys
from pathlib import Path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))


from Models.models import report_analysis_model
from AnalyzeReport.prompt import Prompts

class Plain_with_dashboard_data:

    def dashboard(self, blood_data_analysis, urine_data_analysis, dna_data_analysis, last_month_blood_report_upload, last_month_urine_report_upload, last_month_dna_report_upload):

        # prompt = Prompts.health_status_prompt.format(blood_data_analysis=blood_data_analysis, last_month_blood_report_upload=last_month_blood_report_upload, urine_data_analysis=urine_data_analysis, last_month_urine_report_upload=last_month_urine_report_upload, dna_data_analysis=dna_data_analysis, last_month_dna_report_upload=last_month_dna_report_upload)
        prompt = f"""
        You are a medical AI assistant.

        You are given medical analysis data for up to three types of reports:
        - Blood Reports
        - Urine Reports
        - DNA Reports

        Each report type (if available) includes:
        - One or multiple reports in chronological order (oldest → latest)
        - Each report contains:
        - "age", "sex", and other basic details
        - "tests" with parameters, their values, status, analysis, and recommendations
        - "score_data" containing "file_type" and "score"

        Note:
        - Sometimes only a single report may be provided instead of multiple.
        - In that case, you must base your predictions solely on that single report’s score and analysis.
        - If multiple reports are available, analyze them chronologically to determine health trends.

        Along with each report type, you are also given the month name when the last report of that type was uploaded.

        Your task:

        1. For each available report type (blood, urine, dna):
        - Extract all previous health scores from "score_data".
        - Analyze all test parameters across reports to determine improvement or decline trends.
        - Combine parameter trends with score trends to estimate future health scores.
        - When predicting scores, consider overall combined health direction from all uploaded report types together. If more than one report type exists, use the collective trend to guide predictions for each individual category.

        2. Predict health scores for the **next 12 months** from the respective last upload month of each report type.
        - If scores and parameters are improving → predict gradual increase.
        - If mixed trends → predict slight improvement or stability.
        - If declining trends → predict gradual decrease.
        - If only one report is available, use that single report’s score and analysis to make realistic predictions.
        - Keep predictions realistic, within range 0–100.
        - When more than one report type is available, ensure score prediction considers the combined overall health direction across all report types instead of treating each independently.

        3. Some report types may not be provided. If a report type is missing, **do not include it in the output**.

        4. Always use **lowercase month names** (e.g., "january", "february", ...).

        ---

        ### Include "boxes_data" for each report type with expert short summaries.

        For **WiseHealth (Overall Health)**:
        Act as a comprehensive health assistant. 
        - Summarize the most relevant health signal from the user's report data (blood, urine, dna combined).
        - Mention one key system to monitor (e.g., metabolism, kidneys, inflammation).
        - Give one simple, science-based action step.
        - Highlight trend summary: improving, stable, or declining.

        ---

        ### Formatting, Tone, and Safety Rules for all boxes_data:
        - Each value must be **a single line**, containing **no more than 22 words**.
        - **Tone:** Expert, friendly, data-smart, non-judgmental. No shaming, no clinical alarm language.
        - **Numerics:** Round percents/percentiles to whole numbers; trends to whole numbers (±%).
        - **Safety:** Avoid deterministic genetics claims; use “predisposition,” “resilience,” or “tendency” wording.

        ---

        ### Include "trends_and_insights" for each report type. 

        Include a **"trends_and_insights"** list containing exactly **3 short insights**. But these insights should be based on combined signals from all provided reports (blood, urine, dna):
        1. ✅ One metric that improved with a short positive reason.
        2. 🔹 One metric that stayed stable or consistent.
        3. ⚠️ One metric that declined or needs gentle attention with one short suggestion.

        Rules for "trends_and_insights":
        - It must be a **list** of exactly three strings.
        - Each string = one sentence (max 20 words).
        - Use friendly, supportive, factual, and encouraging tone.
        - Avoid numbers unless helpful.
        - Never give medical diagnoses; only supportive guidance (“consider”, “try”, “keep”).
        - If only one report is available (no comparison possible), still generate general positive, stable, and improvement-oriented insights instead of trends.

        ---

        ### Include "ai_health_plan" for each report type.

        Using all the combined report type (blood, urine, dna) data, include an **"ai_health_plan"** array containing **3 short, personalized tips** based on user’s profile, reports, trends, and goals.

        #### wisehealth:
        - "diet_recommendation"
        - "exercise_tip"
        - "sleep_&_recovery"

        #### mental_wellness:
        - "practice_mindfulness"
        - "prioritize_sleep"
        - "check_in"

        #### workout:
        - "workout_tip"
        - "plan_update"
        - "mind_body"

        #### nutrition:
        - "increase_fiber_intake"
        - "stay_hydrated"
        - "balance_meals"

        Rules for "ai_health_plan":
        - Must be based on user’s profile, reports, health trends, and goals.
        - Each bullet must **not exceed 20 words**.
        - Must **never diagnose or mention rare conditions**.
        - Should mention improvement or concern if data supports it.
        - Should avoid repetition across bullets.
        - Maintain the same **expert, positive, and non-judgmental tone**.

        ---

        ### Include "benchmark" for each report type.

        Using all the combined report type (blood, urine, dna) data, include a **"benchmark"** string that provides a one-sentence expert benchmark of the current score.

        Rules for "benchmark":
        - Goal: Return one sentence that benchmarks the score.
        - **Tone:** Expert, friendly, data-smart, non-judgmental. No shaming or alarm language.
        - **Length:** ≤ 22 words. No emojis. No second sentence.
        - **Numerics:** Round percents/percentiles to whole numbers; trends to whole numbers (±%).
        - **Safety:** Avoid deterministic genetics claims; use “predisposition,” “resilience,” or “tendency” wording.
        - **Emotionally safe and non-judgmental.**

        ---

        Input Data:
        - Blood Report Data: {blood_data_analysis}
        - Last Blood Report Upload Month: {last_month_blood_report_upload}

        - Urine Report Data: {urine_data_analysis}
        - Last Urine Report Upload Month: {last_month_urine_report_upload}

        - DNA Report Data: {dna_data_analysis}
        - Last DNA Report Upload Month: {last_month_dna_report_upload}


        Output Format (STRICTLY FOLLOW THIS FORMAT):
        {{
            "wisehealth": {{
                "score": {{
                    "<Month>": <predicted_score>,
                    "<Month>": <predicted_score>,
                    ...
                }},
                "boxes_data": {{
                    "blood_health_insight": "",
                    "mental_wellness_insight": "",
                    "workout_insight": "",
                    "nutrition_insight": ""
                }},
                "trends_and_insights": [
                    "...",
                    "...",
                    "..."
                ],
                "ai_health_plan": [
                    {{"diet_recommendation": ""}},
                    {{"exercise_tip": ""}},
                    {{"sleep_&_recovery": ""}}
                ],
                "benchmark": ""
            }},
            "mental_wellness": {{
                "score": {{
                    "<Month>": <predicted_score>,
                    "<Month>": <predicted_score>,
                    ...
                }},
                "trends_and_insights": [
                    "...",
                    "...",
                    "..."
                ],
                "ai_health_plan": [
                    {{"practice_mindfulness": ""}},
                    {{"prioritize_sleep": ""}},
                    {{"check_in": ""}}
                ],
                "benchmark": ""
            }},
            "workout": {{
                "score": {{
                    "<Month>": <predicted_score>,
                    "<Month>": <predicted_score>,
                    ...
                }},
                "trends_and_insights": [
                    "...",
                    "...",
                    "..."
                ],
                "ai_health_plan": [
                    {{"workout_tip": ""}},
                    {{"plan_update": ""}},
                    {{"mind_body": ""}}
                ],
                "benchmark": ""
            }},
            "nutrition": {{
                "score": {{
                    "<Month>": <predicted_score>,
                    "<Month>": <predicted_score>,
                    ...
                }},
                "trends_and_insights": [
                    "...",
                    "...",
                    "..."
                ],
                "ai_health_plan": [
                    {{"increase_fiber_intake": ""}},
                    {{"stay_hydrated": ""}},
                    {{"balance_meals": ""}}
                ],
                "benchmark": ""
            }}
        }}

        CRITICAL REQUIREMENTS:
        - No explanatory text.
        - NO ```json``` formatting or code blocks
        - NO conversation or thoughts        
        """
        output = report_analysis_model.invoke(prompt)
        return output.content




last_month_dna_report_upload = ""
dna_data_analysis = []

last_month_urine_report_upload = "march"
urine_data_analysis = [
{
 "age": 42,
 "sex": "male",
 "height_centimeters": 168,
 "weight_kilograms": 72,
 "body_mass_index": 25.5,
 "conditions": ["diabetes"]
},
{
    "tests": {
      "Hematology (Blood Health)": [
        {
          "name": "Hemoglobin",
          "value": "14.5 g/dL",
          "status": "Normal",
          "range": {
            "low_normal": "13.0",
            "high_normal": "16.5",
            "unit": "g/dL"
          },
          "analysis": [
            "Hemoglobin level is within the normal range.",
            "No immediate indication of anemia.",
            "Maintains adequate oxygen-carrying capacity.",
            "Consistent with healthy red blood cell concentration.",
            "Stable hemoglobin level indicates good overall blood health."
          ],
          "recommendations": [
            "Continue current diet and lifestyle to maintain hemoglobin levels.",
            "Stay hydrated to support optimal blood function.",
            "Include iron-rich foods in diet to support hemoglobin production.",
            "Monitor hemoglobin levels during annual health check-ups.",
            "Consult with a healthcare professional if symptoms of anemia arise."
          ]
        },
        {
          "name": "RBC Count",
          "value": "4.79 million/amm",
          "status": "Normal",
          "range": {
            "low_normal": "4.5",
            "high_normal": "5.5",
            "unit": "million/amm"
          },
          "analysis": [
            "RBC count is within the normal range.",
            "Indicates adequate production of red blood cells.",
            "No signs of erythrocytosis or anemia.",
            "Supports effective oxygen transport in body.",
            "Reflects healthy bone marrow function."
          ],
          "recommendations": [
            "Maintain balanced diet rich in vitamins and iron.",
            "Stay active to promote healthy circulation.",
            "Avoid smoking as it can affect RBC count.",
            "Stay hydrated to ensure adequate blood volume.",
            "Have regular blood tests to monitor RBC count."
          ]
        },
        {
          "name": "Hematocrit",
          "value": "43.3 %",
          "status": "Normal",
          "range": {
            "low_normal": "40",
            "high_normal": "49",
            "unit": "%"
          },
          "analysis": [
            "Hematocrit value is within the normal range.",
            "Indicates correct proportion of red blood cells.",
            "No signs of polycythemia or dehydration.",
            "Reflects balanced blood viscosity.",
            "Supports optimal oxygen delivery to tissues."
          ],
          "recommendations": [
            "Ensure adequate fluid intake daily.",
            "Include iron and vitamin B12 in diet to support red cell production.",
            "Engage in regular physical exercise.",
            "Avoid excessive alcohol consumption as it can affect hematocrit levels.",
            "Monitor hematocrit level annually to assess health changes."
          ]
        }
      ]
    },
    "score_data": {
      "file_type": "blood",
      "score": 56.9
    }
}
]

last_month_blood_report_upload = "november"
blood_data_analysis = [
{
 "age": 42,
 "sex": "male",
 "height_centimeters": 168,
 "weight_kilograms": 72,
 "body_mass_index": 25.5,
 "conditions": ["diabetes"]
},
{
    "tests": {
      "Hematology (Blood Health)": [
        {
          "name": "Hemoglobin",
          "value": "14.5 g/dL",
          "status": "Normal",
          "range": {
            "low_normal": "13.0",
            "high_normal": "16.5",
            "unit": "g/dL"
          },
          "analysis": [
            "Hemoglobin level is within the normal range.",
            "No immediate indication of anemia.",
            "Maintains adequate oxygen-carrying capacity.",
            "Consistent with healthy red blood cell concentration.",
            "Stable hemoglobin level indicates good overall blood health."
          ],
          "recommendations": [
            "Continue current diet and lifestyle to maintain hemoglobin levels.",
            "Stay hydrated to support optimal blood function.",
            "Include iron-rich foods in diet to support hemoglobin production.",
            "Monitor hemoglobin levels during annual health check-ups.",
            "Consult with a healthcare professional if symptoms of anemia arise."
          ]
        },
        {
          "name": "RBC Count",
          "value": "4.79 million/amm",
          "status": "Normal",
          "range": {
            "low_normal": "4.5",
            "high_normal": "5.5",
            "unit": "million/amm"
          },
          "analysis": [
            "RBC count is within the normal range.",
            "Indicates adequate production of red blood cells.",
            "No signs of erythrocytosis or anemia.",
            "Supports effective oxygen transport in body.",
            "Reflects healthy bone marrow function."
          ],
          "recommendations": [
            "Maintain balanced diet rich in vitamins and iron.",
            "Stay active to promote healthy circulation.",
            "Avoid smoking as it can affect RBC count.",
            "Stay hydrated to ensure adequate blood volume.",
            "Have regular blood tests to monitor RBC count."
          ]
        },
        {
          "name": "Hematocrit",
          "value": "43.3 %",
          "status": "Normal",
          "range": {
            "low_normal": "40",
            "high_normal": "49",
            "unit": "%"
          },
          "analysis": [
            "Hematocrit value is within the normal range.",
            "Indicates correct proportion of red blood cells.",
            "No signs of polycythemia or dehydration.",
            "Reflects balanced blood viscosity.",
            "Supports optimal oxygen delivery to tissues."
          ],
          "recommendations": [
            "Ensure adequate fluid intake daily.",
            "Include iron and vitamin B12 in diet to support red cell production.",
            "Engage in regular physical exercise.",
            "Avoid excessive alcohol consumption as it can affect hematocrit levels.",
            "Monitor hematocrit level annually to assess health changes."
          ]
        }
      ]
    },
    "score_data": {
      "file_type": "blood",
      "score": 56.9
    }
},
{
  "tests": {
    "Hematology (Blood Health)": [
      {
        "name": "Hemoglobin",
        "value": "15.6 g/dL",
        "status": "Normal",
        "range": {
          "low_normal": "13.0",
          "high_normal": "16.5",
          "unit": "g/dL"
        },
        "analysis": [
          "Hemoglobin level is in the optimal upper-normal range.",
          "Indicates excellent oxygen-carrying capacity.",
          "No signs of anemia or blood loss.",
          "Reflects strong red blood cell health and production.",
          "Suggests good iron and vitamin status."
        ],
        "recommendations": [
          "Maintain current healthy diet rich in iron and proteins.",
          "Continue hydration and regular exercise.",
          "Schedule annual blood tests for ongoing monitoring.",
          "Avoid smoking to preserve hemoglobin quality.",
          "Maintain balanced intake of folate and vitamin B12."
        ]
      },
      {
        "name": "RBC Count",
        "value": "5.1 million/amm",
        "status": "Normal",
        "range": {
          "low_normal": "4.5",
          "high_normal": "5.5",
          "unit": "million/amm"
        },
        "analysis": [
          "RBC count is healthy and slightly improved from previous test.",
          "Shows robust red blood cell production.",
          "Indicates effective oxygen delivery and transport.",
          "No sign of anemia or polycythemia.",
          "Reflects efficient bone marrow activity."
        ],
        "recommendations": [
          "Maintain diet with adequate iron and vitamin C.",
          "Engage in regular moderate exercise.",
          "Stay hydrated to support optimal blood viscosity.",
          "Continue to avoid smoking and alcohol abuse.",
          "Monitor annually for consistent trends."
        ]
      },
      {
        "name": "Hematocrit",
        "value": "45.2 %",
        "status": "Normal",
        "range": {
          "low_normal": "40",
          "high_normal": "49",
          "unit": "%"
        },
        "analysis": [
          "Hematocrit value indicates healthy red blood cell proportion.",
          "Slightly improved oxygen-carrying efficiency.",
          "No evidence of dehydration or blood thickening.",
          "Reflects strong cardiovascular and metabolic balance.",
          "Indicates stable blood formation."
        ],
        "recommendations": [
          "Keep fluid intake steady throughout the day.",
          "Include iron and B vitamins for continued blood health.",
          "Exercise regularly to maintain circulation.",
          "Limit alcohol and caffeine intake.",
          "Review annually during health check-ups."
        ]
      }
    ]
  },
  "score_data": {
    "file_type": "blood",
    "score": 69.1
  }
}
]



obj = Plain_with_dashboard_data()                                                                                                                                                                                                                                                                                                                                                                        
output = obj.dashboard(blood_data_analysis, urine_data_analysis, dna_data_analysis, last_month_blood_report_upload, last_month_urine_report_upload, last_month_dna_report_upload)
print(output)



