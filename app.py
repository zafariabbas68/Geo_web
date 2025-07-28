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


@app.route("/explore-map")
def explore_map():
    return render_template("explore_map.html")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_msg = request.form["message"].lower()
        chat_history.append({"role": "user", "text": user_msg})

        # Enhanced response logic
        if any(keyword in user_msg for keyword in ["burn", "fire", "wildfire"]):
            bot_reply = """
            🔥 Based on our analysis of Australian wildfires (2019-2023):
            - Burned areas show seasonal patterns, especially in temperate/tropical biomes
            - FireCCI51 estimates are slightly higher than MODIS MCD64
            - Arid regions show distinct fire patterns with pronounced seasonality
            See our report for detailed visualizations.
            """
        elif any(keyword in user_msg for keyword in ["method", "approach", "analy"]):
            bot_reply = """
            📊 Our methodology includes:
            1. Data collection from VIIRS and MODIS MCD64 via Google Earth Engine
            2. Spatial aggregation by biome/climate zone
            3. Temporal analysis of NDVI patterns
            4. Statistical comparison of datasets
            """
        elif any(keyword in user_msg for keyword in ["ndvi", "vegetation"]):
            bot_reply = """
            🌱 NDVI findings:
            - Clear vegetation recovery patterns post-fire
            - Time-series analysis shows impact duration
            - Correlates with burned area intensity
            Check Figure 5 in our report.
            """
        elif any(keyword in user_msg for keyword in ["help", "support"]):
            bot_reply = """
            ℹ️ I can discuss:
            - Burned area patterns in Australia
            - Dataset comparisons (VIIRS vs MODIS)
            - NDVI analysis
            - Methodology
            Try asking about wildfires or our analysis approach.
            """
        else:
            bot_reply = "🤖 I specialize in geoinformatics and wildfire analysis. Try asking about burned areas in Australia or our methodology."

        chat_history.append({"role": "bot", "text": bot_reply})

    return render_template("chat.html", messages=chat_history)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)