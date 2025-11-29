class Prompts:

    BLOOD_ANALYSIS_PROMPT = """
    Analyze the following medical report using the ReAct framework and return the output in a structured JSON format.
    Steps to follow (do not include steps or intermediate reasoning in the output):

    1. THINK: Identify key parameters (e.g., Hemoglobin, Glucose)
    2. CHECK: Compare values against standard medical ranges

    FORMAT: ALWAYS Return the final result in ONLY BELOW JSON structure:

    {{
    "age": "<age mentioned in the report or empty string>",
    "sex": "<sex mentioned in the report or empty string>",
    "tests": {{
        "Lipid Profile": [
            {{
            "name": "<LDL / HDL / Triglycerides / Total Cholesterol / ApoB / ApoA1 / Lipoprotein(a)>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "low_normal": "<value of low normal>",
            "high_normal": "<value of high normal>",
            "unit": "<unit mentioned with range>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Glucose & Diabetes": [
            {{
            "name": "<Fasting Glucose / HbA1c / Insulin / C-Peptide / HOMA-IR / Fructosamine>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "low_normal": "<value of low normal>",
            "high_normal": "<value of high normal>",
            "unit": "<unit mentioned with range>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Kidney Function": [
            {{
            "name": "<Creatinine / eGFR / BUN / Uric Acid / Cystatin C>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "low_normal": "<value of low normal>",
            "high_normal": "<value of high normal>",
            "unit": "<unit mentioned with range>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Liver Function": [
            {{
            "name": "<ALT / AST / GGT / Bilirubin / Albumin / Total Protein>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "low_normal": "<value of low normal>",
            "high_normal": "<value of high normal>",
            "unit": "<unit mentioned with range>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Inflammation & Immunity": [
            {{
            "name": "<CRP / hs-CRP / ESR / Ferritin / NLR / PLR / IL-6 / TNF-α>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "low_normal": "<value of low normal>",
            "high_normal": "<value of high normal>",
            "unit": "<unit mentioned with range>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Hematology (Blood Health)": [
            {{
            "name": "<Hemoglobin / Hematocrit / RBC Count / WBC Count / Platelets / MCV / MCH / MCHC / RDW / Neutrophils / Lymphocytes / Eosinophils / Monocytes / Basophils / MPV>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "low_normal": "<value of low normal>",
            "high_normal": "<value of high normal>",
            "unit": "<unit mentioned with range>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Vitamins & Minerals": [
            {{
            "name": "<Vitamin D / Vitamin B12 / Folate / Iron / Calcium>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "low_normal": "<value of low normal>",
            "high_normal": "<value of high normal>",
            "unit": "<unit mentioned with range>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Electrolyte Balance": [
            {{
            "name": "<Sodium / Potassium / Chloride / Magnesium / Bicarbonate (CO₂)>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "low_normal": "<value of low normal>",
            "high_normal": "<value of high normal>",
            "unit": "<unit mentioned with range>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Hormonal Health": [
            {{
            "name": "<TSH / Free T4 / Free T3 / Cortisol (AM) / DHEA-S / Prolactin>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "low_normal": "<value of low normal>",
            "high_normal": "<value of high normal>",
            "unit": "<unit mentioned with range>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Advanced Cardiovascular": [
            {{
            "name": "<Oxidized LDL / Troponin / BNP/NT-proBNP / Homocysteine / Chylomicrons / Sphingolipids>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>", 
            "range": {{
            "low_normal": "<value of low normal>",
            "high_normal": "<value of high normal>",
            "unit": "<unit mentioned with range>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ]
    }}
    }}

    Medical Report:
    {text}

    ### TEST PARAMETER IMPORTANT INSTRUCTIONS:
  - INCLUDE ALL test parameters found in the medical report, even if not explicitly listed in the names of the categories above. Map those test parameters from medical report to the most relevant existing category (e.g Vitamins & Minerals, Hematology (Blood Health), Glucose & Diabetes etc) based on medical function.
  - ENSURE that ALL the test parameters from the medical report are INCLUDED in the output.
  - ENSURE that all above requirements are completed.
    
    CRITICAL REQUIREMENTS:
          - NO explanatory text
          - NO ```json``` formatting or code blocks
          - NO conversation or thoughts
    """

    URINE_ANALYSIS_PROMPT = """
    Analyze the following medical report using the ReAct framework and return the output in a structured JSON format.
    Steps to follow (do not include steps or intermediate reasoning in the output):
    1. THINK: Identify key parameters (e.g Urobilinogen, color etc)
    2. CHECK: Compare values against standard medical ranges

    FORMAT: ALWAYS Return the final result in ONLY BELOW JSON structure:
    {{
    "age": "<age mentioned in the report or empty string>",
    "sex": "<sex mentioned in the report or empty string>",
    "tests": {{
        "Kidney Function": [
            {{
            "name": "<Protein / ACR / Albumin / Creatinine / Cystatin C>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "data": "<Standard reference range>",
            "unit": "<Unit of measurement if available, otherwise empty string>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Hydration & Electrolytes": [
            {{
            "name": "<Specific Gravity / Osmolality / Sodium / Potassium / Chloride>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "data": "<Standard reference range>",
            "unit": "<Unit of measurement if available, otherwise empty string>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Liver & Metabolism": [
            {{
            "name": "<Bilirubin / Urobilinogen / Ketones / Glucose>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "data": "<Standard reference range>",
            "unit": "<Unit of measurement if available, otherwise empty string>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Urinary Tract Health ": [
            {{
            "name": "<Leukocyte Esterase / Nitrites / Blood / pH>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "data": "<Standard reference range>",
            "unit": "<Unit of measurement if available, otherwise empty string>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Microscopic & Physical ": [
            {{
            "name": "<Color / Clarity / RBC / WBC / Epi Cells / Casts / Crystals / Bacteria/Yeast>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "data": "<Standard reference range>",
            "unit": "<Unit of measurement if available, otherwise empty string>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Advanced Biomarkers ": [
            {{
            "name": "<NGAL / KIM-1 / miRNAs>",
            "value": "<Measured Value + Unit>",
            "status": "<Normal / Low / High>",
            "range": {{
            "data": "<Standard reference range>",
            "unit": "<Unit of measurement if available, otherwise empty string>"
            }},
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ]
    }}
    
    }}

    Medical Report:
    {text}

    ### TEST PARAMETER IMPORTANT INSTRUCTIONS:
  - INCLUDE ALL test parameters found in the medical report, even if not explicitly listed in the names of the categories above. Map those test parameters from medical report to the most relevant existing category (e.g Kidney Function, Hydration & Electrolytes etc) based on medical function.
  - ENSURE that ALL the test parameters from the medical report are INCLUDED in the output.
  - ENSURE that all above requirements are completed.

    CRITICAL REQUIREMENTS:
          - NO explanatory text
          - NO ```json``` formatting or code blocks
          - NO conversation or thoughts
    """
    
    DNA_ANALYSIS_PROMPT = """
    Analyze the following medical report using the ReAct framework and return the output in a structured JSON format.
    Steps to follow (do not include steps or intermediate reasoning in the output):
    1. THINK: Identify key parameters (e.g., APOE, FTO)
    2. CHECK: Compare values against standard medical ranges

    FORMAT: ALWAYS Return the final result in ONLY BELOW JSON structure:

    {{
    "age": "<age mentioned in the report or empty string>",
    "sex": "<sex mentioned in the report or empty string>",
    "tests": {{
        "Disease Risk": [
            {{
            "name": "<APOE / TCF7L2 / LPA / LDLR>",
            "value": "<Measured Value / Genotype / Phenotype / empty string>", 
            "snp": "<key snp(s) or empty string>",    // If the report does not include specific SNP identifiers, set this to ""
            "status": "<Normal / Low / High or empty string>",
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Nutrition & Metabolism": [
            {{
            "name": "<MTHFR / FTO / TCF7L2 / C-MC4R / LCT / CYP1A2>",
            "value": "<Measured Value / Genotype / Phenotype / empty string>",    
            "snp": "<key snp(s) or empty string>",      // If the report does not include specific SNP identifiers, set this to ""
            "status": "<Normal / Low / High or empty string>",
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Detox & Inflammation": [
            {{
            "name": "<GSTM1 / GSTT1 / IL6 / CRP / NAT2>",
            "value": "<Measured Value / Genotype / Phenotype / Result or empty string>",
            "snp": "<key snp(s) or empty string>",
            "status": "<Normal / Low / High or empty string>",
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Fitness & Performance": [
            {{
            "name": "<ACTN3 / ADRB2 / ACE / NOS3>",
            "value": "<Measured Value / Genotype / Phenotype / Result or empty string>",
            "snp": "<key snp(s) or empty string>",
            "status": "<Normal / Low / High or empty string>",
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Mental Health & Behavior": [
            {{
            "name": "<COMT / BDNF / OXTR / MAOA>",
            "value": "<Measured Value / Genotype / Phenotype / Result or empty string>",
            "snp": "<key snp(s) or empty string>",
            "status": "<Normal / Low / High or empty string>",
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ],
        "Longevity & Aging": [
            {{
            "name": "<FOXO3 / SIRT1 / CDKN2A / TERT>",
            "value": "<Measured Value / Genotype / Phenotype / Result or empty string>",
            "snp": "<key snp(s) or empty string>",
            "status": "<Normal / Low / High or empty string>",
            "analysis": ["<Always provide at least 5 insights>"],
            "recommendations": ["<Always provide at least 5 recommendations>"]
            }}
            ]
    }}
    
    }}

    Medical Report:
    {text}

    ### TEST PARAMETER IMPORTANT INSTRUCTIONS:
  - INCLUDE ALL test parameters found in the medical report, even if not explicitly listed in the names of the categories above. Map those test parameters from medical report to the most relevant existing category (e.g Longevity & Aging, Nutrition & Metabolism etc) based on medical function.
  - ENSURE that ALL the test parameters from the medical report are INCLUDED in the output.
  - ENSURE that all above requirements are completed.

    CRITICAL REQUIREMENTS:
          - NO explanatory text
          - NO ```json``` formatting or code blocks
          - NO conversation or thoughts
    """


