# chatbot.py
from chatbot_engine import get_response
from langchain.schema import HumanMessage, AIMessage

# Global chat history list, initially empty
history = []

def get_bot_response(user_message: str) -> str:
    global history

    # Append user input to history
    history.append(HumanMessage(content=user_message))

    # Get bot response using full history and current user message
    bot_reply = get_response(history, user_message)

    # Append bot reply to history
    history.append(AIMessage(content=bot_reply))

    return bot_reply
