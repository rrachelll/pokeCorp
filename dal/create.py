from connect_db import connection
from data_update import update_type_pokemon
from pymysql import IntegrityError


def add_pokemon_to_db(pokemon):
    try:
        with connection.cursor() as cursor:
            insert_pokemon_query = """INSERT into pokemon (name, height,weight) values ( '{}', {},{})
                    """.format(pokemon["name"],pokemon["height"],pokemon["weight"])
            cursor.execute(insert_pokemon_query)
            connection.commit() 
            update_type_pokemon(pokemon)            
    except IntegrityError as e:
        return f"IntegrityError:'{e.args}'",500
    except Exception as e:
        return e,500