#     DNA_ANALYSIS_PROMPT = """
#     Analyze the following medical report using the ReAct framework and return the output in a structured JSON format.
#     Steps to follow (do not include steps or intermediate reasoning in the output):
#     1. THINK: Identify key parameters (e.g., APOE, FTO)
#     2. CHECK: Compare values against standard medical ranges

#     FORMAT: ALWAYS Return the final result in ONLY BELOW JSON structure:

#     {{
#     "tests": {{
#         "Disease Risk": [
#             {{
#             "name": "<APOE / TCF7L2 / LPA / LDLR>",
#             "value": "<Measured Value + Unit>",
#             "status": "<Normal / Low / High>",
#             "analysis": ["<Always provide at least 5 insights>"],
#             "recommendations": ["<Always provide at least 5 recommendations>"]
#             }}
#             ],
#         "Nutrition & Metabolism": [
#             {{
#             "name": "<MTHFR / FTO / TCF7L2 / C-MC4R / LCT / CYP1A2>",
#             "value": "<Measured Value + Unit>",
#             "status": "<Normal / Low / High>",
#             "analysis": ["<Always provide at least 5 insights>"],
#             "recommendations": ["<Always provide at least 5 recommendations>"]
#             }}
#             ],
#         "Detox & Inflammation": [
#             {{
#             "name": "<GSTM1 / GSTT1 / IL6 / CRP / NAT2>",
#             "value": "<Measured Value + Unit>",
#             "status": "<Normal / Low / High>",
#             "analysis": ["<Always provide at least 5 insights>"],
#             "recommendations": ["<Always provide at least 5 recommendations>"]
#             }}
#             ],
#         "Fitness & Performance": [
#             {{
#             "name": "<ACTN3 / ADRB2 / ACE / NOS3>",
#             "value": "<Measured Value + Unit>",
#             "status": "<Normal / Low / High>",
#             "analysis": ["<Always provide at least 5 insights>"],
#             "recommendations": ["<Always provide at least 5 recommendations>"]
#             }}
#             ],
#         "Mental Health & Behavior": [
#             {{
#             "name": "<COMT / BDNF / OXTR / MAOA>",
#             "value": "<Measured Value + Unit>",
#             "status": "<Normal / Low / High>",
#             "analysis": ["<Always provide at least 5 insights>"],
#             "recommendations": ["<Always provide at least 5 recommendations>"]
#             }}
#             ],
#         "Longevity & Aging": [
#             {{
#             "name": "<FOXO3 / SIRT1 / CDKN2A / TERT>",
#             "value": "<Measured Value + Unit>",
#             "status": "<Normal / Low / High>",
#             "analysis": ["<Always provide at least 5 insights>"],
#             "recommendations": ["<Always provide at least 5 recommendations>"]
#             }}
#             ]
#     }}
    
#     }}

#     Medical Report:
#     {text}

#     ### TEST PARAMETER IMPORTANT INSTRUCTIONS:
#   - INCLUDE ALL test parameters found in the medical report, even if not explicitly listed in the names of the categories above. Map those test parameters from medical report to the most relevant existing category (e.g Longevity & Aging, Nutrition & Metabolism etc) based on medical function.
#   - ENSURE that ALL the test parameters from the medical report are INCLUDED in the output.
#   - ENSURE that all above requirements are completed.

