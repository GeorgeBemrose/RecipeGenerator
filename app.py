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
        recipeNameImage, recipe_dict, status_code = lookupRecipeNameImage(ingredient)
        
        return render_template(
            "index.html", recipeNameImage = recipeNameImage, recipe_dict = recipe_dict, status_code = status_code
        )
    else:

        # TODO: Display the entries in the database on index.html
        recipeNameImage = []
        return render_template("index.html", recipeNameImage = recipeNameImage)
    
def lookupRecipeNameImage(ingredient):
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
            recipes_dict = {}
            for recipe in data:
                
                recipes_dict[recipe['id']] = lookupDetail(recipe['id'])
                
            return data, recipes_dict, response.status_code
        return [], [], response.status_code
        
    
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return "Error"


def lookupDetail(recipe_id):
        # Query API
    try:
        url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'

        params = {
            'apiKey': config.api_key
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
       
        return []
        
    
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return "Error"