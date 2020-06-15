import requests

type_poke = 'https://pokeapi.co/api/v2/type'
res = requests.get(url=type_poke)
res = res.json()
print([ i["name"] for i in res["results"]] )