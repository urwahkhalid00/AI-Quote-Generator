from flask import Flask, render_template, request
import requests

app = Flask(__name__)

categories = [
    {"name": "Love", "value": "love"},
    {"name": "Inspirational", "value": "inspirational"},
    {"name": "Success", "value": "success"},
    {"name": "Life", "value": "life"},
    {"name": "Happiness", "value": "happiness"},
    {"name": "Wisdom", "value": "wisdom"}
]

@app.route("/", methods=["GET", "POST"])
def home():

    selected_category = None
    quote = None
    author = None

    if request.method == "POST":

        selected_category = request.form["category"]

        url = f"https://zenquotes.io/api/random"

        response = requests.get(url)

        data = response.json()

        quote = data[0]["q"]
        author = data[0]["a"]

    return render_template(
        "index.html",
        categories=categories,
        quote=quote,
        author=author,
        selected_category=selected_category
    )
if __name__ == "__main__":
    app.run(debug=True)