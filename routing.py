from flask import Flask, Response, request
import json
from dal import create,delete,read,update

app = Flask(__name__, static_url_path='', static_folder='dist')



@app.route('/Pokemons/<trainer>')
def pokemons_by_traine(trainer):
    try:
        pokemons_by_trainer = read.Get_pokemons_by_trainer(trainer)
        return json.dumps(pokemons_by_trainer[0]),pokemons_by_trainer[1]
    except Exception as e:
        return e,400


@app.route('/pokemons/<name_pokemon>')
def trainers_of_pokemon(name_pokemon):
    try :
        trainers_of_pokemon = read.Get_trainers_of_pokemon(name_pokemon)
        return json.dumps(trainers_of_pokemon[0]),trainers_of_pokemon[1]
    except Exception as e :
        return e ,400



@app.route('/pokemons/<type_pokemon>')
def Get_pokemon_by_type(type_pokemon):
    try:
        pokemon_by_type = read.Get_pokemons_by_type(type_pokemon)
        return json.dumps(pokemon_by_type[0]),pokemon_by_type[1]
    except Exception as e :
        return e ,400


@app.route('/pokemons', methods=["POST"])
def add():
    try :
        pokemon = request.get_json()
#        return create.add_pokemon_to_db(pokemon)
    except Exception as e:
        return e,400

@app.route('/trainer/<pokemon>/<trainer>', methods=['DELETE'])
def pokemon_of_trainer(pokemon,trainer):
    try:
        delete.delete_pokemon_of_trainer(pokemon,trainer)
#       return "Delete '{}' of trainer '{}'".format(pokemon,trainer)
    except Exception as e :
        return e ,400


@app.route('/pokemons', methods=["PUT"])
def update_type_pokemon():
    try:
        pokemon = request.get_json()
#        return  data_update.update_type_pokemon(pokemon)
    except Exception as e:
        return e,400
 

@app.route('/evolve/<pokemon>/<trainer>')
def evolve(pokemon,trainer):
    try:
#        evolve_to = evolve_to(pokemon,trainer)
        return evolve_to
    except Exception as e :
        return e ,400





port_number = 4200

if __name__ == '__main__':
    app.run(port=port_number)
