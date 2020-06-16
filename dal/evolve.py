from connect_db import connection
from read import select_id_pokemon_by_name
from read import select_id_trainer_by_name

def evolve_to(name_pokemon,name_trainer):
    try :
        poke_url = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon)
        poke = requests.get(url=poke_url)
        poke = poke.json()
        species_url = poke["species"]["url"]
        species_info = requests.get(url=species_url)
        species_info = species_info.json()
        evolution_chain_url = species_info["evolution_chain"]["url"]
        evolution_chain_info = requests.get(url = evolution_chain_url)
        evolution_chain_info = evolution_chain_info.json()
        chain_info = evolution_chain_info["chain"]
        evolves_to = chain_info["evolves_to"]["species"]["name"]
        return f"evolve to '{evolves_to}'",200
    except Exception as e:
        return e,500

"""    Get the info of a specific pokemon.
From the pokemon general info, get the species url.
Get the info of the species, by making a request to the species url
From the species info get the evolution chain url
Get the info of the evolution chain, by making a request to the evolution chain url
From the evolution chain info get the chain item

Scan the chain item in order to find what is the next form of your pokemon. (make sure to cover all cases)
You should end up with the name of the evolved pokemon.
Update the DB accordingly. (think what needs to be updated)"""