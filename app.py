from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    query = request.args.get("q", "").lower()
    response = requests.get("https://api.deezer.com/chart/0/tracks?limit=100")
    data = response.json()
    track_list = data['data']

    tracks = []
    for track in track_list:
        title = track.get("title", "").lower()
        artist = track.get("artist", {}).get("name", "").lower()

        if query in title or query in artist or query == "":
            tracks.append({
                'id': track['id'],
                'title': track.get('title'),
                'artist': track.get('artist', {}).get('name'),
                'image': track.get('album', {}).get('cover_medium')
            })
            
    showing_all = False
    if query and not tracks:
        showing_all = True
        for track in track_list:
            tracks.append({
                'id': track['id'],
                'title': track['title'],
                'artist': track['artist']['name'],
                'image': track['album']['cover_medium']
            })

    return render_template("index.html", tracks=tracks, query=query, showing_all=showing_all)

@app.route("/track/<int:id>")
def detail(id):
    response = requests.get(f"https://api.deezer.com/track/{id}")
    data = response.json()
    return render_template("detail.html", track=data)

if __name__ == '__main__':
    app.run(debug=True)
