from .connect_db import connection
from pymysql import ProgrammingError


def get_id_pokemon_by_name(pokemon_name):
        with connection.cursor() as cursor:
            select_id_by_name_query = """SELECT pokemon.id
                            FROM pokemon
                            WHERE pokemon.name='{}'""".format(pokemon_name)
            cursor.execute(select_id_by_name_query)
            poke_id = cursor.fetchone()
            return 0 if poke_id == None else poke_id["id"] 



def get_id_trainer_by_name(trainer_name):
    with connection.cursor() as cursor:    
            select_id_by_name_query = """SELECT trainer.id
                            FROM trainer
                            WHERE trainer.name='{}'""".format(trainer_name)
            cursor.execute(select_id_by_name_query)
            trainer_id = cursor.fetchone()
            return trainer_id["id"]



def get_pokemons_by_type(type_pokemon):
    with connection.cursor() as cursor:
            query_select_pokemons_by_type = """ SELECT pokemon.name
                        FROM PokeCorp.pokemon join PokeCorp.type_pokemon
                        on pokemon.id = type_pokemon.id_pokemon
                        where type_pokemon.name_type = '{}'""".format(type_pokemon)
            cursor.execute(query_select_pokemons_by_type)
            pokemon_name_same_type = cursor.fetchall()
            return [poke["name"] for poke in pokemon_name_same_type]


def get_pokemons(trainer):
    with connection.cursor() as cursor:
        query_select_pokemons_by_trainer = """ SELECT pokemon.name
                FROM PokeCorp.pokemon join PokeCorp.owned join PokeCorp.trainer 
                on pokemon.id = owned.id_pokemon AND trainer.id = owned.id_trainer
                where trainer.name =  '{}'""".format(trainer)
        cursor.execute(query_select_pokemons_by_trainer )
        pokemon_name_same_trainer = cursor.fetchall()
        return [poke["name"] for poke in pokemon_name_same_trainer]


def get_trainers(name_pokemon):
    with connection.cursor() as cursor:
        query_select_trainers_of_pokemon = """ SELECT trainer.name
            FROM PokeCorp.pokemon join PokeCorp.owned join PokeCorp.trainer 
            on pokemon.id = owned.id_pokemon AND trainer.id = owned.id_trainer
            where pokemon.name =  '{}'""".format(name_pokemon)
        cursor.execute(query_select_trainers_of_pokemon)
        trainer_name_same_pokemon = cursor.fetchall()
        return [trainer_name["name"] for trainer_name in trainer_name_same_pokemon]
