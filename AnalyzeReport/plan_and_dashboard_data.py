import sys
from pathlib import Path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))


from Models.models import report_analysis_model
from AnalyzeReport.prompt import Prompts

class Plain_with_dashboard_data:

    def dashboard(self, blood_data_analysis, urine_data_analysis, dna_data_analysis, last_month_blood_report_upload, last_month_urine_report_upload, last_month_dna_report_upload):

        prompt = Prompts.health_status_prompt.format(blood_data_analysis=blood_data_analysis, last_month_blood_report_upload=last_month_blood_report_upload, urine_data_analysis=urine_data_analysis, last_month_urine_report_upload=last_month_urine_report_upload, dna_data_analysis=dna_data_analysis, last_month_dna_report_upload=last_month_dna_report_upload)
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




# blood_analysis = [
# {
#  "age": 42,
#  "sex": "male",
#  "height_centimeters": 168,
#  "weight_kilograms": 72,
#  "body_mass_index": 25.5,
#  "conditions": ["diabetes"]
# },
# {
#     "tests": {
#       "Hematology (Blood Health)": [
#         {
#           "name": "Hemoglobin",
#           "value": "14.5 g/dL",
#           "status": "Normal",
#           "range": {
#             "low_normal": "13.0",
#             "high_normal": "16.5",
#             "unit": "g/dL"
#           },
#           "analysis": [
#             "Hemoglobin level is within the normal range.",
#             "No immediate indication of anemia.",
#             "Maintains adequate oxygen-carrying capacity.",
#             "Consistent with healthy red blood cell concentration.",
#             "Stable hemoglobin level indicates good overall blood health."
#           ],
#           "recommendations": [
#             "Continue current diet and lifestyle to maintain hemoglobin levels.",
#             "Stay hydrated to support optimal blood function.",
#             "Include iron-rich foods in diet to support hemoglobin production.",
#             "Monitor hemoglobin levels during annual health check-ups.",
#             "Consult with a healthcare professional if symptoms of anemia arise."
#           ]
#         },
#         {
#           "name": "RBC Count",
#           "value": "4.79 million/amm",
#           "status": "Normal",
#           "range": {
#             "low_normal": "4.5",
#             "high_normal": "5.5",
#             "unit": "million/amm"
#           },
#           "analysis": [
#             "RBC count is within the normal range.",
#             "Indicates adequate production of red blood cells.",
#             "No signs of erythrocytosis or anemia.",
#             "Supports effective oxygen transport in body.",
#             "Reflects healthy bone marrow function."
#           ],
#           "recommendations": [
#             "Maintain balanced diet rich in vitamins and iron.",
#             "Stay active to promote healthy circulation.",
#             "Avoid smoking as it can affect RBC count.",
#             "Stay hydrated to ensure adequate blood volume.",
#             "Have regular blood tests to monitor RBC count."
#           ]
#         },
#         {
#           "name": "Hematocrit",
#           "value": "43.3 %",
#           "status": "Normal",
#           "range": {
#             "low_normal": "40",
#             "high_normal": "49",
#             "unit": "%"
#           },
#           "analysis": [
#             "Hematocrit value is within the normal range.",
#             "Indicates correct proportion of red blood cells.",
#             "No signs of polycythemia or dehydration.",
#             "Reflects balanced blood viscosity.",
#             "Supports optimal oxygen delivery to tissues."
#           ],
#           "recommendations": [
#             "Ensure adequate fluid intake daily.",
#             "Include iron and vitamin B12 in diet to support red cell production.",
#             "Engage in regular physical exercise.",
#             "Avoid excessive alcohol consumption as it can affect hematocrit levels.",
#             "Monitor hematocrit level annually to assess health changes."
#           ]
#         },
#         {
#           "name": "MCV",
#           "value": "90.3 fL",
#           "status": "Normal",
#           "range": {
#             "low_normal": "83",
#             "high_normal": "101",
#             "unit": "fL"
#           },
#           "analysis": [
#             "MCV is within the normal range.",
#             "Supports diagnosis of normocytic red blood cells.",
#             "Consistent with balanced red blood cell size and function.",
#             "No indication of macrocytosis or microcytosis.",
#             "Reflects stable red blood cell production and lifespan."
#           ],
#           "recommendations": [
#             "Include vitamin B12 and folate in diet to support red blood cell health.",
#             "Maintain hydration to support red blood cell volume.",
#             "Avoid alcohol which can adversely affect MCV over time.",
#             "Regular check-ups to monitor MCV and other blood parameters.",
#             "Consult healthcare provider if MCV values shift unexpectedly."
#           ]
#         },
#         {
#           "name": "MCH",
#           "value": "30.2 pg",
#           "status": "Normal",
#           "range": {
#             "low_normal": "27.1",
#             "high_normal": "32.5",
#             "unit": "pg"
#           },
#           "analysis": [
#             "MCH value is within the normal range.",
#             "Indicates correct hemoglobin content per red blood cell.",
#             "No signs of hyperchromia or hypochromia.",
#             "Supports normal red blood cell production.",
#             "Reflects effective hemoglobin synthesis."
#           ],
#           "recommendations": [
#             "Consume a diet rich in iron and proteins.",
#             "Maintain a healthy lifestyle free from smoking.",
#             "Regular blood tests to monitor hemoglobin and MCH.",
#             "Consult a doctor if there are signs of anemia.",
#             "Keep a record of lab results for historical trends."
#           ]
#         },
#         {
#           "name": "MCHC",
#           "value": "33.4 g/dL",
#           "status": "Normal",
#           "range": {
#             "low_normal": "32.5",
#             "high_normal": "36.7",
#             "unit": "g/dL"
#           },
#           "analysis": [
#             "MCHC is within the normal range.",
#             "Indicates stable hemoglobin concentration in red blood cells.",
#             "Reflects consistent red blood cell function.",
#             "No signs of spherocytosis or other cell membrane issues.",
#             "Supports effective oxygen transport capacity."
#           ],
#           "recommendations": [
#             "Continue a balanced diet to maintain all blood indices.",
#             "Regular exercise to promote optimal blood flow.",
#             "Follow up with specific medical advice if changes occur.",
#             "Avoid excessive dietary iron supplements without consultation.",
#             "Monitor overall health status with regular check-ups."
#           ]
#         },
#         {
#           "name": "RDW CV",
#           "value": "13.60 %",
#           "status": "Normal",
#           "range": {
#             "low_normal": "11.6",
#             "high_normal": "14",
#             "unit": "%"
#           },
#           "analysis": [
#             "RDW value is within the normal range.",
#             "Indicates uniformity of red blood cell size.",
#             "No signs of anisocytosis or size variation.",
#             "Reflects stable and homogenous erythropoiesis.",
#             "Supports diagnosis of normocytic normochromic condition."
#           ],
#           "recommendations": [
#             "Regular monitoring of RDW levels in routine check-ups.",
#             "Consultation with physician if symptoms like fatigue arise.",
#             "Maintain a nutrient-rich diet for optimal cell function.",
#             "Avoid excessive alcohol to preserve blood health.",
#             "Monitor for signs of inflammation which could affect RDW."
#           ]
#         },
#         {
#           "name": "WBC Count",
#           "value": "10570 /cmm",
#           "status": "High",
#           "range": {
#             "low_normal": "4000",
#             "high_normal": "10000",
#             "unit": "/cmm"
#           },
#           "analysis": [
#             "WBC count is slightly above normal range.",
#             "May indicate a response to infection or stress.",
#             "Necessary to monitor for changes or trends in WBC levels.",
#             "Increases can be due to inflammation or allergies.",
#             "Further investigation may be needed to understand elevation."
#           ],
#           "recommendations": [
#             "Follow up on current health symptoms and conditions.",
#             "Consider additional diagnostic tests if infection is suspected.",
#             "Consult healthcare provider for assessment and advice.",
#             "Monitor WBC levels with subsequent blood tests.",
#             "Adopt stress-reduction techniques to support immune function."
#           ]
#         },
#         {
#           "name": "Neutrophils",
#           "value": "73 %",
#           "status": "Normal",
#           "range": {
#             "low_normal": "40",
#             "high_normal": "80",
#             "unit": "%"
#           },
#           "analysis": [
#             "Neutrophil percentage is within the normal range.",
#             "Indicates effective immune response capability.",
#             "No signs of neutropenia or neutrophilia.",
#             "Suggests normal bone marrow function and maturation.",
#             "Reflects balanced leukocyte differential."
#           ],
#           "recommendations": [
#             "Maintain regular health check-ups to monitor immune health.",
#             "Consult with a healthcare provider if infections persist.",
#             "Ensure a vitamin-enriched diet to support immune cells.",
#             "Practice hygiene to reduce risk of infection.",
#             "Consider vaccines for preventable diseases."
#           ]
#         },
#         {
#           "name": "Lymphocytes",
#           "value": "19 %",
#           "status": "Normal",
#           "range": {
#             "low_normal": "20",
#             "high_normal": "40",
#             "unit": "%"
#           },
#           "analysis": [
#             "Lymphocyte percentage is slightly below range.",
#             "May indicate a transient physiological condition.",
#             "Does not suggest lymphocytopenia or immune deficiency.",
#             "Normal variations can occur with stress or infection.",
#             "Supports immune surveillance and response."
#           ],
#           "recommendations": [
#             "Monitor lymphocyte percentage over time.",
#             "Reduce stress and improve sleep to support immune function.",
#             "Discuss persistent changes with healthcare provider.",
#             "Consider immune support supplements if advised.",
#             "Balance physical activity for optimal immune strength."
#           ]
#         },
#         {
#           "name": "Eosinophils",
#           "value": "2 %",
#           "status": "Normal",
#           "range": {
#             "low_normal": "1",
#             "high_normal": "6",
#             "unit": "%"
#           },
#           "analysis": [
#             "Eosinophil percentage is within normal limits.",
#             "No signs of eosinophilia relate to allergies or parasitic infections.",
#             "Indicates balanced response to allergens and pathogens.",
#             "Reflects effective regulatory immune function.",
#             "Consistent with stable inflammatory and allergy response."
#           ],
#           "recommendations": [
#             "Maintain a balanced diet to support general health.",
#             "Monitor for symptoms of allergies or asthma.",
#             "Discuss persistent issues with an allergist or healthcare provider.",
#             "Track seasonal changes and their impact on health.",
#             "Consider allergy testing if symptoms persist."
#           ]
#         },
#         {
#           "name": "Monocytes",
#           "value": "6 %",
#           "status": "Normal",
#           "range": {
#             "low_normal": "2",
#             "high_normal": "10",
#             "unit": "%"
#           },
#           "analysis": [
#             "Monocyte percentage is within normal range.",
#             "Indicates proficient phagocytic and adaptive immune functions.",
#             "Reflects normal turnover of monocytes into tissue macrophages.",
#             "No indication of monocytosis or inflammatory disease.",
#             "Balances innate immune defense mechanisms."
#           ],
#           "recommendations": [
#             "Engage in regular physical activity to support immune health.",
#             "Monitor for any signs of infection or inflammation.",
#             "Maintain a healthy diet to support monocyte function.",
#             "Stay informed about vaccines to prevent infections.",
#             "Track changes in symptoms or health status over time."
#           ]
#         },
#         {
#           "name": "Basophils",
#           "value": "0 %",
#           "status": "Normal",
#           "range": {
#             "low_normal": "0",
#             "high_normal": "2",
#             "unit": "%"
#           },
#           "analysis": [
#             "Basophil count is within the expected normal range.",
#             "Supports the diagnosis of balanced eosinophil-related conditions.",
#             "Reflects stability in allergic or inflammatory response.",
#             "No signs of basophilia associated with disorders.",
#             "Stable basophil levels reflect normal tissue homeostasis."
#           ],
#           "recommendations": [
#             "Continue monitoring for allergy or hypersensitivity symptoms.",
#             "Investigate further if significant health episodes arise.",
#             "Consult with healthcare providers about persistent allergic reactions.",
#             "Maintain a diet with low allergenic potential if necessary.",
#             "Consider lifestyle changes to minimize exposure to allergens."
#           ]
#         },
#         {
#           "name": "Platelet Count",
#           "value": "150000 /cmm",
#           "status": "Normal",
#           "range": {
#             "low_normal": "150000",
#             "high_normal": "410000",
#             "unit": "/cmm"
#           },
#           "analysis": [
#             "Platelet count is at the lower threshold of normal range.",
#             "Stable platelet production and destruction rates.",
#             "No indication of thrombocytopenia or thrombocytosis.",
#             "Supports adequate clotting function during injury.",
#             "Reflects functional bone marrow activity."
#           ],
#           "recommendations": [
#             "Have regular blood check-ups to monitor platelet count.",
#             "Avoid unnecessary use of medications affecting platelets.",
#             "Ensure a diet supportive of bone marrow function.",
#             "Evaluate bleeding risks with healthcare professional if necessary.",
#             "Monitor for symptoms like bruising or extended bleeding times."
#           ]
#         }
#       ]
#     },
#     "score_data": {
#       "file_type": "blood",
#       "score": 56.9
#     }
# },
# {
#   "tests": {
#     "Hematology (Blood Health)": [
#       {
#         "name": "Hemoglobin",
#         "value": "15.6 g/dL",
#         "status": "Normal",
#         "range": {
#           "low_normal": "13.0",
#           "high_normal": "16.5",
#           "unit": "g/dL"
#         },
#         "analysis": [
#           "Hemoglobin level is in the optimal upper-normal range.",
#           "Indicates excellent oxygen-carrying capacity.",
#           "No signs of anemia or blood loss.",
#           "Reflects strong red blood cell health and production.",
#           "Suggests good iron and vitamin status."
#         ],
#         "recommendations": [
#           "Maintain current healthy diet rich in iron and proteins.",
#           "Continue hydration and regular exercise.",
#           "Schedule annual blood tests for ongoing monitoring.",
#           "Avoid smoking to preserve hemoglobin quality.",
#           "Maintain balanced intake of folate and vitamin B12."
#         ]
#       },
#       {
#         "name": "RBC Count",
#         "value": "5.1 million/amm",
#         "status": "Normal",
#         "range": {
#           "low_normal": "4.5",
#           "high_normal": "5.5",
#           "unit": "million/amm"
#         },
#         "analysis": [
#           "RBC count is healthy and slightly improved from previous test.",
#           "Shows robust red blood cell production.",
#           "Indicates effective oxygen delivery and transport.",
#           "No sign of anemia or polycythemia.",
#           "Reflects efficient bone marrow activity."
#         ],
#         "recommendations": [
#           "Maintain diet with adequate iron and vitamin C.",
#           "Engage in regular moderate exercise.",
#           "Stay hydrated to support optimal blood viscosity.",
#           "Continue to avoid smoking and alcohol abuse.",
#           "Monitor annually for consistent trends."
#         ]
#       },
#       {
#         "name": "Hematocrit",
#         "value": "45.2 %",
#         "status": "Normal",
#         "range": {
#           "low_normal": "40",
#           "high_normal": "49",
#           "unit": "%"
#         },
#         "analysis": [
#           "Hematocrit value indicates healthy red blood cell proportion.",
#           "Slightly improved oxygen-carrying efficiency.",
#           "No evidence of dehydration or blood thickening.",
#           "Reflects strong cardiovascular and metabolic balance.",
#           "Indicates stable blood formation."
#         ],
#         "recommendations": [
#           "Keep fluid intake steady throughout the day.",
#           "Include iron and B vitamins for continued blood health.",
#           "Exercise regularly to maintain circulation.",
#           "Limit alcohol and caffeine intake.",
#           "Review annually during health check-ups."
#         ]
#       },
#       {
#         "name": "MCV",
#         "value": "91.2 fL",
#         "status": "Normal",
#         "range": {
#           "low_normal": "83",
#           "high_normal": "101",
#           "unit": "fL"
#         },
#         "analysis": [
#           "MCV remains in optimal range, showing normocytic red cells.",
#           "Indicates balanced size and shape of red blood cells.",
#           "No signs of B12 or folate deficiency.",
#           "Supports efficient oxygen delivery and exchange.",
#           "Stable over time, indicating consistent red cell health."
#         ],
#         "recommendations": [
#           "Continue nutrient-rich diet with leafy greens and proteins.",
#           "Stay hydrated for cell volume balance.",
#           "Avoid alcohol excess to maintain cell size stability.",
#           "Have routine health assessments yearly.",
#           "Monitor if fatigue or unusual symptoms occur."
#         ]
#       },
#       {
#         "name": "MCH",
#         "value": "31.0 pg",
#         "status": "Normal",
#         "range": {
#           "low_normal": "27.1",
#           "high_normal": "32.5",
#           "unit": "pg"
#         },
#         "analysis": [
#           "MCH is at optimal mid-upper range.",
#           "Shows healthy hemoglobin content per red cell.",
#           "No sign of hypochromia or anemia.",
#           "Indicates efficient hemoglobin synthesis and stability.",
#           "Supports ideal red blood cell coloration."
#         ],
#         "recommendations": [
#           "Include iron, folate, and B12 in meals.",
#           "Avoid nutritional deficiencies through balanced diet.",
#           "Keep record of results to observe trends.",
#           "Follow healthy sleep and stress routines.",
#           "Perform annual wellness screening."
#         ]
#       },
#       {
#         "name": "MCHC",
#         "value": "34.5 g/dL",
#         "status": "Normal",
#         "range": {
#           "low_normal": "32.5",
#           "high_normal": "36.7",
#           "unit": "g/dL"
#         },
#         "analysis": [
#           "MCHC indicates well-balanced hemoglobin concentration.",
#           "Optimal oxygen transport ability maintained.",
#           "No sign of red cell dehydration or hyperchromia.",
#           "Reflects stable red cell structure and membrane integrity.",
#           "Consistent with overall good blood health."
#         ],
#         "recommendations": [
#           "Keep up with nutrient-rich meals and proper hydration.",
#           "Avoid unnecessary iron supplements unless prescribed.",
#           "Continue exercise for proper blood circulation.",
#           "Reassess values annually for trend consistency.",
#           "Maintain moderate physical activity levels."
#         ]
#       },
#       {
#         "name": "RDW CV",
#         "value": "12.7 %",
#         "status": "Normal",
#         "range": {
#           "low_normal": "11.6",
#           "high_normal": "14",
#           "unit": "%"
#         },
#         "analysis": [
#           "RDW is slightly improved, showing excellent red cell uniformity.",
#           "No variability in red cell size or shape.",
#           "Stable erythropoiesis observed.",
#           "Indicates proper iron and vitamin balance.",
#           "Reflects consistent red blood cell regeneration."
#         ],
#         "recommendations": [
#           "Maintain a balanced diet rich in micronutrients.",
#           "Hydrate well to support blood consistency.",
#           "Avoid stress that can impact cellular health.",
#           "Continue annual CBC monitoring.",
#           "Consult healthcare provider if fatigue or weakness appears."
#         ]
#       },
#       {
#         "name": "WBC Count",
#         "value": "7800 /cmm",
#         "status": "Normal",
#         "range": {
#           "low_normal": "4000",
#           "high_normal": "10000",
#           "unit": "/cmm"
#         },
#         "analysis": [
#           "WBC count is perfectly within healthy range.",
#           "Shows balanced immune activity with no infection signs.",
#           "Indicates normal bone marrow response.",
#           "No stress or inflammation markers detected.",
#           "Reflects strong immune system health."
#         ],
#         "recommendations": [
#           "Maintain healthy sleep cycle and diet.",
#           "Include vitamin C and zinc to support immunity.",
#           "Manage stress through relaxation or mindfulness.",
#           "Stay physically active for immune balance.",
#           "Continue monitoring WBC in regular check-ups."
#         ]
#       },
#       {
#         "name": "Neutrophils",
#         "value": "68 %",
#         "status": "Normal",
#         "range": {
#           "low_normal": "40",
#           "high_normal": "80",
#           "unit": "%"
#         },
#         "analysis": [
#           "Neutrophil level is optimal and balanced.",
#           "Indicates readiness to fight infections efficiently.",
#           "No inflammation or abnormal increase noted.",
#           "Reflects healthy bone marrow and immune defense.",
#           "Supports a stable immune equilibrium."
#         ],
#         "recommendations": [
#           "Continue maintaining healthy habits.",
#           "Avoid overuse of antibiotics.",
#           "Prioritize rest during illness recovery.",
#           "Practice hygiene and immune support through nutrition.",
#           "Monitor levels during annual assessments."
#         ]
#       },
#       {
#         "name": "Lymphocytes",
#         "value": "26 %",
#         "status": "Normal",
#         "range": {
#           "low_normal": "20",
#           "high_normal": "40",
#           "unit": "%"
#         },
#         "analysis": [
#           "Lymphocyte percentage is well within normal range.",
#           "Shows balanced adaptive immune response.",
#           "No immune suppression or overactivity detected.",
#           "Indicates improved immune system balance.",
#           "Supports overall resistance to infections."
#         ],
#         "recommendations": [
#           "Maintain balanced diet with antioxidants.",
#           "Continue moderate exercise to boost immunity.",
#           "Manage stress and get adequate sleep.",
#           "Hydrate properly for cellular function.",
#           "Regularly monitor immune-related parameters."
#         ]
#       },
#       {
#         "name": "Eosinophils",
#         "value": "3 %",
#         "status": "Normal",
#         "range": {
#           "low_normal": "1",
#           "high_normal": "6",
#           "unit": "%"
#         },
#         "analysis": [
#           "Eosinophil percentage remains within ideal range.",
#           "No signs of allergies or parasitic activity.",
#           "Indicates stable and balanced immune modulation.",
#           "Reflects reduced inflammation compared to previous results.",
#           "Supports overall respiratory and skin health."
#         ],
#         "recommendations": [
#           "Continue tracking allergy triggers if any.",
#           "Avoid unnecessary exposure to dust and allergens.",
#           "Maintain anti-inflammatory diet with omega-3s.",
#           "Consult doctor if persistent allergic symptoms appear.",
#           "Ensure adequate sleep and hydration."
#         ]
#       },
#       {
#         "name": "Monocytes",
#         "value": "5 %",
#         "status": "Normal",
#         "range": {
#           "low_normal": "2",
#           "high_normal": "10",
#           "unit": "%"
#         },
#         "analysis": [
#           "Monocyte level shows excellent immune balance.",
#           "No signs of chronic inflammation or infection.",
#           "Reflects effective cleanup of damaged cells and debris.",
#           "Consistent with healthy immune regulation.",
#           "Shows efficient innate immune activity."
#         ],
#         "recommendations": [
#           "Continue healthy, active lifestyle.",
#           "Monitor inflammation markers during annual exams.",
#           "Maintain balanced intake of vitamins and minerals.",
#           "Manage stress and avoid excessive processed foods.",
#           "Stay updated on vaccinations."
#         ]
#       },
#       {
#         "name": "Basophils",
#         "value": "1 %",
#         "status": "Normal",
#         "range": {
#           "low_normal": "0",
#           "high_normal": "2",
#           "unit": "%"
#         },
#         "analysis": [
#           "Basophil count indicates normal allergic response regulation.",
#           "Reflects stability in histamine and inflammation control.",
#           "No hypersensitivity reaction detected.",
#           "Supports overall immune equilibrium.",
#           "Consistent with good immune tolerance."
#         ],
#         "recommendations": [
#           "Continue to maintain allergy-free environment.",
#           "Follow seasonal precautions if allergy-prone.",
#           "Eat antioxidant-rich foods to support immune health.",
#           "Stay hydrated and avoid high-histamine foods if sensitive.",
#           "Schedule regular health assessments."
#         ]
#       },
#       {
#         "name": "Platelet Count",
#         "value": "265000 /cmm",
#         "status": "Normal",
#         "range": {
#           "low_normal": "150000",
#           "high_normal": "410000",
#           "unit": "/cmm"
#         },
#         "analysis": [
#           "Platelet count is comfortably within optimal range.",
#           "Indicates healthy clotting ability and bone marrow function.",
#           "No sign of bleeding or clotting disorder.",
#           "Reflects strong vascular and blood repair mechanisms.",
#           "Suggests overall improved blood production."
#         ],
#         "recommendations": [
#           "Maintain balanced nutrition for bone marrow health.",
#           "Avoid unnecessary medications affecting platelets.",
#           "Stay active and hydrated for circulatory balance.",
#           "Limit alcohol intake.",
#           "Include vitamin K-rich foods for clotting support."
#         ]
#       }
#     ]
#   },
#   "score_data": {
#     "file_type": "blood",
#     "score": 69.1
#   }
# }
# ]

