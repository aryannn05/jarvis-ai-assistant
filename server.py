from flask import Flask, request, jsonify
from brain import smart_brain

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ Jarvis Server Running Successfully!"

@app.route("/jarvis", methods=["POST"])
def jarvis():
    try:
        data = request.get_json(force=True)

        user_text = data.get("text", "")
        print("📩 Phone said:", user_text)

        reply = smart_brain(user_text)

        print("🤖 Jarvis replied:", reply)

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("🚀 Jarvis Server Running at http://127.0.0.1:5000/jarvis")
    app.run(host="0.0.0.0", port=5000)
