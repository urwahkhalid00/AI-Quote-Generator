from flask import Flask, render_template, request, redirect, url_for
from database import (
    create_database,
    save_favorite,
    get_favorites,
    delete_favorite,
    quote_exists
)
import requests

app = Flask(__name__)

app.secret_key = "my_secret_key"

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
   
@app.route("/favorite", methods=["POST"])
def favorite():

    quote = request.form["quote"]

    author = request.form["author"]

    category = request.form["category"]

    if not quote_exists(quote):

       save_favorite(quote, author, category)

    return redirect(url_for("favorites"))

@app.route("/favorites")
def favorites():

    quotes = get_favorites()

    return render_template(
        "favorites.html",
        quotes=quotes
    )
    
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    delete_favorite(id)

    return redirect(url_for("favorites"))   
    
if __name__ == "__main__":

    create_database()

    app.run(debug=True)