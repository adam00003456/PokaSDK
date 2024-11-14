import requests
import random

HTTP_TIMEOUT_SECONDS = 10


class PokaSDK:
    def __init__(self):
        pass

    def fetch_paginated_results(self, url, offSet=None):
        results = []

        # Modify the URL with the offset and limit if provided
        if offSet is not None:
            url = f"{url}?offset={offSet}&limit=20"

        # Fetch only one page if an offset is specified
        while url:
            r = requests.get(url, timeout=HTTP_TIMEOUT_SECONDS)
            if r.status_code == 200:
                data = r.json()
                page_results = data.get("results", [])

                if not page_results:
                    print("Warning: No data returned from API.")
                    break

                # Collect results from the current page
                results.extend(page_results)

                # Update URL to the next page only if offset is not specified
                if offSet is None:
                    url = data.get("next")
                else:
                    break  # Stop after the first page if offset is provided

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
        
    
    #Optional offset parameter to fetch a specific offset of paginated results
    def poka_generation_general(self, offSet=None):
        # Calling any API endpoint without a resource ID or name 
        # will return a paginated list of available resources for that API.
        url = f"https://pokeapi.co/api/v2/generation/"
        results = self.fetch_paginated_results(url, offSet)
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
        
     #Optional offSet parameter to fetch a specific offSet of paginated results    
    def poka_pokemon_general(self, offSet=None):
        # Fetch details for a all pokemon with pagination
        # This is the last page: https://pokeapi.co/api/v2/pokemon/?offset=1290&limit=12
        # Note: Calling any API endpoint without a resource ID or name 
        # will return a paginated list of available resources for that API.
        url = f"https://pokeapi.co/api/v2/pokemon/"
        results = self.fetch_paginated_results(url, offSet)
        if results:
            print("Pokémon data retrieved:", results)
        else:
            print("No data found for generations.")
        return results
 
    def poka_random_pokemon_selector(self, generationid=None, offSet=None):
        # Fetch details for a single Pokémon from a specific generation
        # or fetch details for a single Pokémon from all generations
        if generationid == None:
            pokemon_list = self.poka_pokemon_general(offSet)
            # Select a random Pokémon from the list
            encountered_pokemon = random.choice(pokemon_list)
            pokemon_name = encountered_pokemon["name"].capitalize()
            return pokemon_name
        else:
            pokemon_list = self.poka_generation_specific(generationid)

            if not pokemon_list:
                print("No Pokémon found for this generation.")
                return None
            
            pokemon_list = self.pokemonExtractor(pokemon_list)
            # Select a random Pokémon from the list
            encountered_pokemon = random.choice(pokemon_list)
            pokemon_name = encountered_pokemon["name"].capitalize()
            return pokemon_name
    
    def pokemonExtractor(self, generationInfo):
        # Fetch details for a single Pokémon, no pagination
        pokemon_species = generationInfo.get("pokemon_species", [])
        return pokemon_species
    