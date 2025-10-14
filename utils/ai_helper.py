import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

SYSTEM_PROMPT = (
    "You are Kindtime, a compassionate and empathetic conversational companion."
    "Your role is to listen, reflect, and offer gentle, non-judgmental suggestions. "
    "You are NOT a therapist. If the user indicates self-harm or crisis, respond with empathy and advise them to seek professional help or local emergency services, and include the 'I_need_help' token in your JSON response so the caller can route appropriately."
)

async def get_empathic_reply(message: str, user_context: dict = None):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": message}
    ]
    # Basic call: adapt model name in production as needed
    resp = openai.ChatCompletion.create(
        model='gpt-4o-mini',
        messages=messages,
        max_tokens=200,
        temperature=0.7
    )
    text = resp.choices[0].message['content'].strip()
    # Simple heuristic detection for crisis keywords (the AI will also help)
    crisis_tokens = ['suicide', 'kill myself', 'self-harm', 'end my life', 'hurt myself']
    crisis_flag = any(k in message.lower() for k in crisis_tokens)
    return {                'reply': text,                'crisis': crisis_flag            }
