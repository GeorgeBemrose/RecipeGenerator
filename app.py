from flask import Flask, render_template
import requests
import csv
import config

# Configure application
app = Flask(__name__, template_folder ='template')

@app.route("/")
def index():
    """Homepage"""
    output = lookup()
    return render_template(
        "index.html", output = output
    )
    
def lookup():
    """Look up energy Gen"""
    
    headers = {
    'Accept': 'application/json'
    }
    # Query API
    try:
        #r = requests.get('https://api.carbonintensity.org.uk/generation/2023-11-25T00:00Z/2024-01-01T24:00Z', params={}, headers = headers)
        #r = requests.get('https://api.carbonintensity.org.uk/intensity', params={}, headers = headers)


        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

        querystring = {"ingredients":"apples,flour,sugar","number":"5","ignorePantry":"false","ranking":"1"}

        headers = {
            "X-RapidAPI-Key": "config.api_key",
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)


        #mix = list(csv.DictReader(response.content.decode("utf-8").splitlines()))
        return response
    
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return "Error"

    




