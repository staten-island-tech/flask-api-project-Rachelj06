from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.spotify.com")
data = response.json()

print(data)


@app.route("/")
def index():
    """ response = requests.get("https://api.spotify.com")
    data = response.json()
    song_list = data['results']
    song = [] """

   