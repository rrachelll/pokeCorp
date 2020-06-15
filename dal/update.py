from connect_db import connection
from read import select_id_pokemon_by_name
import requests
from pymysql import IntegrityError

def update_type_pokemon(pokemon):
    try :
        with connection.cursor() as cursor:
            id_poke = select_id_pokemon_by_name(pokemon["name"])
            poke_url = "https://pokeapi.co/api/v2/pokemon/'{}'/".format(pokemon["name"])
            poke = requests.get(url=poke_url)
            poke = poke.json()
            try:
                for t in poke["types"]:
                    insert_type_pokemon_query = """INSERT into type_pokemon (name_type, id_pokemon) values ('{}', {})
                                            """.format(t["type"]["name"],id_poke)
                    cursor.execute(insert_type_pokemon_query)
                    connection.commit() 
                return "Update",200
            except IntegrityError as e:
                    return f"IntegrityError:'{e.args}'",500
    except Exception as e:
        print (e)
        return "Fails",500
