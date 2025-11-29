from celery import Celery
import requests

# Initialize Celery with the broker and backend URLs
celery = Celery("tasks", broker="redis://redis:6379/0", backend="redis://redis:6379/0")

# Django API endpoint to send the message
DJANGO_USER_CHAT_API = "http://localhost:8000/api/user-chats/"

@celery.task
def process_chat_message(message: str, user_id: int, chatbot_type: str, is_encrypted: bool = False):
    """Send the chat response to Django user-chats API."""

    try:
        payload = {
            "user_id": user_id,
            "content": message,
            "is_encrypted": is_encrypted,
            "chatbot_type": chatbot_type
        }

        response = requests.post(DJANGO_USER_CHAT_API, json=payload)

        if response.status_code != 201:
            return f"Failed to post to Django API: {response.status_code} - {response.text}"

        return "Message sent to Django successfully"

    except Exception as e:
        return str(e)
