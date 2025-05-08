from flask import Flask, render_template, request
from chatbot import LegalChatbot

app = Flask(__name__)
bot = LegalChatbot("data/legal_data.csv")

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    mode = None
    if request.method == "POST":
        query = request.form["query"]
        mode = request.form["mode"]
        if mode == "search":
            response = bot.get_case_match(query)
        elif mode == "ai":
            response = bot.get_ai_advice(query)
    return render_template("index.html", response=response, mode=mode)

if __name__ == "__main__":
    app.run(debug=True)
