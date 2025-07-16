from flask import Flask, render_template, request, session, redirect, url_for
import openai
from utils.chat_history import save_chat, load_chat

app = Flask(__name__)
app.secret_key = "your_secret_key"  # For session

openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/", methods=["GET", "POST"])
def home():
    if "chat_history" not in session:
        session["chat_history"] = []

    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        session["chat_history"].append({"role": "user", "content": user_input})

        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=session["chat_history"]
            )
            bot_reply = completion.choices[0].message["content"]
            session["chat_history"].append({"role": "assistant", "content": bot_reply})
            response = bot_reply

            # Save chat history
            save_chat(session["chat_history"])
        except Exception as e:
            response = f"Error: {str(e)}"

    return render_template("chat.html", response=response, history=session["chat_history"])

@app.route("/reset")
def reset():
    session.pop("chat_history", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
