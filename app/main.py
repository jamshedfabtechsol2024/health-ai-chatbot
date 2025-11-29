import re
from app.schemas import QAInput, ChatMessageModel, ChatHistoryModel, SurveyModel, SurveyModelQA, UpdateSurveyModel , PlanRequest , UserProfile
from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from typing import Optional, List
import httpx
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from app import schemas
from app.database import get_db
from mainn import main , FileAnalysis
from utils.utils import TokenService

app = FastAPI()

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify the domains you want to allow
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

DJANGO_AUTH_URL = "http://localhost:8000/api/user-chats/authenticate/"  # adjust as needed


@app.post("/chat-stream/")
async def stream_chat_response(
        payload: QAInput,
        chatbot_key: str = Query(...)
):
    try:
        # Step 1: Authenticate and fetch chat history
        async with httpx.AsyncClient() as client:
            auth_response = await client.get(
                "http://localhost:8000/api/user-chats/authenticate/",
                params={
                    "uid": payload.user_id,
                    "chatbot_key": chatbot_key,
                    "chatbot_type": payload.chatbot_type,
                    "user_chat_id": payload.chats
                }
            )

        if auth_response.status_code != 200:
            raise HTTPException(status_code=403, detail="Invalid user authentication")

        auth_data = auth_response.json()

        chat_history = auth_data.get("chat_history", [])

        # Step 2: Get bot response from your main processing logic
        full_response = main(
            user_id=str(payload.user_id),
            user_input=payload.user_input,
            chat_history=chat_history,
            file_path="",
            report_type="",
            previous_reports_data=""
        )

        message = full_response.get("answer", "")

        # Step 3: Stream response word by word
        async def response_stream():
            for word in message.split():
                yield f"data: {word}\n\n"
                await asyncio.sleep(0.05)

        # Step 4: Save messages back to Django
        message_data = {
            "user": payload.user_id,
            "user_chat": payload.chats,
            "chatbot_type": payload.chatbot_type,
            "chats": [
                {"sender": "user", "message": payload.user_input},
                {"sender": "bot", "message": message}
            ]
        }
        if payload.report_type:
            message_data["report_type"] = payload.report_type
        if payload.file_path:
            message_data["file_path"] = payload.file_path

        async with httpx.AsyncClient() as client:
            save_response = await client.post(
                "http://localhost:8000/api/chats/",
                json=message_data
            )

        if save_response.status_code != 201:
            try:
                error_detail = save_response.json()
            except Exception:
                error_detail = save_response.text
            raise HTTPException(
                status_code=save_response.status_code,
                detail={"message": "Failed to save messages", "errors": error_detail}
            )

        return StreamingResponse(response_stream(), media_type="text/event-stream")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


VALID_REPORT_TYPES = ["blood", "dna", "urine"]


def _format_nutrition_plan(nutrition_plan):
    """Helper function to format nutrition plan data with tags"""
    formatted_days = {}

    for day, meals in nutrition_plan.items():
        formatted_days[day] = {
            "breakfast": {
                "options": [
                    {
                        "name": option.get('name', ''),
                        "description": option.get('description', ''),
                        "quantity": option.get('quantity', ''),
                        "tags": option.get('tags', [])
                    }
                    for option in meals.get('breakfast', {}).values()
                    if isinstance(option, dict)
                ]
            },
            "morning_snack": {
                "options": [
                    {
                        "name": option.get('name', ''),
                        "description": option.get('description', ''),
                        "quantity": option.get('quantity', ''),
                        "tags": option.get('tags', [])
                    }
                    for option in meals.get('morning_snack', {}).values()
                    if isinstance(option, dict)
                ]
            },
            "lunch": {
                "options": [
                    {
                        "name": option.get('name', ''),
                        "description": option.get('description', ''),
                        "quantity": option.get('quantity', ''),
                        "tags": option.get('tags', [])
                    }
                    for option in meals.get('lunch', {}).values()
                    if isinstance(option, dict)
                ]
            },
            "afternoon_snack": {
                "options": [
                    {
                        "name": option.get('name', ''),
                        "description": option.get('description', ''),
                        "quantity": option.get('quantity', ''),
                        "tags": option.get('tags', [])
                    }
                    for option in meals.get('afternoon_snack', {}).values()
                    if isinstance(option, dict)
                ]
            },
            "dinner": {
                "options": [
                    {
                        "name": option.get('name', ''),
                        "description": option.get('description', ''),
                        "quantity": option.get('quantity', ''),
                        "tags": option.get('tags', [])
                    }
                    for option in meals.get('dinner', {}).values()
                    if isinstance(option, dict)
                ]
            }
        }

    return formatted_days


