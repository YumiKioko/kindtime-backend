from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import insert_mood, get_moods

router = APIRouter(prefix='/moods', tags=['moods'])

class MoodEntry(BaseModel):
    user_id: str
    mood: str
    meta: dict | None = None

@router.post('/add')
async def add_mood(entry: MoodEntry):
    if not entry.user_id or not entry.mood:
        raise HTTPException(status_code=400, detail='user_id and mood required')
    resp = insert_mood(entry.user_id, entry.mood, entry.meta)
    return {'status': 'ok', 'result': resp.data if hasattr(resp, 'data') else resp}

@router.get('/{user_id}')
async def list_moods(user_id: str, limit: int = 50):
    resp = get_moods(user_id, limit)
    return {'status': 'ok', 'result': resp.data if hasattr(resp, 'data') else resp}
