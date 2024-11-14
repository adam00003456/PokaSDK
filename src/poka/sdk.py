import requests
import random

HTTP_TIMEOUT_SECONDS = 10


class PokaSDK:
    def __init__(self):
        pass

    def fetch_paginated_results(self, url):
        results = []
        while url:
            r = requests.get(url, timeout=HTTP_TIMEOUT_SECONDS)
            if r.status_code == 200:
                data = r.json()
                results.extend(data.get("results", []))  # Collect results from the current page
                url = data.get("next")  # Update URL to the next page
            else:
                raise Exception("Invalid response status code: " + str(r.status_code))
        return results

    def poka_generation_specific(self, idOrName):
        # Calling any API endpoint without a resource ID or name 
        # will return a paginated list of available resources for that API.
        url = f"https://pokeapi.co/api/v2/generation/{idOrName}/"
        r = requests.get(url, timeout=HTTP_TIMEOUT_SECONDS)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            print("No data found for this generation.")
            return {}
    
    def poka_generation_general(self):
        # Calling any API endpoint without a resource ID or name 
        # will return a paginated list of available resources for that API.
        url = f"https://pokeapi.co/api/v2/generation/"
        results = self.fetch_paginated_results(url)
        if results:
            print("Pokémon data retrieved:", results)
        else:
            print("No data found for generations.")
        return results

    def poka_pokemon(self, idOrName):
        # Fetch details for a single Pokémon, no pagination
        # Calling any API endpoint without a resource ID or name 
        # will return a paginated list of available resources for that API.
        url = f"https://pokeapi.co/api/v2/pokemon/{idOrName}/"
        r = requests.get(url, timeout=HTTP_TIMEOUT_SECONDS)
        if r.status_code == 200:
            data = r.json()
            print("Pokémon details retrieved:", data)
            return data
        else:
            raise Exception("Invalid response status code: " + str(r.status_code))
        
    def poka_pokemon_general(self):
        # Fetch details for a single Pokémon, no pagination
        # Calling any API endpoint without a resource ID or name 
        # will return a paginated list of available resources for that API.
        url = f"https://pokeapi.co/api/v2/pokemon/"
        r = requests.get(url, timeout=HTTP_TIMEOUT_SECONDS)
        if r.status_code == 200:
            data = r.json()
            print("Pokémon details retrieved:", data)
            return data
        else:
            raise Exception("Invalid response status code: " + str(r.status_code))

    def poka_random_pokemon_selector(self, generationid):
        # Fetch details for a single Pokémon, no pagination
        # Calling any API endpoint without a resource ID or name 
        # will return a paginated list of available resources for that API.
        pokemon_list = self.poka_generation_specific(generationid)
        pokemon_list = self.pokemonExtractor(pokemon_list)
        print("POKEMONZ " + str(pokemon_list))
        # Select a random Pokémon from the list
        encountered_pokemon = random.choice(pokemon_list)
        pokemon_name = encountered_pokemon["name"].capitalize()
        return pokemon_name
    
    def pokemonExtractor(self, generationInfo):
        # Fetch details for a single Pokémon, no pagination
        pokemon_species = generationInfo.get("pokemon_species", [])
        return pokemon_species
    