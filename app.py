from flask import Flask, render_template, request
import requests
import csv
import config
import json

# Configure application
app = Flask(__name__, template_folder ='template')

@app.route("/", methods=["GET", "POST"])
def index():
    """Homepage"""
    if request.method == "POST":
        ingredient = request.form.get("ingredient")
        recipe = lookup(ingredient)
        return render_template(
            "index.html", recipe = recipe
        )
    else:

        # TODO: Display the entries in the database on index.html
        recipe = []
        return render_template("index.html", recipe = recipe)
    
def lookup(ingredient):
    """Look up energy Gen"""
    

        # Query API
    try:
        url = f'https://api.spoonacular.com/recipes/findByIngredients'

        params = {
            'apiKey': config.api_key,
            'ingredients': ingredient,
            'number': 5,
            "ignorePantry":"false",
            "ranking":"1"
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        return []
        
    
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return "Error"

    




