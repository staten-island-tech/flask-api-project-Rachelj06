from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get("https://api.deezer.com/chart/0/tracks?limit=100")
    data = response.json()
    track_list = data['data']
    tracks = []
    for track in track_list:
        tracks.append(track['title'])

   