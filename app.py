from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get("https://api.lyrics.ovh/v1/artist/title")
data = response.json()
""" song_list = data['results'] """
songs = []
for song in data:
    print(song)
# Route for the home page
""" @app.route("/")
def index():
    
    response = requests.get("https://api.lyrics.ovh/v1/artist/title")
    data = response.json()
    song_list = data['results']
    
    songs = []
    
    for song in songs:
        # Each Pokémon has a URL like "https://pokeapi.co/api/v2/pokemon/1/"
        url = song['url']
        parts = url.strip("/").split("/")
        id = parts[-1]  # The last part of the URL is the Pokémon's ID
        
        # We use the ID to build an image URL.
        image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
        
        characters.append({
            'name': character['name'].capitalize(),
            'id': id,
            'image': image_url
        })
    
    # We tell Flask to show the 'index.html' page and pass the list of Pokémon.
    return render_template("index.html", songs=songs)
 """
# Route for the Pokémon details page
""" @app.route("/pokemon/<int:id>")
def pokemon_detail(id):
    # We get detailed info for a specific Pokémon using its id.
    response = requests.get(f"https://api.disneyapi.dev/character/{id}")
    data = response.json()
    
    # We extract extra details like types, height, weight, and stats.
    types = [t['type']['name'] for t in data['types']]
    height = data.get('height')
    weight = data.get('weight')
    name = data.get('name').capitalize()
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
    
    # Get the Pokémon’s base stats (like hp, attack, defense, etc.)
    stat_names = [stat['stat']['name'] for stat in data['stats']]
    stat_values = [stat['base_stat'] for stat in data['stats']]
    
    # We tell Flask to show the 'pokemon.html' page with all these details.
    return render_template("pokemon.html", pokemon={
        'name': name,
        'id': id,
        'image': image_url,
        'types': types,
        'height': height,
        'weight': weight,
        'stat_names': stat_names,
        'stat_values': stat_values
    })

if __name__ == '__main__':
    app.run(debug=True) """