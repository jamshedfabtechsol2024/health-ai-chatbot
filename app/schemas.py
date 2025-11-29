import re
from datetime import datetime, timezone, timedelta
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import and_
from sqlalchemy.orm import Session
from .models import ChatMessage, ChatHistory, AppSurveyModel
from fastapi import HTTPException


# schemas.py
class MessageSchema(BaseModel):
    content: dict
    is_encrypted: bool


class QAInput(BaseModel):
    user_id: str
    chat_id: int
    chats: Optional[int] = None
    user_input: str
    chatbot_type: Optional[str] = None
    file_path: Optional[str] = None
    previous_reports_data: Optional[str] = None
    chat_history: Optional[list] = None


class AnalyzeReportInput(BaseModel):
    user_id: int
    file_path: str
    report_type: str


class AuthInput(BaseModel):
    id: int
    chat_bot: str


class ChatMessageModel(BaseModel):
    id: Optional[int] = None
    chatbot_type: Optional[str] = None
    report_type: Optional[str] = None
    created_at: Optional[datetime] = None
    message: str
    user_id: int

    def store_chat(self, db: Session):
        now = datetime.utcnow().isoformat()
        chat_message = ChatMessage(
            message=self.message,
            created_at=now,
            report_type=self.report_type,
            chat_bot_type=self.chatbot_type,
            user_id=self.user_id
        )

        db.add(chat_message)

        return self

    @staticmethod
    def update_chat(chat_id: int, message: str, db: Session):
        chat = ChatMessageModel.get_chat_by_id(chat_id, db)
        chat.message = message

        return chat

    @staticmethod
    def get_chat_message_by_content(message: str, db: Session):
        return db.query(ChatMessage).filter(ChatMessage.message == message).first()

    @staticmethod
    def get_chat_by_id(chat_id: int, db: Session):
        return db.query(ChatMessage).filter(
            ChatMessage.id == chat_id
        ).first()

    @staticmethod
    def create_new_chat(user_id: int, chat_bot_type: str, db: Session):
        now = datetime.now().isoformat()
        new_chat = ChatMessage(
            user_id=user_id,
            message='',
            chat_bot_type=chat_bot_type,
            report_type=chat_bot_type,
            created_at=now
        )

        db.add(new_chat)
        db.commit()

        return {
            "chat_id": new_chat.id
        }

    @staticmethod
    def delete_chat_message(user_id: int, chat_id: int, db: Session):
        chats = db.query(ChatMessage).filter(
            ChatMessage.id == chat_id,
            ChatMessage.user_id == user_id
        ).all()

        if not chats:
            raise HTTPException(status_code=404, detail='Chat not found')

        for chat in chats:
            db.delete(chat)
        db.commit()

        return {
            "message": "Chat Message deleted!"
        }


class ChatHistoryModel(BaseModel):
    user_id: int
    chat_id: Optional[int] = None
    history: Optional[str] = None

    def store_user_chat_history(self, role: str, content: str, db: Session):
        chat_data = {
            "role": role,
            "content": content
        }
        history = ChatHistory(
            user_id=self.user_id,
            chat_id=self.chat_id,
            history_json=chat_data
        )
        db.add(history)

        return {
            "message": "history saved"
        }

    @staticmethod
    def get_chat_history(user_id, chat_id: int, chat_bot_type: str, db: Session):
        message_chats = db.query(ChatMessage).filter(
            ChatMessage.chat_bot_type == chat_bot_type,
            ChatMessage.id == chat_id
        ).all()

        if not message_chats:
            return []

        history_records = []
        for message_chat in message_chats:
            records = (db.query(ChatHistory).filter(
                ChatHistory.user_id == user_id,
                ChatHistory.chat_id == message_chat.id
            ).order_by(ChatHistory.id.asc()).all())
            history_records.extend(records)

        return [
            {
                "id": h.id,
                "user_id": h.user_id,
                "chat_id": h.chat_id,
                "history_json": h.history_json
            }
            for h in history_records
        ]

    @staticmethod
    def get_chat_names(user_id: int, chat_bot_type: str, db: Session):
        all_chats = db.query(ChatHistory).select_from(ChatHistory).join(
            ChatMessage,
            ChatHistory.chat_id == ChatMessage.id
        ).filter(
            ChatHistory.user_id == user_id,
            ChatMessage.chat_bot_type == chat_bot_type
        ).order_by(ChatHistory.id.desc()).all()  # Ensure consistent ordering

        seen_chat_ids = set()
        chat_names = []

        for chat in all_chats:
            if chat.chat_id in seen_chat_ids:
                continue
            seen_chat_ids.add(chat.chat_id)

            content = chat.history_json.get("content", "")
            chat_name = ChatHistoryModel.generate_chat_title(content)
            chat_names.append({
                "name": chat_name,
                "chat_id": chat.chat_id
            })

        return chat_names

    @staticmethod
    def delete_chat_history(user_id: int, chat_id: int, db: Session):
        chats = db.query(ChatHistory).filter(
            ChatHistory.chat_id == chat_id,
            ChatHistory.user_id == user_id
        ).all()

        if not chats:
            raise HTTPException(status_code=404, detail="No chat history found for this user and chat_id")

        for chat in chats:
            db.delete(chat)

        db.commit()
        return {"detail": "Chat history deleted successfully"}

    @staticmethod
    def generate_chat_title(content: str) -> str:
        content = re.sub(r'^role:\s*\w+', '', content).strip()

        sentences = re.split(r'[.!?]\s+', content)

        for sentence in sentences:
            clean = sentence.strip()
            if clean:
                title = clean[0].upper() + clean[1:]
                return title[:60] + ("..." if len(title) > 60 else "")

    @staticmethod
    def search(user_id: int, chat_bot_type: str, query: str, db: Session):
        all_chats = db.query(ChatHistory).select_from(ChatHistory).join(
            ChatMessage,
            ChatHistory.chat_id == ChatMessage.id
        ).filter(
            ChatHistory.user_id == user_id,
            ChatMessage.chat_bot_type == chat_bot_type
        ).all()

        results = []
        seen_chat_ids = set()
        query_lower = query.strip().lower()

        for chat in all_chats:
            content = chat.history_json.get("content", "")
            content_words = content.strip().split()
            first_5_words = " ".join(content_words[:5]).lower()

            if query_lower in first_5_words and chat.chat_id not in seen_chat_ids:
                chat_name = ChatHistoryModel.generate_chat_title(content)
                results.append({
                    "chat_id": chat.chat_id,
                    "name": chat_name
                })
                seen_chat_ids.add(chat.chat_id)

        return results


