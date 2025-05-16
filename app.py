from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.deezer.com/chart/0/tracks?limit=10")
data = response.json()

for track in data['data']:
    print(track)


@app.route("/")
def index():
    """ response = requests.get("")
    data = response.json()
    song_list = data['results']
    song = [] """

   