from langchain_core.output_parsers import StrOutputParser
from Chatbot.chatbot_prompts import ChatbotPrompts
from Models.models import report_analysis_model
import json

class TitleGenerator:

    def make_chat_title(self, question: str) -> str:
        resp = ChatbotPrompts.title_prompt | report_analysis_model | StrOutputParser()
        out = resp.invoke({"question": question})
        return json.loads(out)

title = TitleGenerator()
question = "give me blood analysis of my report"
output = title.make_chat_title(question)
print(output)
