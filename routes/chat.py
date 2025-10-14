from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel
from utils.ai_helper import get_empathic_reply

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    user_id: str | None = None
    message: str

# ✅ Handle browser preflight requests
@router.options("/")
async def options_chat():
    return Response(status_code=200)

@router.post("/")
async def chat(req: ChatRequest):
    if not req.message or len(req.message.strip()) == 0:
        raise HTTPException(status_code=400, detail="Empty message")

    result = await get_empathic_reply(req.message, user_context={"user_id": req.user_id})
    return {
        "reply": result["reply"],
        "crisis": result.get("crisis", False)
    }
