from flask import Flask, Response, request, render_template
from model import poke_model,trainer_model,owner_model,evolve
#from dal import delete,create,read,update,evolve
from pymysql import IntegrityError
import json

app = Flask(__name__, static_url_path='', static_folder='dist')


@app.route('/pokemons')
def pokemons_by_trainer():
    try:
        ptype = request.args.get("type")
        trainer = request.args.get("trainer")
        pokemons =[]
        if ptype :
            pokemons = poke_model.get_by_type(ptype)
        elif trainer :
            pokemons = poke_model.get(trainer)
        return json.dumps(pokemons,indent=4),200
    except Exception as e:
        return {'ERROR:' :srt(e)},500


@app.route('/trainer')
def trainers_of_pokemon():
    try :
        pokemon = request.args.get("pokemon")
        trainers_of_pokemon = trainer_model.get(pokemon)
        return json.dumps(trainers_of_pokemon,indent=4),200
    except Exception as e :
        return {'ERROR:' :srt(e)},500


@app.route('/owner'  ,methods=["POST"])
def add_owner():
    try :
        owner = request.get_json()
        return owner_model.add(owner),201
    except IntegrityError as e:
            return "IntegrityError: {} ".format(e.args),409
    except Exception as e:
        return e,500


@app.route('/pokemons', methods=["POST"])
def add():
    try :
        pokemon = request.get_json()
        c = poke_model.add(pokemon)
        return c,201
    except IntegrityError as e:
            return "IntegrityError: {} ".format(e.args),409
    except Exception as e:
        return e.args,500

@app.route('/pokemons', methods=['DELETE'])
def pokemon_of_trainer():
    try:
        trainer = request.args.get("trainer")
        pokemon = request.args.get("pokemon")
        return owner_model.delete(trainer,pokemon),202
    except Exception as e :
        return e.args ,500


@app.route('/types', methods=["PUT"])
def update_type_pokemon():
    try:
        pokemon = request.get_json()
        return poke_model.update_type(pokemon),201
    except IntegrityError as e:
            return f"IntegrityError:'{e.args}'",409
    except Exception as e:
        return e,500
 

@app.route('/evolve', methods=["PUT"])
def evolve_pokemon():
    try:
        pokemon = request.args.get("pokemon")
        trainer = request.args.get("trainer")
        evolve_to = evolve.evolve(pokemon,trainer)
        return evolve_to,201
    except ValueError as e:
        return "ValueError : {}".format(e.args),409
    except Exception as e :
        return e ,500



@app.route('/pokemon_image/<id_poke>')
def img_poke(id_poke):
    try:

        #api_img_poke_back="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/{}.png".format(num_poke)
        #api_img_poke = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{}.png".format(num_poke)
        api_img_poke_back,api_img_poke = poke_model.get_imge(id_poke)
        return render_template("poke_imge.html",api_img_poke = api_img_poke,api_img_poke_back = api_img_poke_back)
    except Exception as e :
        return e ,500


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<path:file_path>')
def serve_static_file(file_path):
    return app.send_static_file(file_path)




port_number = 4200

if __name__ == '__main__':
    app.run(port=port_number)
