from voice import speak
from wake_word import wake_word_detect
from listen_live import listen_live
from brain import smart_brain
from commands import run_command
from memory import load_memory, save_memory

memory = load_memory()

def main():
    speak("Hello sir. I am Jarvis, developed by Mister Aryan Sharma.")

    while True:

        wake_word_detect()
        speak("Yes sir?")

        command = listen_live()

        if command == "":
            continue

        if "shutdown" in command:
            speak("Goodbye sir.")
            break

        # PC Commands
        cmd = run_command(command)
        if cmd:
            speak(cmd)
            continue

        # Memory Example
        if "my name is" in command:
            name = command.replace("my name is", "").strip()
            memory["user_name"] = name
            save_memory(memory)
            speak(f"Noted, sir. Hello {name}.")
            continue

        reply = smart_brain(command)
        speak(reply)

if __name__ == "__main__":
    main()
