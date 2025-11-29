import logging
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import json

from Models.models import chatbot_model, report_analysis_model
from utils.utils import HealthReportUtils
from Chatbot.chatbot_prompts import ChatbotPrompts

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Chatbot:
    def __init__(self, chatbot_type: str, history_msgs: list, user_id: int = None, ):
        self.chatbot_type = chatbot_type
        self.user_id = user_id
        self.utils = HealthReportUtils()
        self.vector_store = None
        self.history_msgs = history_msgs
        self.messages = None


    def initialize_report_qa(self):
        try:
            logger.info("QA system initialized successfully")
            return True
        except Exception as e:
            logger.error(f"Error initializing QA system: {str(e)}")
            return False

    def ask_question(self, question: str, survey, report_text) -> str:
        try:   
            self.messages = []

            self.messages.append(SystemMessage(
                 content=ChatbotPrompts.REPORT_QA_PROMPT["system"].format(survey=survey, report_text=report_text)
             ))


            if not self.history_msgs:
            # If chat history is empty, only append the current query
                self.messages.append(HumanMessage(content=question))

            else:
                # If there is previous history, append it first
                for entry in self.history_msgs:
                    if entry["role"] == "user":
                        self.messages.append(HumanMessage(content=entry["content"]))
                    elif entry["role"] == "assistant":
                        self.messages.append(AIMessage(content=entry["content"]))
                
                self.messages.append(HumanMessage(content=question))
                

            full_response = ""
            for chunk in chatbot_model.stream(self.messages):
                content = chunk.content or ""
                # print(content, end="", flush=True)
                full_response += content
                
            return full_response

        except Exception as e:
            logger.error(f"Error processing question: {str(e)}")
            raise



    def start_interactive_session(self, user_input, survey, report_text=None):
        try:
            self.messages = []

            if self.chatbot_type in {"lab", "dna"}:

                answer = self.ask_question(
                    user_input, survey, report_text
                )

                return {
                    "status": "success",
                    "answer": answer,
                    "chatbot_type": self.chatbot_type
                }


            elif self.chatbot_type == "workout":
                    
                self.messages.append(SystemMessage(
                    content=ChatbotPrompts.WORKOUT_PROMPT["system"].format(qna=survey)
                ))


                if not self.history_msgs:
                # If chat history is empty, only append the current query
                    self.messages.append(HumanMessage(content=user_input))

                else:
                    # If there is previous history, append it first
                    for entry in self.history_msgs:
                        if entry["role"] == "user":
                            self.messages.append(HumanMessage(content=entry["content"]))
                        elif entry["role"] == "assistant":
                            self.messages.append(AIMessage(content=entry["content"]))
                    
                    # Then add the latest user query as the next message
                    self.messages.append(HumanMessage(content=user_input))
                    # print("----------------------------------", self.messages)


            elif self.chatbot_type == "nutrition":
                    
                self.messages.append(SystemMessage(
                    content=ChatbotPrompts.NUTRITION_PROMPT["system"].format(qna=survey)
                ))


                if not self.history_msgs:
                # If chat history is empty, only append the current query
                    self.messages.append(HumanMessage(content=user_input))

                else:
                    # If there is previous history, append it first
                    for entry in self.history_msgs:
                        if entry["role"] == "user":
                            self.messages.append(HumanMessage(content=entry["content"]))
                        elif entry["role"] == "assistant":
                            self.messages.append(AIMessage(content=entry["content"]))
                    
                    # Then add the latest user query as the next message
                    self.messages.append(HumanMessage(content=user_input))
                    # print("----------------------------------", self.messages)



            else:
                    
                self.messages.append(SystemMessage(
                    content=ChatbotPrompts.THERAPIST_PROMPT["system"].format(qna=survey)
                ))


                if not self.history_msgs:
                # If chat history is empty, only append the current query
                    self.messages.append(HumanMessage(content=user_input))

                else:
                    # If there is previous history, append it first
                    for entry in self.history_msgs:
                        if entry["role"] == "user":
                            self.messages.append(HumanMessage(content=entry["content"]))
                        elif entry["role"] == "assistant":
                            self.messages.append(AIMessage(content=entry["content"]))
                    
                    # Then add the latest user query as the next message
                    self.messages.append(HumanMessage(content=user_input))
                    # print("----------------------------------", self.messages)



            answer = ""
            for chunk in chatbot_model.stream(self.messages):
                content = chunk.content or ""
                # print(content, end="", flush=True)
                answer += content

            # print(answer)
            return {
                "status": "success",
                "answer": answer,
                "chatbot_type": self.chatbot_type
            }

        except Exception as e:
            logger.error(f"Error in interactive session: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "chatbot_type": self.chatbot_type
            }











































































# import logging
# from langchain.schema import SystemMessage, HumanMessage, AIMessage
# import json

# from Models.models import chatbot_model, report_analysis_model
# from utils.utils import HealthReportUtils
# from Chatbot.chatbot_prompts import ChatbotPrompts

# # Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
# logger = logging.getLogger(__name__)


# class Chatbot:
#     def __init__(self, chatbot_type: str, history_msgs: list, user_id: int = None, ):
#         self.chatbot_type = chatbot_type
#         self.user_id = user_id
#         self.utils = HealthReportUtils()
#         self.vector_store = None
#         self.history_msgs = history_msgs
#         self.messages = None


