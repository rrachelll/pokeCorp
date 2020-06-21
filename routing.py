from flask import Flask, Response, request, render_template

from dal import delete,create,read,update,evolve
from pymysql import IntegrityError
app = Flask(__name__, static_url_path='', static_folder='dist')



@app.route('/pokemons')
def pokemons_by_traine():
    try:
        ptype = request.args.get("type")
        trainer = request.args.get("trainer")
        pokemons =[]
        if ptype :
            pokemons = read.get_pokemons_by_type(ptype)
        elif trainer :
            pokemons = read.get_pokemons(trainer)
        return json.dumps(pokemons,indent=4),200
    except Exception as e:
        return {'ERROR:' :srt(e)},500


@app.route('/trainer')
def trainers_of_pokemon():
    try :
        pokemon = request.args.get("pokemon")
        trainers_of_pokemon = read.get_trainers(pokemon)
        return json.dumps(trainers_of_pokemon,indent=4),200
    except Exception as e :
        return {'ERROR:' :srt(e)},500

@app.route('/trainer'  ,methods=["POST"])
def add_owner():
    try :
        owner = request.get_json()
        return create.add_owner(owner),201
    except IntegrityError as e:
            return "IntegrityError: {} ".format(e.args),409
    except Exception as e:
        return e,500


@app.route('/pokemons', methods=["POST"])
def add():
    try :
        pokemon = request.get_json()
        c = create.add_pokemon_to_db(pokemon)
        return c,201
    except IntegrityError as e:
            return "IntegrityError: {} ".format(e.args),409
    except Exception as e:
        return e,500

@app.route('/pokemons', methods=['DELETE'])
def pokemon_of_trainer():
    try:
        trainer = request.args.get("trainer")
        pokemon = request.args.get("pokemon")
        return delete.delete_pokemon_of_trainer(trainer,pokemon),202
    except Exception as e :
        return e ,500


@app.route('/types', methods=["PUT"])
def update_type_pokemon():
    try:
        pokemon = request.get_json()
        return update.update_type_pokemon(pokemon),201
    except IntegrityError as e:
            return f"IntegrityError:'{e.args}'",409
    except Exception as e:
        return e,500
 

@app.route('/evolve', methods=["PUT"])
def evolve_pokemon():
    try:
        pokemon = request.args.get("pokemon")
        trainer = request.args.get("trainer")
        evolve_to = evolve.evolve_to(pokemon,trainer)
        return evolve_to,201
    except ValueError as e:
        return "ValueError : {}".format(e.args),409
    except Exception as e :
        return e ,500



@app.route('/pokemon_image/<num_poke>')
def img_poke(num_poke):
    try:
        api_img_poke_back="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/{}.png".format(num_poke)
        api_img_poke = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{}.png".format(num_poke)
        return render_template("poke_imge.html",api_img_poke = api_img_poke,api_img_poke_back = api_img_poke_back)
    except Exception as e :
        return e ,500


@app.route('/<path:file_path>')
def serve_static_file(file_path):
    return app.send_static_file(file_path)




port_number = 4200

if __name__ == '__main__':
    app.run(port=port_number)
