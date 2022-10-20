import app
import requests
import json

class Pokemon():
    def __init__(self, sprite, namePokemon, ability, type_primary, type_secondary, weight, height, hp, attack, defense, special_attack, special_defense, speed):
        self.namePokemon = namePokemon
        self.ability = ability
        self.sprite = sprite
        self.type_primary = type_primary
        self.type_secondary = type_secondary
        self.weight = weight
        self.height = height
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed


def findPokeByName(pokeName):
        pokemonName = pokeName.lower()
        request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}")
        data = json.loads(request.content)

        namePokemon = data['name'].capitalize()
        ability = data["abilities"][0]["ability"]["name"]
        spriteData = data['sprites']
        sprite = spriteData['other']['official-artwork']['front_default']
        type_primary = data['types'][0]['type']['name'].capitalize()
        try:
            type_secondary = data['types'][1]['type']['name'].capitalize()
        except:
            type_secondary = "Nothing"
        weight = data['weight']
        height = data['height']
        hp = data['stats'][0]['base_stat']
        attack = data['stats'][1]['base_stat']
        defense = data['stats'][2]['base_stat']
        special_attack = data['stats'][3]['base_stat']
        special_defense = data['stats'][4]['base_stat']
        speed = data['stats'][5]['base_stat']

        pokemon = Pokemon(sprite, namePokemon, ability, type_primary, type_secondary, weight, height, hp, attack, defense, special_attack, special_defense, speed)
        return pokemon