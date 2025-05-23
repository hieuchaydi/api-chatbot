# app.py
from flask import Flask, render_template, request, jsonify
from chatbot_engine import ChatBot
from stt import listen_and_transcribe

app = Flask(__name__)
bot = ChatBot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("message", "")
    reply = bot.ask(user_input)
    return jsonify({"reply": reply})

@app.route("/listen", methods=["GET"])
def listen():
    text = listen_and_transcribe()
    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(debug=True)
