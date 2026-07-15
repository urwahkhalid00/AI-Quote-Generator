from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    Response,
    jsonify
)
import csv
import io
from database import (
    create_database,
    save_favorite,
    get_favorites,
    delete_favorite,
    quote_exists,
    search_favorites,
    filter_favorites
)

# import os
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

        try:

            response = requests.get(url, timeout=10)

            response.raise_for_status()

            data = response.json()

            quote = data[0]["q"]

            author = data[0]["a"]

        except requests.exceptions.RequestException:

           quote = "Unable to fetch a quote at the moment. Please try again in a few moments."
           author = ""

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

       flash("Quote saved successfully!", "success")

    else:

       flash("This quote is already in your favorites.", "warning")

    return redirect(url_for("favorites"))

@app.route("/get_quote", methods=["POST"])
def get_quote():

    url = "https://zenquotes.io/api/random"

    response = requests.get(url)

    data = response.json()

    return jsonify({

        "quote": data[0]["q"],

        "author": data[0]["a"]

    })

@app.route("/favorites")
def favorites():

    search = request.args.get("search", "")

    category = request.args.get("category", "all")

    quotes = filter_favorites(search, category)

    return render_template(

        "favorites.html",

        quotes=quotes,

        search=search,

        category=category,

        categories=categories
    )


@app.route("/export")
def export():

    quotes = get_favorites()

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(["Quote", "Author", "Category"])

    for quote in quotes:

        writer.writerow([

            quote[1],
            quote[2],
            quote[3]

        ])

    csv_data = output.getvalue()

    output.close()

    return Response(

        csv_data,

        mimetype="text/csv",

        headers={

            "Content-Disposition":
            "attachment; filename=favorites.csv"

        }

    )
    
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    delete_favorite(id)

    return redirect(url_for("favorites"))   
    
if __name__ == "__main__":

    create_database()

    app.run(debug=True)


# if __name__ == "__main__":

#     print(os.path.abspath("quotes.db"))

#     create_database()

#     app.run(debug=True)