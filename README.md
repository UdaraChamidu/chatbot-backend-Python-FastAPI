
# ⚙️ Simple Chatbot - Backend

This is the backend of the EyeDoc Chatbot, powered by FastAPI and LangChain. It handles message processing, conversation history, and integrates with OpenAI's language models to generate intelligent replies.

## 🚀 Features

- FastAPI-based REST endpoint (`/chat`)
- CORS-enabled to work with local or deployed frontends
- Uses LangChain + OpenAI API to maintain context and chat history
- Modular architecture for easy integration

## 🧠 Technologies Used

- FastAPI
- LangChain
- OpenAI GPT-3.5 Turbo
- Python 3.11
- dotenv for managing API keys

## 🔐 Environment Variables

Create a `.env` file in the backend root with your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

##A simple chatbot project which created for study the deployment process.

- Create a folder
- Copy and paste the frontend and backend folders
- First run backend part and then run frontend part (same time both are running)
- Install requirements.txt file and give a OpenAI API key

---

### to run, frontend and backend should be in same server.

## To run, 
```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Screenshots
![image](https://github.com/user-attachments/assets/abd2d0d7-2d0a-418b-aab9-b2c8c32fdbd1)
![image](https://github.com/user-attachments/assets/d9bb746c-d69c-4cd8-8c3a-d6fff96a1e6f)


