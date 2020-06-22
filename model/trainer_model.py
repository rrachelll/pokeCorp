from .connect_db import connection


def get(name_pokemon):
    with connection.cursor() as cursor:
        query_select_trainers_of_pokemon = """ SELECT trainer.name
            FROM PokeCorp.pokemon join PokeCorp.owned join PokeCorp.trainer 
            on pokemon.id = owned.id_pokemon AND trainer.id = owned.id_trainer
            where pokemon.name =  '{}'""".format(name_pokemon)
        cursor.execute(query_select_trainers_of_pokemon)
        trainer_name_same_pokemon = cursor.fetchall()
        return [trainer_name["name"] for trainer_name in trainer_name_same_pokemon]


def get_id_by_name(trainer_name):
    with connection.cursor() as cursor:    
            select_id_by_name_query = """SELECT trainer.id
                            FROM trainer
                            WHERE trainer.name='{}'""".format(trainer_name)
            cursor.execute(select_id_by_name_query)
            trainer_id = cursor.fetchone()
            return trainer_id["id"]


