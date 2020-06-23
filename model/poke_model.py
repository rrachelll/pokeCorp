from .connect_db import connection
import requests


def add(pokemon):
        with connection.cursor() as cursor:
            insert_pokemon_query = """INSERT into pokemon (id,name, height,weight,sprites_back_shiny,sprites_front_shiny) values ( {},'{}', {},{},'{}','{}')
                    """.format(pokemon["id"],pokemon["name"],pokemon["height"],pokemon["weight"],pokemon["sprites"]["back_shiny"],pokemon["sprites"]["front_shiny"])
            cursor.execute(insert_pokemon_query)
            connection.commit() 
            update_type = update_type(pokemon) 
            return "inserted pokemon : '{}' and '{}'".format(pokemon['name'],update_type)         


def get(trainer):
    with connection.cursor() as cursor:
        query_select_pokemons_by_trainer = """ SELECT pokemon.name
                FROM PokeCorp.pokemon join PokeCorp.owned join PokeCorp.trainer 
                on pokemon.id = owned.id_pokemon AND trainer.id = owned.id_trainer
                where trainer.name =  '{}'""".format(trainer)
        cursor.execute(query_select_pokemons_by_trainer )
        pokemon_name_same_trainer = cursor.fetchall()
        return [poke["name"] for poke in pokemon_name_same_trainer]


def get_imge(id):
    with connection.cursor() as cursor:
        query_select_imge_pokemon = """ SELECT pokemon.sprites_back_shiny,pokemon.sprites_front_shiny
                                    FROM PokeCorp.pokemon  
                                    where pokemon.id =  '{}'""".format(id)
        cursor.execute(query_select_imge_pokemon )
        pokemon_imge = cursor.fetchone()
        if pokemon_imge["sprites_back_shiny"] is None:
            update_imge(id)
            return get_imge(id)
        return pokemon_imge["sprites_back_shiny"],pokemon_imge["sprites_front_shiny"]



def get_by_type(type_pokemon):
    with connection.cursor() as cursor:
            query_select_pokemons_by_type = """ SELECT pokemon.name
                        FROM PokeCorp.pokemon join PokeCorp.type_pokemon
                        on pokemon.id = type_pokemon.id_pokemon
                        where type_pokemon.name_type = '{}'""".format(type_pokemon)
            cursor.execute(query_select_pokemons_by_type)
            pokemon_name_same_type = cursor.fetchall()
            return [poke["name"] for poke in pokemon_name_same_type]


def get_id_by_name(pokemon_name):
        with connection.cursor() as cursor:
            select_id_by_name_query = """SELECT pokemon.id
                            FROM pokemon
                            WHERE pokemon.name='{}'""".format(pokemon_name)
            cursor.execute(select_id_by_name_query)
            poke_id = cursor.fetchone()
            return 0 if poke_id == None else poke_id["id"] 


def update_type(pokemon):
        with connection.cursor() as cursor:
            poke_url = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon["name"])
            poke = requests.get(url=poke_url)
            poke = poke.json()
            id_poke = get_id_by_name(pokemon["name"])
            for t in poke["types"]:
                    insert_type_pokemon_query = """INSERT into type_pokemon (name_type, id_pokemon) values ('{}', {})
                                            """.format(t["type"]["name"],id_poke)
                    cursor.execute(insert_type_pokemon_query)
                    connection.commit() 
            return "Updated tpyes : " + str([t["type"]["name"] for t in poke["types"]])


def update_imge(id):
    api_img_poke_back="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/{}.png".format(id)
    api_img_poke = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{}.png".format(id)
    with connection.cursor() as cursor:
        insert_imge_pokemon_query = """UPDATE pokemon
                                       SET
                                        sprites_back_shiny = '{}',
                                        sprites_front_shiny = '{}'
                                       WHERE id = {};
                                    """.format(api_img_poke_back,api_img_poke,id)
        cursor.execute(insert_imge_pokemon_query)
        connection.commit()
    return "Updated sprites shiny"
