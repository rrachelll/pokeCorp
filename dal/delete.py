from .connect_db import connection
from .read import get_id_trainer_by_name,get_id_pokemon_by_name

def delete_pokemon_of_trainer(trainer_name,pokemon_name):
        with connection.cursor() as cursor:
            trainer_id = get_id_trainer_by_name(trainer_name)
            pokemon_id = get_id_pokemon_by_name(pokemon_name)
            delete_pokemon_query = """DELETE FROM owned
                                      WHERE owned.id_trainer = {} and owned.id_pokemon = {} 
                    """.format(trainer_id,pokemon_id)
            cursor.execute(delete_pokemon_query)
        connection.commit()
        return "deleted" 