#     def initialize_report_qa(self):
#         try:
#             logger.info("QA system initialized successfully")
#             return True
#         except Exception as e:
#             logger.error(f"Error initializing QA system: {str(e)}")
#             return False

#     def ask_question(self, question: str, pinecone_retrive_data: str) -> str:
#         try:   
#             self.messages = []

#             self.messages.append(SystemMessage(
#                  content=ChatbotPrompts.REPORT_QA_PROMPT["system"].format(pinecone_retrive_data=pinecone_retrive_data)
#              ))


#             if not self.history_msgs:
#             # If chat history is empty, only append the current query
#                 self.messages.append(HumanMessage(content=question))

#             else:
#                 # If there is previous history, append it first
#                 for entry in self.history_msgs:
#                     if entry["role"] == "user":
#                         self.messages.append(HumanMessage(content=entry["content"]))
#                     elif entry["role"] == "assistant":
#                         self.messages.append(AIMessage(content=entry["content"]))
                
#                 # Then add the latest user query as the next message
#                 # self.messages.append(HumanMessage(
#                 #     content=ChatbotPrompts.REPORT_QA_PROMPT["human"].format(
#                 #         context=pinecone_retrive_data,
#                 #         question=question
#                 #     )
#                 # ))
#                 self.messages.append(HumanMessage(content=question))
                

#             full_response = ""
#             for chunk in chatbot_model.stream(self.messages):
#                 content = chunk.content or ""
#                 # print(content, end="", flush=True)
#                 full_response += content
                
#             return full_response

#         except Exception as e:
#             logger.error(f"Error processing question: {str(e)}")
#             raise



#     def start_interactive_session(self, user_input, survey):
#         try:
#             self.messages = []

#             if self.chatbot_type in {"lab", "dna"}:
#                 analyzer_prompt = ChatbotPrompts.query_analyzer.format(user_input=user_input)
#                 result = report_analysis_model.invoke(analyzer_prompt)
#                 print("::::::::::::::::::::::;", result)
#                 parsed_result = json.loads(result.content)

#                 if parsed_result["vector_db"] == "True":

#                     pinecone_retrive_data = self.utils.retrieve_data_from_pinecone(
#                         user_input, self.user_id, self.chatbot_type
#                     )

#                     answer = self.ask_question(
#                         user_input, pinecone_retrive_data
#                     )

#                 else:
#                     answer = self.ask_question(
#                         user_input, pinecone_retrive_data = ""
#                     )

#                 return {
#                     "status": "success",
#                     "answer": answer,
#                     "chatbot_type": self.chatbot_type
#                 }


#             elif self.chatbot_type == "workout":
                    
#                 self.messages.append(SystemMessage(
#                     content=ChatbotPrompts.WORKOUT_PROMPT["system"].format(qna=survey)
#                 ))


#                 if not self.history_msgs:
#                 # If chat history is empty, only append the current query
#                     self.messages.append(HumanMessage(content=user_input))

#                 else:
#                     # If there is previous history, append it first
#                     for entry in self.history_msgs:
#                         if entry["role"] == "user":
#                             self.messages.append(HumanMessage(content=entry["content"]))
#                         elif entry["role"] == "assistant":
#                             self.messages.append(AIMessage(content=entry["content"]))
                    
#                     # Then add the latest user query as the next message
#                     self.messages.append(HumanMessage(content=user_input))
#                     # print("----------------------------------", self.messages)


#             elif self.chatbot_type == "nutrition":
                    
#                 self.messages.append(SystemMessage(
#                     content=ChatbotPrompts.NUTRITION_PROMPT["system"].format(qna=survey)
#                 ))


#                 if not self.history_msgs:
#                 # If chat history is empty, only append the current query
#                     self.messages.append(HumanMessage(content=user_input))

#                 else:
#                     # If there is previous history, append it first
#                     for entry in self.history_msgs:
#                         if entry["role"] == "user":
#                             self.messages.append(HumanMessage(content=entry["content"]))
#                         elif entry["role"] == "assistant":
#                             self.messages.append(AIMessage(content=entry["content"]))
                    
#                     # Then add the latest user query as the next message
#                     self.messages.append(HumanMessage(content=user_input))
#                     # print("----------------------------------", self.messages)



#             else:
                    
#                 self.messages.append(SystemMessage(
#                     content=ChatbotPrompts.THERAPIST_PROMPT["system"].format(qna=survey)
#                 ))


#                 if not self.history_msgs:
#                 # If chat history is empty, only append the current query
#                     self.messages.append(HumanMessage(content=user_input))

#                 else:
#                     # If there is previous history, append it first
#                     for entry in self.history_msgs:
#                         if entry["role"] == "user":
#                             self.messages.append(HumanMessage(content=entry["content"]))
#                         elif entry["role"] == "assistant":
#                             self.messages.append(AIMessage(content=entry["content"]))
                    
#                     # Then add the latest user query as the next message
#                     self.messages.append(HumanMessage(content=user_input))
#                     # print("----------------------------------", self.messages)



#             answer = ""
#             for chunk in chatbot_model.stream(self.messages):
#                 content = chunk.content or ""
#                 # print(content, end="", flush=True)
#                 answer += content

#             # print(answer)
#             return {
#                 "status": "success",
#                 "answer": answer,
#                 "chatbot_type": self.chatbot_type
#             }

#         except Exception as e:
#             logger.error(f"Error in interactive session: {str(e)}")
#             return {
#                 "status": "error",
#                 "error": str(e),
#                 "chatbot_type": self.chatbot_type
#             }
















