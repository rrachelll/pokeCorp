from .connect_db import connection
from . import poke_model,trainer_model



def add(owner):
        for id_pokemon in owner ["lits_id_pokemon"]:
                with connection.cursor() as cursor:
                        insert_owned_query =  """INSERT into owned (id_pokemon,id_trainer) values ({},{})
                                """.format(id_pokemon,owner["id_trainer"])
                        cursor.execute(insert_owned_query)
                        connection.commit()
        return "add"


def delete(trainer_name,pokemon_name):
        with connection.cursor() as cursor:
            trainer_id = trainer_model.get_id_by_name(trainer_name)
            pokemon_id = poke_model.get_id_by_name(pokemon_name)
            delete_pokemon_query = """DELETE FROM owned
                                      WHERE owned.id_trainer = {} and owned.id_pokemon = {} 
                    """.format(trainer_id,pokemon_id)
            cursor.execute(delete_pokemon_query)
        connection.commit()
        return "deleted" 


