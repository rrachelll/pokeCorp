from connect_db import connection

def select_id_pokemon_by_name(pokemon_name):
    with connection.cursor() as cursor:
        select_id_by_name_query = """SELECT pokemon.id
                        FROM pokemon
                        WHERE pokemon.name='{}'""".format(pokemon_name)
        cursor.execute(select_id_by_name_query)
        poke_id = cursor.fetchone()
        return poke_id["id"]

def select_id_trainer_by_name(trainer_name):
    with connection.cursor() as cursor:    
        select_id_by_name_query = """SELECT trainer.id
                        FROM trainer
                        WHERE trainer.name='{}'""".format(trainer_name)
        cursor.execute(select_id_by_name_query)
        trainer_id = cursor.fetchone()
        return trainer_id["id"]

def pokemons_by_type(type_pokemon):
    with connection.cursor() as cursor:
        query = """ SELECT pokemon.name
                    FROM PokeCorp.pokemon join PokeCorp.type_pokemon
                    on pokemon.id = type_pokemon.id_pokemon
                    where type_pokemon.name_type = '{}'""".format(type_pokemon)
        cursor.execute(query)
        results = cursor.fetchall()
    return results

def find_owners(trainer):
    with connection.cursor() as cursor:
        query = """ SELECT pokemon.name
            FROM PokeCorp.pokemon join PokeCorp.owned join PokeCorp.trainer 
            on pokemon.id = owned.id_pokemon AND trainer.id = owned.id_trainer
            where trainer.name =  '{}'""".format(trainer)
        cursor.execute(query)
        results = cursor.fetchall()
    return results

def find_trainer_of_pokamon(name_pokemon):
      with connection.cursor() as cursor:
        query = """ SELECT trainer.name
            FROM PokeCorp.pokemon join PokeCorp.owned join PokeCorp.trainer 
            on pokemon.id = owned.id_pokemon AND trainer.id = owned.id_trainer
            where pokemon.name =  '{}'""".format(name_pokemon)
        cursor.execute(query)
        results = cursor.fetchall()
        return results