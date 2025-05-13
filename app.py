from flask import Flask, render_template
import requests

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    
    response = requests.get("https://api.spotify.com")
    data = response.json()
    _list = data['results']
    
   