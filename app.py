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
        tracks.append(track)
        title = track.get('title')
        artist = track.get(['artist']['name'])
        image = track.get('md5_image')

    return render_template("index.html", tracks=tracks)

if __name__ == '__main__':
    app.run(debug=True)