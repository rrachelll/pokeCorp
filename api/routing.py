from flask import Flask, Response, request
import json
from dal import create

app = Flask(__name__, static_url_path='', static_folder='dist')



@app.route('/findOwnersPokemon/<trainer>')
def find_owners(trainer):
    try:
        return json.dumps(read.find_owners(trainer))
    except Exception as e:
        return e,400


@app.route('/findTrainerOfPokamon/<name_pokemon>')
def trainers_of_pokemon(name_pokemon):
    try :
        return json.dumps(read.find_trainer_of_pokamon(name_pokemon))
    except Exception as e :
        return e ,400

pokemon["id"]
@app.route('/findPokamonByType/<type_pokemon>')
def Get_pokemon_by_type(type_pokemon):
    try:
        return json.dumps(read.pokemons_by_type(type_pokemon))
    except Exception as e :
        return e ,400


@app.route('/add_pokemon', methods=["POST"])
def add():
    try :
        pokemon = request.get_json()
        return create.add_pokemon_to_db(pokemon)
    except Exception as e:
        return e,400

@app.route('/pokemon_of_trainer/<pokemon>/<trainer>', methods=['DELETE'])
def pokemon_of_trainer(pokemon,trainer):
    try:
        delete.delete_pokemon_of_trainer(pokemon,trainer)
        return "Delete '{}' of trainer '{}'".format(pokemon,trainer)
    except Exception as e :
        return e ,400


@app.route('/update_type_pokemon', methods=["PUT"])
def update_type_pokemon():
    try:
        pokemon = request.get_json()
        return  data_update.update_type_pokemon(pokemon)
    except Exception as e:
        return e,400
 

@app.route('/evolve/<pokemon>/<trainer>')
def evolve(pokemon,trainer):
    try:
        evolve_to = evolve_to(pokemon,trainer)
        return evolve_to
    except Exception as e :
        return e ,400





port_number = 4200

if __name__ == '__main__':
    app.run(port=port_number)
