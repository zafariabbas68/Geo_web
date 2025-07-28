from flask import Flask, render_template, request

app = Flask(__name__)
chat_history = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    @app.route("/explore-map")
    def explore_map():
        return render_template("explore_map.html")

    if request.method == "POST":
        user_msg = request.form["message"]
        chat_history.append({"role": "user", "text": user_msg})
        bot_reply = "🔥 Wildfire data explained!" if "fire" in user_msg.lower() else "🤖 Ask me about geoinformatics."
        chat_history.append({"role": "bot", "text": bot_reply})
    return render_template("chat.html", messages=chat_history)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
