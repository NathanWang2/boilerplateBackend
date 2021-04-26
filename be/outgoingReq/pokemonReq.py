import requests
from bson.json_util import dumps
from time import process_time

BASE_URL = "https://pokeapi.co/api/v2/"  # Should move this to a env file?


def getPokemonInfo(pokemon: str):
    r = requests.get(BASE_URL + "pokemon/" + pokemon)
    return r.json()


def getAbilities(pokemon_data):

    return pokemon_data["abilities"]


def main():

    start = process_time()
    poke_data = getPokemonInfo("ditto")
    print("Total time for data req: ", process_time() - start)

    start = process_time()
    poke_abilities = getAbilities(poke_data)
    print("Total time for data parse: ", process_time() - start)

    start = process_time()
    requests.get('https://deelay.me/5000/https://picsum.photos/200/300')
    print("Total Github timr: ", process_time() - start)

    print("abilities: ", poke_abilities)
    f = open("test.txt", "w")
    f.write(dumps(poke_abilities, indent=4))
    f.close()


main()
