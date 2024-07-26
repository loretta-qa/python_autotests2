import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5a5a35998312646db2ca58f0fe7718a7'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_pokemon = {
    "name": "Barbara",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "45207",
    "name": "Lava",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "45207"
}

response_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon)
print(response_pokemon.text)

pokemon_id =  response_pokemon.json()['id']

response_name = requests.put(url = f'{URL}/pokemons', headers=HEADER, json = body_change)
print(response_name.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_pokeball)
print(response_pokeball.text)