from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class ChatMessage(Base):
    __tablename__ = 'app_chatmessage'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    report_type = Column(String, nullable=False)
    chat_bot_type = Column(String, nullable=False)


class ChatHistory(Base):
    __tablename__ = 'app_chathistory'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    chat_id = Column(Integer, nullable=False)
    history_json = Column(JSON, nullable=False)


class AppSurveyModel(Base):
    __tablename__ = 'app_survey'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    created_at = Column(DateTime, nullable=False)
    survey_json = Column(JSON, nullable=False)
    user_id = Column(Integer, nullable=False)
    survey_type = Column(String, nullable=False)
    two_min_breathing = Column(DateTime, nullable=True)


class User(Base):
    __tablename__ = "app_user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    chat_limit = Column(Integer, default=0)
    unlimited_chats = Column(Boolean, default=False)
