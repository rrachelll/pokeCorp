from .connect_db import connection
from .read import select_id_pokemon_by_name
from .read import select_id_trainer_by_name

def delete_pokemon_of_trainer(pokemon_name,trainer_name):
    try:
        with connection.cursor() as cursor:
            poke_id = select_id_pokemon_by_name(pokemon_name) 
            trainer_id = select_id_trainer_by_name(trainer_name)
            delete_pokemon_query = """DELETE FROM owned
                                      WHERE owned.id_pokemon = {} and owned.id_trainer = {}
                    """.format(poke_id,trainer_id)
            cursor.execute(delete_pokemon_query)
        connection.commit()
        return "deleted" ,200 
    except Exception as e:
        return e,500