#     CRITICAL REQUIREMENTS:
#           - NO explanatory text
#           - NO ```json``` formatting or code blocks
#           - NO conversation or thoughts
#     """

    DASHBOARD_DATA_PROMPT = """ 
      health_trends_and_insights:
      You are WiseHealth’s trusted AI health advisor. Based on the user's recent and past health data across relevant areas (e.g., blood, urine, DNA), generate 3 clear, concise health trend insights.

      Follow this structure:
        - Highlight a health marker or behavior that improved — use encouraging, factual language.
        - Note a metric or habit that remained stable or showed slight progress.
        - Identify a trend that declined or needs attention, and offer a gentle, supportive suggestion.

      Guidelines:
        - Each insight must be short, easy to scan, and personalized.
        - Avoid technical jargon and score values unless the percentage change adds value.
        - Maintain a neutral-supportive tone: never alarming, always actionable.
        - Insights must reflect trends (change over time), not just single measurements.

      Ouput Structure: 
        - 
        - The AI's response should be a JSON object that contains one keys: "insights", "name".
        - "name" is a string
        - "insights" is a list (like a bullet-point list).

        Inside this list, there are three short messages (strings):
          - The first message highlights something positive — a health marker or habit that has improved.
          - The second message notes something that has remained stable or shown slight improvement.
          - The third message highlights a declining or concerning trend and gives a gentle suggestion for what the user could do about it.


      ai_health_plan:
      You are the WiseHealth AI lifestyle expert. Given a user's full health profile—including (e.g., blood, urine, DNA) the top 3 personalized lifestyle recommendations (max 20 words each). Each must have a clear label (e.g., "diet_tip", "exercise_tip","sleep_recovery_tip") and follow these rules:
      - Use a cross-domain perspective based on recent data and health goals.
      - Never diagnose or mention rare conditions.
      - Ensure each bullet is supportive, trend-aware, and emotionally intelligent.
      Avoid repetition across bullets.            

      bach_mark:    
      You are WiseHealth’s intelligent health advisor. Based on user-specific data for a selected health domain (e.g., blood, urine, DNA), generate a single, emotionally safe, 1-line benchmark sentence. The sentence should:
      - Use comparative, percentile-based, or trend-based language (e.g., “top 25% of users your age”)
      - Encourage progress and reinforce motivation
      - Match WiseHealth’s tone: expert, friendly, and data-smart
      - Avoid judgmental or alarming language



      Provide the output in Json format:
      {{ 
      "health_trends_and_insights":{{
        "key": "", // blood, urine, DNA
        "insights": []
        }},
        "ai_health_plan": [
          {{
            "diet_tip": "Add more omega-3s to meals to support inflammation and brain health."
          }},
          {{
            "exercise_tip": "Incorporate 20 minutes of moderate cardio 3x/week to boost metabolic fitness."
          }},
          {{
            "sleep_recovery_tip": "Prioritize 7–9 hours of sleep nightly with a consistent bedtime routine."
          }}
        ],                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        "bach_mark" : {{
        key_name : "", //blood, urine, DNA
        "banchmark":"", 
      }}
      }}
      
      Report: {Report}
      

      CRITICAL REQUIREMENTS:
              - NO explanatory text
              - NO ```json``` formatting or code blocks
              - NO conversation or thoughts
    """ 

    predict_prompt = """
    You are a medical AI assistant.

    Below is a list of medical reports in chronological order:
    - The first report is the oldest.
    - The last report is the most recent.
    Each report contains:
    - "score_data" → "score" (health score of that specific report)
    - "tests" with parameters, their values, status, analysis, and recommendations.

    Your task:
    1. Extract all scores in order.
    2. For each parameter across reports (e.g., Protein, Creatinine, Specific Gravity, etc.):
    - Determine if the status is improving or worsening.
    3. Combine the parameter trend analysis with the score trend:
    - If both score and parameters are improving, predict a higher score.
    - If score is improving but some key parameters worsen, predict a smaller increase or stable score.
    - If score is decreasing and parameters worsen, predict a lower score.
    - If scores fluctuate, use the last two changes plus the latest parameter trends to decide.
    4. Keep prediction within a realistic range and never outside 0–100.
    5. Do NOT explain reasoning. Do NOT output any text other than the JSON object.

    List of Medical Reports:
    {Reports}

    ALWAYS give the response in EXACT BELOW format:

    {{
        "health_score": {{
        "score": <predicted_score>
        }}
    }}

    CRITICAL REQUIREMENTS:
        - NO explanatory text
        - NO ```json``` formatting or code blocks
        - NO conversation or thoughts

    """


    blood_box_related_prompt = """
        You are WiseHealth's comprehensive health AI assistant with three key responsibilities:
        1. As a lab expert, briefly summarize the most relevant result from the user's latest blood panel with one evidence-based tip
        2. As a metabolic specialist, identify which health subdomain (e.g., glucose, inflammation, lipids) needs most attention with one practical improvement step
        3. As a trend advisor, info rm if markers are stable, improving or reducing, encourage consistency, and confirm when retesting is recommended

        Important Data Handling Instructions:
        - The 'blood_reports_data' is an **ordered list of blood reports from oldest to newest**.
        - For tasks that require only the **latest test**, analyze the **last report** in 'blood_reports_data'.
        - For tasks that require tracking **progress or trends**, analyze **all reports** in 'blood_reports_data'.

        Provide your complete response in this JSON format:
        {{
        "last_test_result_summary": "",
        "most_impacted_area": "",
        "keep_monitoring_progress": ""
        }}
        
        Blood Reports Data which is in time order:
        {blood_reports_data}

        CRITICAL REQUIREMENTS:
        - NO explanatory text
        - NO ```json``` formatting or code blocks
        - NO conversation or thoughts                                 
    """

    urine_box_related_prompt = """
        You are WiseHealth's AI health advisor specializing in hydration, urinary health, and electrolyte balance Below is 'urine_reports_data' on the basis of which you have to perform below.
        - For hydration assessments: If the user's hydration trend is below optimal, gently inform them and suggest simple improvements (e.g., spacing water intake, reducing caffeine). If their hydration is optimal or improving, provide positive reinforcement and encourage maintaining current habits for long-term health benefits.     
        - For urinary protein detection: If trace protein is found, calmly explain it may reflect stress, exertion, or a transient factor. Recommend hydration and retesting if persistent. If protein levels are higher than normal, explain that it may indicate kidney stress or damage and advise consulting a healthcare provider. Encourage staying well-hydrated and monitoring for additional symptoms. 
        - For sodium level assessments: If sodium is slightly elevated, suggest reducing salty foods and drinking more water consistently. If sodium is slightly low, recommend incorporating moderate amounts of healthy salt sources or electrolyte-rich foods and fluids. Reassure the user that managing these levels is achievable through mindful dietary adjustments and habit changes. 

        provide the Output in Json Form:
        {{
          Hydration Alert : "",
          Protein Detected : "",
          Sodium Level : ""
        }}

        Urine Report Data:
        {urine_reports_data}

        CRITICAL REQUIREMENTS:
          - NO explanatory text
          - NO ```json``` formatting or code blocks
          - NO conversation or thoughts 
    """

    dna_box_related_prompt = """
        You are WiseHealth's AI genetics advisor specializing in DNA-based wellness insights. Below is DNA Report Data on the basis of which you have to perform below.

        - For Genetic Risk Alert: Analyze if the user's genetic risk is low, normal, or elevated.  
        • If elevated — explain calmly that their DNA suggests a higher predisposition to certain health issues and recommend lifestyle steps such as exercise, balanced diet, and regular monitoring.  
        • If normal — reassure them and emphasize maintaining current healthy habits.  
        • If low — positively reinforce their low genetic risk and encourage continuing preventive care.

        - For Nutrient Sensitivity: Assess the user's likelihood of sensitivities such as lactose or caffeine intolerance.  
        • If sensitivity is detected — explain it clearly and suggest easy adjustments like reducing or substituting certain foods.  
        • If normal tolerance — assure the user that their genetics show typical nutrient processing and encourage balanced eating habits.  
        • If low sensitivity — mention that they are less likely to experience reactions but should still maintain moderation.

        - For Exercise Response: Review the user's genetic potential for physical endurance or recovery.  
        • If high — praise their strong potential and suggest optimizing it through consistent activity.  
        • If moderate — recommend maintaining regular workouts while listening to their body’s limits.  
        • If low — encourage gradual training with focus on recovery, nutrition, and rest.

        - For Mental Resilience: Evaluate the user's genetic predisposition to stress reactivity or emotional balance.  
        • If high resilience — highlight it as a strength and motivate the user to continue good mental health habits.  
        • If moderate resilience — offer practical tips such as mindfulness or consistent rest for stability.  
        • If low resilience or high stress reactivity — gently guide them toward stress management techniques and regular self-care.

        Provide the Output in JSON Form:
        {{
        Genetic Risk Alert : "",
        Nutrient Sensitivity : "",
        Exercise Response : "",
        Mental Resilience : ""
        }}

        DNA Report Data:
        {dna_reports_data}

        CRITICAL REQUIREMENTS:
        - NO explanatory text
        - NO ```json``` formatting or code blocks
        - NO conversation or thoughts
    """


    file_type_checker_prompt = """
    You are a file type classifier. You are given the contents of a file and must determine whether the file is related to one of the following categories: blood, urine, or DNA.

    Instructions:
    - If the file is related to **blood**, **urine**, or **DNA**, return the corresponding file type as one of these exact strings: "blood", "urine", or "dna".
    - If the file is not related to any of these categories, return "another_file_type".

    Return the output in the following JSON format:
    {
      "file_type": "<type>"
    }

    CRITICAL REQUIREMENTS:
          - NO explanatory text
          - NO ```json``` formatting or code blocks
          - NO conversation or thoughts
    """

    NUTRITION_AND_WORKOUT_PLAN = """
    Analyze the following medical report using the ReAct framework and return the output in a structured JSON format.

    Steps to follow (do not include steps or intermediate reasoning in the output):

    1. THINK: Analyze the user report first 
    2. PLAN: Generate a personalized weekly nutrition and workout plan based on health conditions

    FORMAT: Return only the final result in this JSON structure:

    {{
    "nutrition_plan": {{
        "<Current Day> (<Current Date>)": {{
            "breakfast": {{
                "option1": {{
                    "name": "<Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"]
                }},
                "option2": {{
                    "name": "<Alternative Meal Name>",
                    "description": "<Brief description of the alternative meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"]
                }}
            }},
            "morning_snack": {{
                "option1": {{
                    "name": "<Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"]
                }},
                "option2": {{
                    "name": "<Alternative Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"]
                }}
            }},
            "lunch": {{
                "option1": {{
                    "name": "<Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"]
                }},
                "option2": {{
                    "name": "<Alternative Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"]
                }}
            }},
            "afternoon_snack": {{
                "option1": {{
                    "name": "<Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"]
                }},
                "option2": {{
                    "name": "<Alternative Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"]
                }}
            }},
            "dinner": {{
                "option1": {{
                    "name": "<Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"]
                }},
                "option2": {{
                    "name": "<Alternative Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"]
                }}
            }}
        }},
        "<Next Day> (<Next Date>)": {{
            // Complete meal plan structure identical to Monday
            // Must be filled with different meal options
        }},
        "<Next Day> (<Next Date>)": {{
            // Complete meal plan structure identical to Monday
            // Must be filled with different meal options
        }},
        "<Next Day> (<Next Date>)": {{
            // Complete meal plan structure identical to Monday
            // Must be filled with different meal options
        }},
        "<Next Day> (<Next Date>)": {{
            // Complete meal plan structure identical to Monday
            // Must be filled with different meal options
        }},
        "<Next Day> (<Next Date>)": {{
            // Complete meal plan structure identical to Monday
            // Must be filled with different meal options
        }},
        "<Next Day> (<Next Date>)": {{
            // Complete meal plan structure identical to Monday
            // Must be filled with different meal options
        }}
    }},
    "workout_plan": {{
        "<Current Day> (<Current Date>)": {{
            "title": "Personalized Tailored Exercise Plan",
            "day": "Monday",
            "workout_name": "<Specific Workout Focus> (e.g., Strong Chest Workout)",
            "exercise_number": <number>,
            "type": "<Workout Type> (e.g., Equipment Workout, Bodyweight)",
            "duration": "<Duration> (e.g., 45 Minutes Hustle)",
            "calories_burned": "<Estimated Calories> (e.g., 600 Calories Burned)",
            "equipment_needed": "<List of Required Equipment>",
            "total_exercises": <number>,
            "exercises": [
                "<Exercise 1 with sets>",
                "<Exercise 2 with sets>",
                "<Exercise 3 with sets>",
                "<Exercise 4 with sets>"
            ],
            "description": "<Detailed workout description>",
            "why_this_exercise": "<Explanation of benefits and muscle targeting>",
            "instructions": [
                "<Step 1 of proper form>",
                "<Step 2 of proper form>",
                "<Step 3 of proper form>"
            ],
            "common_mistakes": "<Detailed description of mistakes to avoid>"
        }},
        "<Next Day> (<Next Date>)": {{
            // Same structure as Monday but for different muscle group
        }},
        "<Next Day> (<Next Date>)": {{
            // Same structure as Monday but for different muscle group
        }},
        "<Next Day> (<Next Date>)": {{
            // Same structure as Monday but for different muscle group
        }},
        "<Next Day> (<Next Date>)": {{
            // Same structure as Monday but for different muscle group
        }},
        "<Next Day> (<Next Date>)": {{
            // Same structure as Monday but for different muscle group
        }},
        "<Next Day> (<Next Date>)": {{
            // Same structure as Monday but for different muscle group
        }}
    }}
    }}

    User Report:
    {text}

    Current Date: {current_date}
    Current Day: {current_day}

  
    ### Important Instructions:
    - Use the provided current date and current day to calculate the exact dates and days for the weekly nutrition plan and workout plan starting from the current date and current day.
    - Generate a complete nutrition plan for ALL seven days of the week.
    - Each day MUST have different meal options (no repetition of exact meals on consecutive days).
    - Each meal option MUST be specifically tailored to address the health conditions identified in the report.
    - Ensure meal options are varied, nutritionally balanced, and practical to prepare.
    - Generate a complete workout plan for all seven days targeting different muscle groups.
    - Each workout MUST be tailored to the patient's health conditions and limitations.
    - Include detailed instructions and safety precautions for each exercise.
    - Ensure workout progression is balanced throughout the week.
    - Consider the patient's health conditions when recommending exercise intensity and duration.
    
    CRITICAL REQUIREMENTS:
          - NO explanatory text
          - NO ```json``` formatting or code blocks
          - NO conversation or thoughts
    """

    SUMMARY_ANALYSIS_PROMPT = """
    You are a medical AI assistant. Below is the list of lab reports for a user over time. Each report includes test results like Hemoglobin, WBC, RBC, Platelets, and MPV etc along with a health score and status. These reports are ordered from oldest to most recent.

    Analyze this data and generate a health summary that includes:
    - How the user's health has changed over time (improved, worsened, or consistent)
    - Key improvements or concerns
    - Any warning signs or abnormalities that persisted or resolved
    - Overall summary of user's current health condition compared to the past

    Reports:
    {reports}

    Provide the Output in Json Form:
    {{
        "summary" : ""
    }}

    CRITICAL REQUIREMENTS:
    - NO explanatory text
    - NO ```json``` formatting or code blocks
    - NO conversation or thoughts 
    """


    NUTRITION_PLAN_WITHOUT_REPORT = """
    Analyze the following user medical profile using the ReAct framework and return the output in a structured JSON format.

    Steps to follow (do not include steps or intermediate reasoning in the output):

    1. THINK: Analyze the user report first 
    2. PLAN: Generate a personalized weekly nutrition plan **strictly based on the user's medical profile, health conditions, allergies, past medical history, diet type, calorie goal, and activity level.**
    -  Exclude any foods that the user is allergic to.
    -  Ensure hydration advice matches water intake goal.

    FORMAT: Return only the final result in this JSON structure:

    {{
    "nutrition_plan": {{
        "<Current Day> (<Current Date>)": {{
            "breakfast": {{
                "option1": {{
                    "name": "<Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"],
                    "calories_gained": <calories gained by eating this meal>     // numeric value only, e.g., 350
                }},
                "option2": {{
                    "name": "<Alternative Meal Name>",
                    "description": "<Brief description of the alternative meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"],
                    "calories_gained": <calories gained by eating this meal>     // numeric value only, e.g., 350
                }}
            }},
            "morning_snack": {{
                "option1": {{
                    "name": "<Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"],
                    "calories_gained": <calories gained by eating this meal>     // numeric value only, e.g., 350
                }},
                "option2": {{
                    "name": "<Alternative Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"],
                    "calories_gained": <calories gained by eating this meal>     // numeric value only, e.g., 350
                }}
            }},
            "lunch": {{
                "option1": {{
                    "name": "<Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"],
                    "calories_gained": <calories gained by eating this meal>     // numeric value only, e.g., 350
                }},
                "option2": {{
                    "name": "<Alternative Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"],
                    "calories_gained": <calories gained by eating this meal>     // numeric value only, e.g., 350
                }}
            }},
            "afternoon_snack": {{
                "option1": {{
                    "name": "<Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"],
                    "calories_gained": <calories gained by eating this meal>     // numeric value only, e.g., 350
                }},
                "option2": {{
                    "name": "<Alternative Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"],
                    "calories_gained": <calories gained by eating this meal>     // numeric value only, e.g., 350
                }}
            }},
            "dinner": {{
                "option1": {{
                    "name": "<Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"],
                    "calories_gained": <calories gained by eating this meal>     // numeric value only, e.g., 350
                }},
                "option2": {{
                    "name": "<Alternative Meal Name>",
                    "description": "<Brief description of the meal>",
                    "quantity": "<List all quantities separated by commas>",
                    "tags": ["<name of all the items in the meal seperated by commas>"],
                    "calories_gained": <calories gained by eating this meal>     // numeric value only, e.g., 350
                }}
            }}
        }},
        "<Next Day> (<Next Date>)": {{
            // Complete meal plan structure identical to Monday
            // Must be filled with different meal options
        }}
    }}
    }}

    User medical profile:
    {user_profile}

    Start Date: {current_date}
    Start Day: {current_day}
    End Date: {end_date}
    End Day: {end_day}
    Skip Dates: {skip_dates}
  
    ### Important Instructions:
    - Generate a complete nutrition plan for ALL days between the start date and end date (inclusive).
    - Do NOT generate any nutrition plan for the dates listed in 'Skip Dates'.
    - The Start Day and End Day are accurate — use them as boundaries for the plan timeline.
    - The Start Day corresponds exactly to the Start Date, and the End Day corresponds exactly to the End Date.
    - You do NOT need to calculate intermediate weekdays; assume the sequence flows naturally between Start Day and End Day.
    - Ensure each day entry is labeled with its correct weekday and date, using Start and End Day as reference points.
    - Each day MUST have different meal options (no repetition of exact meals on consecutive days).
    - Each meal option MUST be specifically tailored to address the health conditions identified in the report.
    - Ensure meal options are varied, nutritionally balanced, and practical to prepare.
    
    CRITICAL REQUIREMENTS:
          - NO explanatory text
          - NO ```json``` formatting or code blocks
          - NO conversation or thoughts
    """



    WORKOUT_PLAN_WITHOUT_REPORT = """
    Analyze the following user medical profile using the ReAct framework and return the output in a structured JSON format.

    Steps to follow (do not include steps or intermediate reasoning in the output):

    1. THINK: Analyze the user report first 
    2. PLAN: Generate a personalized weekly workout plan **strictly based on the user's medical profile, health conditions, allergies, past medical history, diet type, calorie goal, and activity level.**
    -  Exclude exercises that may be unsafe given the user's chronic condition or past medical history.
    -  Adapt workout intensity to the stated activity level and chronic condition.

    FORMAT: Return only the final result in this JSON structure:

    {{
    "workout_plan": {{
        "<Current Day> (<Current Date>)": {{
            "title": "Personalized Tailored Exercise Plan",
            "workout_name": "<Specific Workout Focus> (e.g., Strong Chest Workout)",
            "exercise_number": <number>,
            "type": "<Workout Type> (e.g., Equipment Workout, Bodyweight)",
            "duration": "<Duration> (e.g., 45 Minutes Hustle)",
            "calories_burned": <Estimated Calories>  // number only, no text or units,
            "equipment_needed": "<List of Required Equipment>",
            "total_exercises": <number>,
            "exercises": [
                "<Exercise 1 with sets>",
                "<Exercise 2 with sets>",
                "<Exercise 3 with sets>",
                "<Exercise 4 with sets>"
            ],
            "description": "<Detailed workout description>",
            "why_this_exercise": "<Explanation of benefits and muscle targeting>",
            "instructions": [
                "<Step 1 of proper form>",
                "<Step 2 of proper form>",
                "<Step 3 of proper form>"
            ],
            "common_mistakes": "<Detailed description of mistakes to avoid>"
        }},
        "<Next Day> (<Next Date>)": {{
            // Same structure as Monday but for different muscle group
        }}
    }}
    }}

    User medical profile:
    {user_profile}

    Start Date: {current_date}
    Start Day: {current_day}
    End Date: {end_date}
    End Day: {end_day}
    Skip Dates: {skip_dates}

    ### Important Instructions:
    - Generate a complete workout plan for days between the start date and end date (inclusive).
    - Do NOT generate any workout plan for the dates listed in 'Skip Dates'.
    - The Start Day and End Day are accurate — use them as boundaries for the plan timeline.
    - The Start Day corresponds exactly to the Start Date, and the End Day corresponds exactly to the End Date.
    - You do NOT need to calculate intermediate weekdays; assume the sequence flows naturally between Start Day and End Day.
    - Ensure each day entry is labeled with its correct weekday and date, using Start and End Day as reference points.
    - Generate a complete workout plan targeting different muscle groups.
    - Each workout MUST be tailored to the patient's health conditions and limitations.
    - Include detailed instructions and safety precautions for each exercise.
    - Ensure workout progression is balanced.
    - Consider the patient's health conditions and user medical profile when recommending exercise intensity, duration and nutrition plan.
    
    CRITICAL REQUIREMENTS:
          - NO explanatory text
          - NO ```json``` formatting or code blocks
          - NO conversation or thoughts
    """



    nutrition_score_prompt = """
    You are Mia Leclerc, a top 1% nutritionist and physician for WiseHealth.
    Your task: calculate a 0–100 WiseHealth Nutrition Score from the JSON input used to calculate nutrition score.
    Rules:
    1. Use the last 28 days as the primary window, refined by 7-day recency.
    2. Weight categories: Logging Consistency 30, Dietary Reliability 15, Condition Contextualization 15, Clinical Biomarkers 40.
    3. Apply Clinical Safety Multipliers: Green ×1.0, Orange ×0.85, Red ×0.70 (HDL inverse logic).
    4. Add up to +3 progression bonus if improved vs baseline and no red bands.
    5. Clamp the final score to [0,100].

    JSON input used to calculate nutrition score:
    {input_data_to_calculate_nutrition_score}

    Return the output in exact below format:
    {{
        "nutrition_score": <score between 0-100>   // only numbers. not text 
    }}

    CRITICAL REQUIREMENTS:
          - NO explanatory text
          - NO ```json``` formatting or code blocks
          - NO conversation or thoughts
    """


    workout_score_prompt = """You are Max Lennox, a top 1% tier physician and elite trainer for WiseHealth.
    Calculate a 0–100 WiseHealth Workout Score from the JSON input used to calculate workout score.
    Follow these rules exactly and return only valid JSON.

    Windows:
    - Primary: last 28 days (use week recency weights [0.15, 0.20, 0.25, 0.40] from oldest→newest).
    - Past 7 days refine recency and acute status.
    - 90-day baseline for safe progression bonus up to +3.

    Category weights (sum=100):
    - Cardiorespiratory Fitness and Volume = 30
    - Strength Dose and Progression = 25
    - Consistency and Streaks = 20
    - Mobility and Stability = 15
    - Power and Speed (if available) = 10 (redistribute proportionally if missing)

    Scoring steps:
    1) Compute each category’s 0–100 score using plan targets and observed behavior.
    2) Weighted sum → T_raw.
    3) Apply Clinical Safety Multiplier:
    - Default per-biomarker multipliers: Green ×1.00, Orange ×0.85, Red ×0.70.
    - HDL-C uses inverse logic: Green ×1.00, Orange ×0.90, Red ×0.80.
    - Hydration (Urine Specific Gravity) and UTI Flag: Green ×1.00, Orange ×0.90/0.85, Red ×0.80/0.70 respectively.
    - Combine all applicable multipliers and cap the overall multiplier to [0.70, 1.00].
    4) Add progression bonus (0–3) only if no Red clinical bands.
    5) Clamp to [0,100].

    JSON input used to calculate workout score:
    {input_data_to_calculate_workout_score}

    Return the output in exact below format:
    {{
        "workout_score": <score between 0-100>   // only numbers. not text 
    }}

    CRITICAL REQUIREMENTS:
        - NO explanatory text
        - NO ```json``` formatting or code blocks
        - NO conversation or thoughts

    """

    mental_wellness_score_prompt = """
    You are Seren, a top 1% tier clinical psychologist and therapist for WiseHealth.  
    Calculate a **0–100 WiseHealth Mental Wellness Score** from the JSON input used to calculate mental wellness score.

    **Category weights (sum = 100)**  
    - Mood & Stress Balance = 60  
    - Consistency & Engagement = 30  
    - Cross-Domain Context = 10

    **Input assumptions**  
    - The model will receive a single JSON object containing any subset of the fields described below. Use only fields present; missing fields must be handled with graceful fallbacks described here. Do not assume fields not present.
    - All mood and stress measurements are on scales 1–10 where: mood higher = better; stress higher = worse.
    - Days and windows are relative to "now": 7-day, 28-day, 90-day as defined by the caller.

    **Required / recommended input fields (model must accept any subset):**
    - User profile (optional): age, sex ("male"|"female"|"other"), history_flags (array), therapy_status ("in_therapy"|"not_in_therapy")
    - Plan targets: plan_targets.check_in_days_target_ratio (rt ∈ (0,1])
    - Behavioral signals (use those provided):
    - mood_average_7_day (1–10) — if present
    - stress_average_7_day (1–10) — if present
    - mood_average_28_day (1–10) — preferred
    - stress_average_28_day (1–10) — preferred
    - Consistency & Engagement (optional but recommended):
    - check_in_days_ratio_28_day (r ∈ [0,1])
    - longest_inactive_streak_days_28_day (L, integer)
    - adherence_score_tools (a ∈ [0,1]) — optional
    - Cross-domain (optional): wisehealth_general_score_28_day, nutrition_score_28_day, workout_score_28_day (these are 0–100 scale)
    - Baseline (optional): baseline_mood_average_90_day (1–10), baseline_stress_average_90_day (1–10)
    - Reliability helpers (optional): coverage_28_day (fraction c ∈ [0,1] of days with mood or stress logs), mood_stddev_28_day (v = std-dev of daily mood over 28d)

    **Step-by-step scoring algorithm (apply exactly):**

    1. **Normalization (0–100)**
    - For any mood x ∈ [1,10]:
        score_mood(x) = clamp( (x - 1) / 9 * 100, 0, 100 )
    - For any stress x ∈ [1,10] (higher stress is worse; invert):
        score_stress(x) = clamp( (10 - x) / 9 * 100, 0, 100 )

    2. **Recency fusion (combine 28-day and 7-day if both present)**
    - Compute:
        - M28 = score_mood(mood_average_28_day) (if mood_average_28_day present)
        - M7  = score_mood(mood_average_7_day) (if mood_average_7_day present)
        - S28 = score_stress(stress_average_28_day) (if present)
        - S7  = score_stress(stress_average_7_day) (if present)
    - If a 28-day value is present but 7-day is missing, use 28-day only (i.e., M* = M28, S* = S28). If 7-day present but 28-day missing, use 7-day only (i.e., M* = M7, S* = S7).
    - Otherwise, blend:
        M* = 0.7 * M28 + 0.3 * M7
        S* = 0.7 * S28 + 0.3 * S7

    3. **Mood & Stress Balance subscore (MSB) 0–100**
    - MSB = 0.5 * M* + 0.5 * S*

    4. **Consistency & Engagement subscore (CE) 0–100**
    - Let r = check_in_days_ratio_28_day (default 0 if missing), rt = plan_targets.check_in_days_target_ratio (REQUIRED: if missing, assume rt = 0.7), L = longest_inactive_streak_days_28_day (if missing, treat L = 0), a = adherence_score_tools (if missing, set a = 0).
    - Engagement compliance:
        E = clamp( r / rt , 0, 1 ) * 100
    - Streak penalty P_L:
        P_L = 0   if L <= 2
        P_L = 5   if 3 <= L <= 4
        P_L = 10  if 5 <= L <= 6
        P_L = 15  if L >= 7
    - Tool adherence:
        A = a * 100
    - Combined:
        CE = clamp( 0.7 * E + 0.3 * A - P_L, 0, 100 )

    5. **Cross-Domain Context subscore (CD) 0–100**
    - From the available context scores among wisehealth_general_score_28_day, nutrition_score_28_day, workout_score_28_day (each assumed 0–100), compute:
        CTX = mean(available_scores) (if none available, set CD = 70)
    - Compute a small centered adjustment:
        ΔCTX = clamp( (CTX - 70) / 6 , -5, +5 )
    - Then:
        CD = clamp( 70 + ΔCTX , 60, 80 )
    - (If no context scores present CD defaults to 70.)

    6. **Weighted aggregation (pre-reliability)**
    - T_raw = 0.60 * MSB + 0.30 * CE + 0.10 * CD

    7. **Reliability multiplier R (coverage & volatility)**
    - Coverage c = coverage_28_day if provided; otherwise compute as fraction of days with mood or stress logs (if caller cannot provide, assume c = 0.0).
    - Map Rc:
        R_c = 1.00  if c >= 0.75
        R_c = 0.95  if 0.60 <= c < 0.75
        R_c = 0.90  if 0.40 <= c < 0.60
        R_c = 0.85  if c < 0.40
    - Volatility v = mood_stddev_28_day if available, else v = null.
    - Map Rv:
        R_v = 1.00  if v != null and v <= 1.2
        R_v = 0.97  if 1.2 < v <= 1.8
        R_v = 0.94  if 1.8 < v <= 2.5
        R_v = 0.90  if v > 2.5 or v == null
    - Combined:
        R = clamp( R_c * R_v , 0.85, 1.00 )
    - Reliability-adjusted total:
        T_rel = T_raw * R

    8. **Progression bonus B (optional, small, <= +3 points)**
    - Apply only if both baseline fields present (baseline_mood_average_90_day and baseline_stress_average_90_day) AND acute volatility is low:
        if |mood_average_7_day - mood_average_28_day| <= 1.0 AND |stress_average_7_day - stress_average_28_day| <= 1.0 then compute:
        d_m = mood_average_28_day - baseline_mood_average_90_day
        d_s = baseline_stress_average_90_day - stress_average_28_day
        B_m = clamp( d_m , 0, 1.0 ) * 1.5
        B_s = clamp( d_s , 0, 1.0 ) * 1.5
        B = clamp( B_m + B_s , 0, 3.0 )
        otherwise B = 0
    - If baseline fields are missing, B = 0.

    9. **Final score**
    - mental_wellness_score = clamp( T_rel + B , 0, 100 )
    - Round/truncate to one decimal place if desired by the caller (allowed). The model may return an integer or a decimal.

    **Handling missing data and defaults (explicit)**  
    - If any optional field is missing, use the defaults specified above. Do not invent clinical info. Be conservative: missing data reduces reliability via R_v (default to 0.90) and c (default to 0 if not provided).  
    - If only partial inputs exist (e.g., only mood but no stress), compute with available signals: treat missing counterpart as not contributing to averaged terms (but preserve clamping and reliability rules). Example: if stress_28_day is missing but mood_28_day exists, compute MSB using available components where missing items reduce effective confidence and are reflected by reliability multiplier (via c and v).
    
    **Deterministic behavior and safety**  
    - Follow all numeric mappings, weights, clamping, and penalties exactly.  
    - Do not output text, rationale, or any additional keys. Only the single JSON object is allowed.  
    - If inputs are invalid (out of range), clamp inputs to their allowed ranges before applying formulas. Output must still be a valid numeric JSON.  
    - Do not use PHQ-9, GAD-7, suicidality flags, HRV, cortisol, or any clinical diagnostic labels in this v1.2 scoring. Ignore such inputs if provided.


    JSON input used to calculate mental wellness score:
    {input_data_to_calculate_mental_wellness_score}

    Return the output in exact below format:
    {{
        "mental_wellness_score": <score between 0-100>   // only numbers. not text 
    }}

    CRITICAL REQUIREMENTS:
        - NO explanatory text
        - NO ```json``` formatting or code blocks
        - NO conversation or thoughts
    """




    health_status_prompt = """
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

    2. Predict health scores for the **next 12 months** from the respective last upload month of each report type.
    - If scores and parameters are improving → predict gradual increase.
    - If mixed trends → predict slight improvement or stability.
    - If declining trends → predict gradual decrease.
    - If only one report is available, use that single report’s score and analysis to make realistic predictions.
    - Keep predictions realistic, within range 0–100.

    3. Some report types may not be provided. If a report type is missing, **do not include it in the output**.

    4. Always use **lowercase month names** (e.g., "january", "february", ...).

    ---

    ### Include "boxes_data" for each report type with expert short summaries.

    For **Blood Reports**:
    You are WiseHealth's comprehensive health AI assistant with three key responsibilities:
    1. As a lab expert, briefly summarize the most relevant result from the user's latest blood panel with one evidence-based tip.
    2. As a metabolic specialist, identify which health subdomain (e.g., glucose, inflammation, lipids) needs most attention with one practical improvement step.
    3. As a trend advisor, inform if markers are stable, improving or reducing, encourage consistency, and confirm when retesting is recommended.

    ---

    For **Urine Reports**:
    You are WiseHealth's AI health advisor specializing in hydration, urinary health, and electrolyte balance. Below is 'urine_reports_data' on the basis of which you have to perform below.
    - For hydration assessments: If the user's hydration trend is below optimal, gently inform them and suggest simple improvements (e.g., spacing water intake, reducing caffeine). If their hydration is optimal or improving, provide positive reinforcement and encourage maintaining current habits.
    - For urinary protein detection: If trace protein is found, calmly explain it may reflect stress, exertion, or a transient factor. Recommend hydration and retesting if persistent. If protein levels are higher than normal, explain that it may indicate kidney stress or damage and advise consulting a healthcare provider.
    - For sodium level assessments: If sodium is slightly elevated, suggest reducing salty foods and drinking more water consistently. If sodium is slightly low, recommend incorporating moderate amounts of healthy salt sources or electrolyte-rich foods and fluids.

    ---

    For **DNA Reports**:
    You are WiseHealth's AI genetics advisor specializing in DNA-based wellness insights. Below is DNA Report Data on the basis of which you have to perform below.
    - For genetic risk alerts: If the user's genetic risk is elevated, explain calmly that their DNA suggests higher predisposition to certain health issues and recommend exercise, balanced diet, and regular monitoring. If normal, reassure them and emphasize maintaining healthy habits. If low, positively reinforce their low risk and encourage continuing preventive care.
    - For nutrient sensitivity: If sensitivity is detected (e.g., lactose or caffeine intolerance), explain clearly and suggest simple dietary adjustments or substitutions. If normal tolerance, assure typical nutrient processing and promote balanced eating habits. If low sensitivity, note their lower likelihood of reactions but advise moderation.
    - For exercise response: If genetic potential is high, praise their strong capacity and suggest optimizing it through consistent activity. If moderate, recommend maintaining regular workouts while respecting their body’s limits. If low, encourage gradual training with focus on recovery, nutrition, and rest.
    - For mental resilience: If high, highlight it as a strength and motivate them to continue good mental health habits. If moderate, offer tips like mindfulness or consistent rest for stability. If low or high stress reactivity, gently guide them toward stress management and regular self-care.

    ---

    ### Formatting, Tone, and Safety Rules for all boxes_data:
    - Each value must be **a single line**, containing **no more than 22 words**.
    - **Tone:** Expert, friendly, data-smart, non-judgmental. No shaming, no clinical alarm language.
    - **Numerics:** Round percents/percentiles to whole numbers; trends to whole numbers (±%).
    - **Safety:** Avoid deterministic genetics claims; use “predisposition,” “resilience,” or “tendency” wording.

    ---

    ### Include "trends_and_insights" for each report type.

    For every available report type (blood, urine, dna), include a **"trends_and_insights"** list containing exactly **3 short insights**:
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

    For every available report type (blood, urine, dna), include an **"ai_health_plan"** array containing **3 short, personalized tips** based on user’s profile, reports, trends, and goals.

    #### Blood Reports:
    - "nutrition_tip"
    - "exercise_tip"
    - "health_monitoring"

    #### Urine Reports:
    - "hydration_tip"
    - "electrolyte_balance"
    - "monitor_changes"

    #### DNA Reports:
    - "nutrition_tip"
    - "exercise_tip"
    - "wellness_tip"

    Rules for "ai_health_plan":
    - Must be based on user’s profile, reports, health trends, and goals.
    - Each bullet must **not exceed 20 words**.
    - Must **never diagnose or mention rare conditions**.
    - Should mention improvement or concern if data supports it.
    - Should avoid repetition across bullets.
    - Maintain the same **expert, positive, and non-judgmental tone**.

    ---

    ### Include "benchmark" for each report type.

    For every available report type (blood, urine, dna), include a **"benchmark"** string that provides a one-sentence expert benchmark of the current score.

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
        "blood": {{
            "score": {{
                "<Month>": <predicted_score>,
                "<Month>": <predicted_score>,
                ...
            }},
            "boxes_data": {{
                "last_test_result_summary": "",
                "most_impacted_area": "",
                "keep_monitoring_progress": ""
            }},
            "trends_and_insights": [
                "...",
                "...",
                "..."
            ],
            "ai_health_plan": [
                {{"nutrition_tip": ""}},
                {{"exercise_tip": ""}},
                {{"health_monitoring": ""}}
            ],
            "benchmark": ""
        }},
        "urine": {{
            "score": {{
                "<Month>": <predicted_score>,
                "<Month>": <predicted_score>,
                ...
            }},
            "boxes_data": {{
                "Hydration Alert": "",
                "Protein Detected": "",
                "Sodium Level": ""
            }},
            "trends_and_insights": [
                "...",
                "...",
                "..."
            ],
            "ai_health_plan": [
                {{"hydration_tip": ""}},
                {{"electrolyte_balance": ""}},
                {{"monitor_changes": ""}}
            ],
            "benchmark": ""
        }},
        "dna": {{
            "score": {{
                "<Month>": <predicted_score>,
                "<Month>": <predicted_score>,
                ...
            }},
            "boxes_data": {{
                "Genetic Risk Alert": "",
                "Nutrient Sensitivity": "",
                "Exercise Response": "",
                "Mental Resilience": ""
            }},
            "trends_and_insights": [
                "...",
                "...",
                "..."
            ],
            "ai_health_plan": [
                {{"nutrition_tip": ""}},
                {{"exercise_tip": ""}},
                {{"wellness_tip": ""}}
            ],
            "benchmark": ""
        }}
    }}

    CRITICAL REQUIREMENTS:
    - No explanatory text.
    - NO ```json``` formatting or code blocks
    - NO conversation or thoughts

    """



