from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chat, moods
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Kindtime API")

FRONTEND = os.getenv("FRONTEND_ORIGIN", "*")

# ✅ Enable CORS globally
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or [FRONTEND] if you prefer
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register your routers *after* CORS middleware
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(moods.router, prefix="/moods", tags=["moods"])

@app.get("/")
def root():
    return {"message": "Kindtime API running"}
