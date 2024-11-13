import random
import time
from src.poka.sdk import PokaSDK

class PokemonGame:
    def __init__(self):
        self.sdk = PokaSDK()
        print("Welcome to the Pokémon Terminal Game!")

    def choose_generation(self):
        print("\nChoose a Pokémon Generation to explore (1-9): ")
        while True:
            try:
                generation = input("Enter generation number: ")
                # Validate generation choice
                if generation.isdigit() and 1 <= int(generation) <= 9:
                    return generation
                else:
                    print("Please enter a valid generation number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def encounter_pokemon(self, generation):
        print("\nFetching Pokémon from Generation", generation, "...")
        pokemon_list = self.sdk.poka_generation(generation)
        
        if not pokemon_list:
            print("No Pokémon found for this generation.")
            return None

        # Select a random Pokémon from the list
        encountered_pokemon = random.choice(pokemon_list)
        pokemon_name = encountered_pokemon["name"].capitalize()
        print(f"\nA wild {pokemon_name} appeared!")
        return pokemon_name

    def catch_pokemon(self, pokemon_name):
        # Simple random chance to catch
        success = random.choice([True, False])
        if success:
            print(f"Congratulations! You caught {pokemon_name}!")
        else:
            print(f"{pokemon_name} escaped!")

    def play(self):
        generation = self.choose_generation()
        pokemon_name = self.encounter_pokemon(generation)
        
        if pokemon_name:
            # Player action
            action = input(f"\nDo you want to catch {pokemon_name} or run? (catch/run): ").strip().lower()
            if action == "catch":
                self.catch_pokemon(pokemon_name)
            elif action == "run":
                print(f"You ran away from {pokemon_name}!")
            else:
                print("Invalid action. The Pokémon got away!")

if __name__ == "__main__":
    game = PokemonGame()
    game.play()
