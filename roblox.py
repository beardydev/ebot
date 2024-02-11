import random
import requests
import re, json

URL = "https://www.rolimons.com/gametable"

def get_random_game():
    page = requests.get(URL)
    games_json = re.search(r'var game_details+ = ({.*})', page.text)

    if games_json:
        games_json = games_json.group(1)
        with open('roblox.json', 'w+') as file:
            # TODO: Fall back to json and cache.
            file.write(str(games_json))

        games = json.loads(games_json)
        game = random.choice(list(games.items()))[1]

        print(game)

        name, genre, thumbnail, *others = game

        return name + ' ' + thumbnail
