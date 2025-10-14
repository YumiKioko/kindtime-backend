from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chat, moods
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Kindtime API")

FRONTEND = os.getenv('FRONTEND_ORIGIN', '*')

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND] if FRONTEND != '*' else ['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(moods.router)

@app.get('/')
def root():
    return {"message": "Kindtime API running"}