class SurveyModel(BaseModel):
    question: str
    answer: str


class SurveyModelQA(BaseModel):
    survey_json: List[SurveyModel]
    user_id: int
    survey_type: str
    two_min_breathing: Optional[bool] = False

    def add_personal_chat(self, db: Session):
        now = datetime.utcnow().isoformat()

        current_form = db.query(AppSurveyModel).filter(
            AppSurveyModel.user_id == self.user_id,
            AppSurveyModel.survey_type == self.survey_type
        ).all()

        if current_form:
            for form in current_form:
                db.delete(form)
        db.commit()

        data = AppSurveyModel(
            user_id=self.user_id,
            survey_json=[q.dict() for q in self.survey_json],
            created_at=now,
            survey_type=self.survey_type,
            two_min_breathing=now if self.survey_type == 'therapist' and self.two_min_breathing else None
        )

        db.add(data)
        db.commit()

        return {
            "message": "Submitted!"
        }

    @staticmethod
    def get_personal_trainer_form_by_user_and_survey(user_id, survey_type: str, db: Session):
        return db.query(AppSurveyModel).filter(
            AppSurveyModel.user_id == user_id,
            AppSurveyModel.survey_type == survey_type
        ).first()

    @staticmethod
    def is_personal_trainer_form_expired(user_id: int, survey_type: str, db: Session):
        current_data = SurveyModelQA.get_personal_trainer_form_by_user_and_survey(user_id, survey_type, db)

        if not current_data:
            raise HTTPException(status_code=404, detail='Form is not submitted yet')

        now = datetime.now(timezone.utc).replace(microsecond=0)
        age = now - (current_data.created_at.replace(microsecond=0))

        return age >= timedelta(hours=24)

    @staticmethod
    def delete_survey(user_id: int, survey_type: str, db: Session):
        surveys = db.query(AppSurveyModel).filter(
            AppSurveyModel.survey_type == survey_type,
            AppSurveyModel.user_id == user_id
        ).all()

        for survey in surveys:
            db.delete(survey)

        db.commit()

        return {
            "message": "Survey deleted"
        }

    @staticmethod
    def is_two_min_breathing_expired(user_id: int, survey_type: str, db: Session):
        current_data = SurveyModelQA.get_personal_trainer_form_by_user_and_survey(user_id, survey_type, db)

        if not current_data:
            raise HTTPException(status_code=404, detail='Form is not submitted yet')

        if not current_data.two_min_breathing:
            raise HTTPException(status_code=400, detail='two_min_breathing timestamp not set')

        now = datetime.now(timezone.utc).replace(microsecond=0)
        age = now - (current_data.two_min_breathing.replace(microsecond=0))

        return age >= timedelta(hours=24)


class UpdateSurveyModel(BaseModel):
    two_min_breathing: bool

    def update_survey(self, user_id: int, survey_type: str, db: Session):
        data = SurveyModelQA.get_personal_trainer_form_by_user_and_survey(user_id, survey_type, db)

        if not data:
            raise HTTPException(status_code=404, detail='Not found')

        if self.two_min_breathing:
            data.two_min_breathing = datetime.utcnow().isoformat()
            db.commit()
            db.refresh(data)

        return {
            "Two min breathing added!"
        }



class UserProfile(BaseModel):
    gender: str
    date_of_birth: str
    weight_kg: str
    height_cm: str
    blood_group: str
    chronic_condition: str
    major_illness: str
    allergies: str
    medication_allergies: str
    hospitalization_history: str
    daily_calorie_goal: int
    diet_type: str
    activity_level: str
    water_intake_goal_liters: float


class PlanRequest(BaseModel):
    current_date: str
    current_day: str
    user_profile: UserProfile