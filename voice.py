import asyncio
import edge_tts
import os
from playsound import playsound

VOICE = "en-GB-RyanNeural"

async def speak_async(text):
    file = "jarvis.mp3"
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(file)
    playsound(file)
    os.remove(file)

def speak(text):
    print("Jarvis:", text)
    asyncio.run(speak_async(text))
