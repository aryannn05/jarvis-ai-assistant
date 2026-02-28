import os
import webbrowser

def run_command(text):

    if "open chrome" in text:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        return "Opening Chrome, sir."

    if "open youtube" in text:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube, sir."

    if "open vscode" in text:
        os.system("code")
        return "Opening Visual Studio Code, sir."

    return None
