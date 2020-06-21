from .connect_db import connection
from .read import  get_id_pokemon_by_name,get_id_trainer_by_name,get_pokemons
from .create import add_pokemon_to_db,add_owner
from .delete import delete_pokemon_of_trainer
import requests

def evolve_to(name_pokemon,name_trainer):
        trainers_pokemons = get_pokemons(name_trainer)
        if name_pokemon not in trainers_pokemons:
            raise ValueError(" sorry, {} does not have a {} pokemon ".format(name_trainer,name_pokemon))
        id_pokemon = get_id_pokemon_by_name(name_pokemon)
        
        id_trainer = get_id_trainer_by_name(name_trainer)
        poke_url = "https://pokeapi.co/api/v2/pokemon/{}".format(name_pokemon)
        poke = requests.get(url=poke_url)
        poke = poke.json()
        species_url = poke["species"]["url"]
        species_info = requests.get(url=species_url)
        species_info = species_info.json()
        evolution_chain_url = species_info["evolution_chain"]["url"]
        evolution_chain_info = requests.get(url = evolution_chain_url)
        evolution_chain_info = evolution_chain_info.json()
        chain_info = evolution_chain_info["chain"]
        if chain_info['evolves_to'] == []:
            raise ValueError(" sorry, {} pokemon can not evolve".format(name_pokemon))
        evolves_to = chain_info["evolves_to"][0]["species"]["name"]
        chain_info = chain_info["evolves_to"][0]
        if evolves_to == name_pokemon :
            evolves_to = chain_info["evolves_to"][0]["species"]["name"]
        if evolves_to in trainers_pokemons:
            raise ValueError("Sorry, trainer {} have {} the evolves of {}.".format(name_trainer,evolves_to,name_pokemon))
        id_poke_evolve = get_id_pokemon_by_name(evolves_to)
        if id_poke_evolve == 0:
            pokemon_url = "https://pokeapi.co/api/v2/pokemon/{}".format(evolves_to)
            pokemon = requests.get(pokemon_url)
            pokemon = pokemon.json()
            add_pokemon_to_db(pokemon)
            id_poke_evolve = pokemon["id"]
        delete_pokemon_of_trainer(name_trainer,name_pokemon)
        owner = { 
	                "id_trainer": id_trainer,
	                "lits_id_pokemon": [id_poke_evolve]
                }
        add_owner(owner)
        return "{} should evolve to {}".format(name_pokemon,evolves_to)



