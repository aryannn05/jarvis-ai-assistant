import customtkinter as ctk
import requests

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("900x500")
app.title("JARVIS HUD - Aryan Edition")

title = ctk.CTkLabel(app, text="J.A.R.V.I.S", font=("Orbitron", 40))
title.pack(pady=20)

entry = ctk.CTkEntry(app, width=600, placeholder_text="Ask Jarvis...")
entry.pack(pady=10)

output = ctk.CTkTextbox(app, width=800, height=250)
output.pack(pady=20)

def ask_jarvis():
    user_text = entry.get()

    res = requests.post(
        "http://127.0.0.1:5000/jarvis",
        json={"text": user_text}
    )

    reply = res.json()["reply"]

    output.insert("end", f"\nYou: {user_text}\nJarvis: {reply}\n")
    entry.delete(0, "end")

btn = ctk.CTkButton(app, text="Send", command=ask_jarvis)
btn.pack()

app.mainloop()
