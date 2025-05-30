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
        tracks.append({
            'id': track['id'],
            'title': track.get('title'),
            'artist': track.get('artist', {}).get('name'),
            'image': track.get('album', {}).get('cover_medium')
        })

    return render_template("index.html", tracks=tracks)

@app.route("/track/<int:id>")
def detail(id):
    response = requests.get(f"https://api.deezer.com/track/{id}")
    data = response.json()
    return render_template("detail.html", track=data)

if __name__ == '__main__':
    app.run(debug=True)
