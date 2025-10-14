# Kindtime Backend (Starter)
Lightweight FastAPI backend for the Kindtime app.

Features:
- FastAPI app with CORS enabled
- /chat endpoint wired to OpenAI
- /moods endpoints to store/retrieve mood entries using Supabase
- .env.example for required environment variables
- Ready to run locally and deploy to Render or Railway

Quick start (local):
1. unzip and cd into folder
2. create a virtualenv: python -m venv venv && source venv/bin/activate
3. pip install -r requirements.txt
4. copy .env.example -> .env and fill values (OPENAI_API_KEY, SUPABASE_URL, SUPABASE_KEY)
5. uvicorn main:app --reload --port 8000
