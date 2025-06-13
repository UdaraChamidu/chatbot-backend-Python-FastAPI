import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.prompts.chat import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()  # Loads environment variables from a .env file

# Set up the LLM with your OpenAI API key from environment variables
llm = ChatOpenAI(
    model_name='gpt-3.5-turbo',
    temperature=0
)

# Create prompt templates
def create_prompt_with_history():
    return ChatPromptTemplate.from_messages([
        SystemMessage(content="You are an intelligent chatbot. Answer the following questions."),
        MessagesPlaceholder(variable_name="history"),
        MessagesPlaceholder(variable_name="question")
    ])

# Function to get response from LLM
def get_response(history, question):
    prompt = create_prompt_with_history()
    # Prepare input for prompt
    inputs = {
        "history": history,
        "question": [HumanMessage(content=question)]
    }
    # Format the messages for the model
    messages = prompt.format_messages(**inputs)
    # Call the LLM with formatted messages
    response = llm.invoke(messages)
    return response.content

# Example usage with chat history
if __name__ == "__main__":
    history = [
        HumanMessage(content="My name is Udara ... "),
        AIMessage(content="Nice to meet you, Udara! How can I assist you today?"),
        HumanMessage(content="What is 2+2?"),
        AIMessage(content="4")
    ]

    question = "Who am I?"
    answer = get_response(history, question)
    print(answer)

    # Add the latest Q&A to history
    history.extend([HumanMessage(content=question), AIMessage(content=answer)])

    question2 = "What was my last question?"
    answer2 = get_response(history, question2)
    print(answer2)
