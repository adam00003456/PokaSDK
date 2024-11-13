import requests

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

    def poka_generation(self, idOrName):
        r = "https://pokeapi.co/api/v2/generation/" + idOrName + "/"
        return self.fetch_paginated_results(r)
      
        
    def poka_pokemon(self,idOrName):
        r = "https://pokeapi.co/api/v2/pokemon/" + idOrName + "/"
        return self.fetch_paginated_results(r)