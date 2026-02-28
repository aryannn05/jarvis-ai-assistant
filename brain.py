from openai import OpenAI
from config import OPENAI_API_KEY
from offline_ai import ask_offline

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_gpt(prompt):
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=f"Reply like Jarvis in 1 short human sentence: {prompt}",
            max_output_tokens=80
        )
        return response.output_text
    except:
        return None

def smart_brain(prompt):

    if len(prompt) < 20:
        return ask_offline(prompt)

    gpt = ask_gpt(prompt)
    if gpt:
        return gpt

    return ask_offline(prompt)
