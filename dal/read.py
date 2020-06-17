from .connect_db import connection
from pymysql import ProgrammingError


def Get_id_pokemon_by_name(pokemon_name):
    try:
        with connection.cursor() as cursor:
            select_id_by_name_query = """SELECT pokemon.id
                            FROM pokemon
                            WHERE pokemon.name='{}'""".format(pokemon_name)
            cursor.execute(select_id_by_name_query)
            poke_id = cursor.fetchone()
            return poke_id["id"]
    except Exception as e:
        return e,500


def Get_id_trainer_by_name(trainer_name):
    try:
        with connection.cursor() as cursor:    
            select_id_by_name_query = """SELECT trainer.id
                            FROM trainer
                            WHERE trainer.name='{}'""".format(trainer_name)
            cursor.execute(select_id_by_name_query)
            trainer_id = cursor.fetchone()
            return trainer_id["id"]
    except Exception as e:
        return e,500


def Get_pokemons_by_type(type_pokemon):
    try: 
        with connection.cursor() as cursor:
            query_select_pokemons_by_type = """ SELECT pokemon.name
                        FROM PokeCorp.pokemon join PokeCorp.type_pokemon
                        on pokemon.id = type_pokemon.id_pokemon
                        where type_pokemon.name_type = '{}'""".format(type_pokemon)
            cursor.execute(query_select_pokemons_by_type)
            pokemon_name_same_type = cursor.fetchall()
        return [poke["name"] for poke in pokemon_name_same_type],200
    except Exception as e:
        return e,500

def Get_pokemons_by_trainer(trainer):
    try :
        with connection.cursor() as cursor:
            query_select_pokemons_by_trainer = """ SELECT pokemon.name
                FROM PokeCorp.pokemon join PokeCorp.owned join PokeCorp.trainer 
                on pokemon.id = owned.id_pokemon AND trainer.id = owned.id_trainer
                where trainer.name =  '{}'""".format(trainer)
            cursor.execute(query_select_pokemons_by_trainer )
            pokemon_name_same_trainer = cursor.fetchall()
            return [poke["name"] for poke in pokemon_name_same_trainer],200
    except  ProgrammingError as p:
        return f"ProgrammingError: '{p.args}'",401
    except Exception as e:
        return e,500

def Get_trainers_of_pokemon(name_pokemon):
    try:
      with connection.cursor() as cursor:
        query_select_trainers_of_pokemon = """ SELECT trainer.name
            FROM PokeCorp.pokemon join PokeCorp.owned join PokeCorp.trainer 
            on pokemon.id = owned.id_pokemon AND trainer.id = owned.id_trainer
            where pokemon.name =  '{}'""".format(name_pokemon)
        cursor.execute(query_select_trainers_of_pokemon)
        trainer_name_same_pokemon = cursor.fetchall()
        return [trainer_name["name"] for trainer_name in trainer_name_same_pokemon],200
    except  ProgrammingError as p:
        return f"ProgrammingError: '{p.args}'",401
    except Exception as e:
        return e,500    