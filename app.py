from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")


from flask import Flask, render_template, request

app = Flask(__name__)

# Store messages in memory
chat_history = []

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.form["message"]
        chat_history.append({"role": "user", "text": user_message})

        # Dummy bot reply logic
        if "fire" in user_message.lower():
            bot_reply = "🔥 Wildfires are tracked using remote sensing and BA products."
        else:
            bot_reply = "🤖 I'm a simple chatbot. Ask me about geoinformatics!"

        chat_history.append({"role": "bot", "text": bot_reply})

    return render_template("chat.html", messages=chat_history)
