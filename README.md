## PokeCorp
PokeCorp is a company that tracks pokemon and their trainers around the world

## Usage Guide


http://127.0.0.1:4200/
![home](screenshot/home.png "home") 

http://127.0.0.1:4200/types
![1.Update%20pokemon%20types](screenshot/update_type.png "Update pokemon types")
## 

http://127.0.0.1:4200/pokemons
![Add%20new%20pokemon](screenshot/add_pokemon.png "Add new pokemon")
Fields marked in blue are mandatory fields for entry into the DB
## 

http://127.0.0.1:4200/pokemons?type=<p_type>
![Get%20pokemons%20by%20type](screenshot/get_pokemon_by_same_type.png "Get pokemons by type")

## 

http://127.0.0.1:4200/pokemons?trainer=<name_trainer>
![Get%20pokemons%20by%20trainer](screenshot/get_pokemon_by_same_trainer.png "Get pokemons by trainer")

## 

http://127.0.0.1:4200/pokemons?id=<id_pokemon>
![Get%20image%20pokemon](screenshot/imge_poke_25.png "Get image pokemon")

## 

http://127.0.0.1:4200/trainer?pokemon=<name_pokemon>
![Get%20trainers%20of%20a%20pokemon](screenshot/get_trainer_of_pokemon.png "Get imge pokemon")

## 

http://127.0.0.1:4200/evolve?pokemon=<name_pokemon>&trainer=<name_trainer>
![Evolve (pokemon%20x%20of%20trainer%20y)](screenshot/evolve.png "Evolve (pokemon x of trainer y)")

## 

http://127.0.0.1:4200/pokemons?pokemon=<name_pokemon>&trainer=<name_trainer>
![Delete%20pokemon%20of%20trainer](screenshot/deleted_pokemon_of_trainer.png "Delete pokemon of trainer")

## 
http://127.0.0.1:4200/owner
![Add%20list%20pokemon%20to%20trainer](screenshot/add_list_pokemon_to_trainer.png "Add list pokemon to trainer")