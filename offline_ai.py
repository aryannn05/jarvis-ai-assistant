import subprocess

SYSTEM_PROMPT = """
You are Jarvis, an AI assistant created by Mister Aryan Sharma.
Never mention Microsoft, Phi, OpenAI, or being a model.
If asked who you are, say:
'I am Jarvis, developed by Mister Aryan Sharma.'
"""

def ask_offline(prompt):
    full_prompt = SYSTEM_PROMPT + "\nUser: " + prompt + "\nJarvis:"

    result = subprocess.run(
        ["ollama", "run", "phi3"],
        input=full_prompt,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE
    )

    return result.stdout.strip()
