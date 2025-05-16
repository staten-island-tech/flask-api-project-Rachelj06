from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.deezer.com/chart/0/tracks?limit=100")
data = response.json()

for track in data['data']:
    print(f"{track['title']} by {track['artist']['name']}")




@app.route("/")
def index():
    """ response = requests.get("")
    data = response.json()
    song_list = data['results']
    song = [] """

   