def _format_workout_plan(workout_plan):
    """Helper function to format workout plan data with tags"""
    formatted_workouts = {}

    for day, workout in workout_plan.items():
        tags = [workout.get('type', '').lower()]
        if workout.get('focus_areas'):
            tags.extend(workout.get('focus_areas', []))
        else:
            tags.extend([workout.get('workout_name', '').lower()])

        formatted_workouts[day] = {
            "workout_overview": {
                "title": workout.get('title', ''),
                "workout_name": workout.get('workout_name', ''),
                "type": workout.get('type', ''),
                "duration": workout.get('duration', ''),
                "calories_burned": workout.get('calories_burned', ''),
                "equipment_needed": workout.get('equipment_needed', ''),
                "total_exercises": workout.get('total_exercises', 0),
                "tags": tags
            },
            "exercise_details": {
                "exercises": workout.get('exercises', []),
                "description": workout.get('description', ''),
                "why_this_exercise": workout.get('why_this_exercise', ''),
                "instructions": workout.get('instructions', []),
                "common_mistakes": workout.get('common_mistakes', '')
            }
        }

    return formatted_workouts


from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import json
from datetime import datetime


@app.post("/analyze-report/")
async def analyze_report(data: schemas.AnalyzeReportInput):
    try:
        # Call the main function
        print(str(data.user_id),data.file_path,data.report_type)
        response = FileAnalysis(
            user_id=str(data.user_id),
            file_path=data.file_path,
            report_type=data.report_type,
        )

        # Parse raw_analysis JSON string
        try:
            parsed_analysis = json.loads(response.get('raw_analysis', '{}'))
            print("Parsed Analysis:", parsed_analysis)
        except json.JSONDecodeError:
            parsed_analysis = {}

        
        return JSONResponse(
            content=parsed_analysis,
            headers={"Content-Type": "application/json; charset=utf-8"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@app.post('/store-chat-message')
async def store_chat_message(
        payload: QAInput,
        survey: Optional[List[SurveyModel]] = None,
        survey_type: Optional[str] = None,
        db: Session = Depends(get_db)
):
    try:
        if survey_type:
            current_survey = SurveyModelQA.get_personal_trainer_form_by_user_and_survey(payload.user_id, survey_type,
                                                                                        db)
            mcq_data = current_survey.survey_json if current_survey else []

            if isinstance(mcq_data, str):
                try:
                    mcq_data = json.loads(mcq_data)
                except json.JSONDecodeError:
                    mcq_data = []

            survey = {
                "question_answer": mcq_data
            }

            if survey_type == "therapist":
                survey["mental_score_summary"] = {
                    "avg_last_3_days": 64,
                    "avg_last_week": 66,
                    "avg_last_month": 70
                }

            elif survey_type == "workout":
                survey.update({
                    "fitness_score_summary": {
                        "avg_last_3_days": 64,
                        "avg_last_week": 66,
                        "avg_last_month": 70
                    },
                    "diseases": "Diabetes",
                    "Bmi": 24,
                    "streak_days": 3,
                    "calories_this_week": 1500,
                    "calories_goal": 1650,
                    "avg_duration": 45,
                    "wisehealthscore_month": 82,
                    "wisehealthscore_week": 78,
                    "wisehealthscore_3days": 86,
                    "daily_workout_plan": {
                        "today_session_type": "Upper Body Strength",
                        "duration": "40 min",
                        "status": "Pending"
                    },
                    "insights": {
                        "training": "You've completed 4 of 5 sessions this week. CK and cortisol are slightly elevated — recovery is recommended.",
                        "hydration": "Hydration has improved, but sodium-potassium balance is still low. Consider a rehydration strategy post-session."
                    }
                })

            elif survey_type == "nutrition":
                survey.update({
                    "nutrition_score_summary": {
                        "avg_last_3_days": 64,
                        "avg_last_week": 66,
                        "avg_last_month": 70
                    },
                    "Bmi": 24,
                    "avg_wisehealthscore_month": 82,
                    "insights": {
                        "health": "Your cholesterol levels improved by 8% this month. Hemoglobin remains stable. LDL is slightly elevated — consider adjusting your diet.",
                        "nutrition": "Your nutrition score dropped by 5% this week. Fiber and protein intake below optimal levels. Hydration improved compared to last month's average."
                    }
                })

        chat_history = ChatHistoryModel(
            user_id=int(payload.user_id)
        ).get_chat_history(user_id=int(payload.user_id), chat_bot_type=payload.chatbot_type, chat_id=payload.chat_id, db=db)
        chat_message_current = ChatMessageModel.get_chat_by_id(payload.chat_id, db)

        transformed_history = []

        for idx, chat in enumerate(chat_history):
            raw = chat.get("history_json")

            if not raw:
                continue

            # Parse if string
            if isinstance(raw, str):
                try:
                    raw = json.loads(raw)
                except json.JSONDecodeError:
                    continue

            if isinstance(raw, dict):
                # Use 'role' field as the user's question
                user_question = raw.get("role", "").strip()
                assistant_response = raw.get("content", "").strip()

                if user_question and assistant_response:
                    transformed_history.append({"role": "user", "content": user_question})
                    transformed_history.append({"role": "assistant", "content": assistant_response})

            elif isinstance(raw, list):
                for item in raw:
                    # Optionally use same logic if list has dicts with similar structure
                    if isinstance(item, dict) and 'role' in item and 'content' in item:
                        role = item['role'].strip().lower()
                        content = item['content'].strip()
                        if role in ["user", "assistant"]:
                            transformed_history.append({"role": role, "content": content})
        result = main(
            user_id=str(payload.user_id),
            user_input=payload.user_input,
            history_msgs=transformed_history,
            file_path="",
            report_type=payload.chatbot_type,
            chatbot_type=payload.chatbot_type,
            survey=survey
        )
        message = result.get('answer')
        if chat_message_current and chat_message_current.message == '':
            chat_message = ChatMessageModel.update_chat(payload.chat_id, message, db)
        else:
            chat_message = ChatMessageModel(
                message=message,
                chatbot_type=payload.chatbot_type,
                user_id=payload.user_id,
                report_type=payload.chatbot_type,
                created_at=datetime.now().isoformat()
            ).store_chat(db)
        ChatHistoryModel(
            user_id=int(payload.user_id),
            chat_id=payload.chat_id
        ).store_user_chat_history(role=payload.user_input, content=chat_message.message, db=db)

        remaining = TokenService.deduct_chat_token(int(payload.user_id), db)
        print(f"Remaining tokens for user {payload.user_id}: {remaining}")

        db.commit()

        async def get_stream():
            for word in message.split():
                yield f"data: {word}\n\n"
                await asyncio.sleep(0.05)

        return StreamingResponse(get_stream(), media_type="text/event-stream")

    except BaseException as e:
        raise e


@app.get('/get-chat-messages')
async def get_chat_message(
        user_id: int,
        chat_bot_type: str,
        chat_id: int,
        db: Session = Depends(get_db)
):
    try:
        history = ChatHistoryModel.get_chat_history(user_id, chat_id, chat_bot_type, db)
        if history:
            transformed_history = []
            for h in history:
                item = h["history_json"]
                transformed_history.append({"role": "User", "content": item.get("role", "")})
                transformed_history.append({"role": "Bot", "content": item.get("content", "")})
            return transformed_history
        else:
            return []
    except BaseException as e:
        raise e


@app.get('/chat-name')
async def chat_name(
        user_id: int,
        chat_bot_type: str,
        db: Session = Depends(get_db)
):
    try:
        return ChatHistoryModel.get_chat_names(user_id, chat_bot_type, db)
    except BaseException as e:
        raise e


@app.post('/new-chat')
async def new_chat(
        user_id: int,
        chat_bot_type: str,
        db: Session = Depends(get_db)
):
    try:
        return ChatMessageModel.create_new_chat(user_id, chat_bot_type, db)
    except BaseException as e:
        raise e


@app.get('/search')
async def search(
        user_id: int,
        chat_bot_type: str,
        name: str,
        db: Session = Depends(get_db)
):
    try:
        return ChatHistoryModel.search(user_id, chat_bot_type, name, db)
    except BaseException as e:
        raise e


@app.delete('/delete-chat')
async def delete_chat(
        user_id: int,
        chat_id: int,
        db: Session = Depends(get_db)
):
    try:
        ChatHistoryModel.delete_chat_history(user_id, chat_id, db)
        return ChatMessageModel.delete_chat_message(user_id, chat_id, db)
    except BaseException as e:
        raise e


@app.post('/store-mcq-chat-form')
async def store_mcq_data(
        payload: SurveyModelQA,
        db: Session = Depends(get_db)
):
    try:
        return payload.add_personal_chat(db)
    except BaseException as e:
        raise e


@app.get('/is-mcq-chat-form-expired')
async def is_expired(
        user_id: int,
        survey_type: str,
        db: Session = Depends(get_db)
):
    try:
        return SurveyModelQA.is_personal_trainer_form_expired(user_id, survey_type, db)
    except BaseException as e:
        raise e


@app.delete('/delete-survey')
async def delete(
        user_id: int,
        survey_type: str,
        db: Session = Depends(get_db)
):
    try:
        return SurveyModelQA.delete_survey(user_id, survey_type, db)
    except BaseException as e:
        raise e


@app.get('/is-two-min-breathing-expired')
async def two_min_breathing_expired(
        user_id: int,
        survey_type: str,
        db: Session = Depends(get_db)
):
    try:
        return SurveyModelQA.is_two_min_breathing_expired(user_id, survey_type, db)
    except BaseException as e:
        raise e


@app.patch('/update-survey/{user_id}')
async def update(
        payload: UpdateSurveyModel,
        user_id: int,
        survey_type: str,
        db: Session = Depends(get_db)
):
    try:
        return payload.update_survey(user_id, survey_type, db)
    except BaseException as e:
        raise e



import json
import logging
from Models.models import report_analysis_model
from AnalyzeReport.prompt import Prompts
from utils.utils import HealthReportUtils
from pprint import pprint
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any


class Plain_data_without_report:

    def plans(self, current_date, current_day, user_profile):

        prompt = Prompts.NUTRITION_AND_WORKOUT_PLAN_WITHOUT_REPORT.format(user_profile=user_profile, current_date=current_date, current_day=current_day)
        output = report_analysis_model.invoke(prompt)
        return output.content




@app.post("/generate_plan")
def generate_plan(req: PlanRequest) -> Dict[str, Any]:
    try:
        planner = Plain_data_without_report()
        # Convert Pydantic model to plain dict for formatting
        profile_dict = req.user_profile.dict()
        plan_content = planner.plans(
            current_date=req.current_date,
            current_day=req.current_day,
            user_profile=profile_dict,
        )
        return {"plan": json.loads(plan_content)}
    except Exception as e:
        # Return HTTP 500 with error message
        raise HTTPException(status_code=500, detail=str(e))