# utils/ai_helper.py

from openai import OpenAI
import os
print("✅ Loaded new ai_helper.py — using OpenAI 2.x client syntax")

# Initialize OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def get_empathic_reply(message, user_context=None):
    """
    Generate a compassionate AI response to the given message.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a kind, calm, and empathic listener. Offer support in a warm, nonjudgmental way."},
            {"role": "user", "content": message}
        ],
        temperature=0.7,
    )

    reply = response.choices[0].message.content
    return {"reply": reply, "crisis": False}
