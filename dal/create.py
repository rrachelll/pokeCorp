from .update import update_type_pokemon
from .read import get_id_pokemon_by_name,get_id_trainer_by_name
from .connect_db import connection

def add_pokemon_to_db(pokemon):
        with connection.cursor() as cursor:
            insert_pokemon_query = """INSERT into pokemon (id,name, height,weight) values ( {},'{}', {},{})
                    """.format(pokemon["id"],pokemon["name"],pokemon["height"],pokemon["weight"])
            cursor.execute(insert_pokemon_query)
            connection.commit() 
            update_type = update_type_pokemon(pokemon) 
            return "inserted pokemon : '{}' and '{}'".format(pokemon['name'],update_type)         

def add_owner(owner):
        for id_pokemon in owner ["lits_id_pokemon"]:
                with connection.cursor() as cursor:
                        insert_owned_query =  """INSERT into owned (id_pokemon,id_trainer) values ({},{})
                                """.format(id_pokemon,owner["id_trainer"])
                        cursor.execute(insert_owned_query)
                        connection.commit()
        return "add"
