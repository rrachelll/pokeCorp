import requests
from .connect_db import connection
from .read import get_id_pokemon_by_name


def update_type_pokemon(pokemon):
        with connection.cursor() as cursor:
            poke_url = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon["name"])
            poke = requests.get(url=poke_url)
            poke = poke.json()
            id_poke = get_id_pokemon_by_name(pokemon["name"])
            for t in poke["types"]:
                    insert_type_pokemon_query = """INSERT into type_pokemon (name_type, id_pokemon) values ('{}', {})
                                            """.format(t["type"]["name"],id_poke)
                    cursor.execute(insert_type_pokemon_query)
                    connection.commit() 
            return "Updated tpyes : " + str([t["type"]["name"] for t in poke["types"]])


