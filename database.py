import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_mood(user_id: str, mood: str, meta: dict = None):
    payload = {
        'user_id': user_id,
        'mood': mood,
        'meta': meta or {}
    }
    return supabase.table('moods').insert(payload).execute()

def get_moods(user_id: str, limit: int = 50):
    return supabase.table('moods').select('*').eq('user_id', user_id).order('created_at', desc=True).limit(limit).execute()
