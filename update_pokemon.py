from connect_db import connection
import requests
def creat_type():
    type_poke_url = 'https://pokeapi.co/api/v2/type'
    type_poke = requests.get(url=type_poke_url)
    type_poke = type_poke.json()

    for t_p in type_poke["results"] :
        with connection.cursor() as cursor:
            insert_type_query= """INSERT into type (name, url) values ('{}', '{}')
            """.format(t_p["name"],t_p["url"])
            cursor.execute(insert_type_query)
    connection.commit() 



print("sucsses")