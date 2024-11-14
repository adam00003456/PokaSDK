import random
from src.poka.sdk import PokaSDK

class PokemonGame:
    def __init__(self):
        self.sdk = PokaSDK()
        print("Welcome to the Pokémon Terminal Game!\n")


    def choose_generation(self):
        
        
        generationNumber = self.sdk.poka_generation_general()
        print("\nChoose a Pokémon Generation to explore (1-" + 
              str(len(generationNumber)) + "): ")

        while True:
            try:
                generation = input("Enter generation number: ")
                # Validate generation choice
                if generation.isdigit() and 1 <= int(generation) <= len(generationNumber):
                    return generation
                else:
                    print("Please enter a valid generation number between 1 and " + 
                          str(len(generationNumber)) + ".")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def encounter_pokemon(self, generation=None, offset=None):
        if (generation != None):
            print("\nFetching Pokémon from Generation", generation, "...")

        print("offset", offset)

        # Select a random Pokémon from the chosen generation
        pokemonName = self.sdk.poka_random_pokemon_selector(generation, offset)
        print(f"A wild {pokemonName} appeared!")
        return pokemonName

    def catch_pokemon(self, pokemon_name):
        # Simple random chance to catch
        success = random.choice([True, False])
        if success:
            print(f"Congratulations! You caught {pokemon_name}!")
        else:
            print(f"{pokemon_name} escaped!")

    def play(self):

        # Ask if the user wants to choose a specific generation or see all Pokémon
        # Ask if the user wants to choose a specific generation or see all Pokémon
        choice = input("Do you want to try to catch a Pokémon " + 
                    "from a specific generation (enter 'yes')" +
                    " or catch from all Pokémon (enter 'all')? ").strip().lower()

        if choice == 'yes':
            generation = self.choose_generation()
            pokemon_name = self.encounter_pokemon(generation)

        elif choice == 'all':
            choice = input("Do you want to try catching a Pokémon from a small sample (enter 'yes')" +
                        " for a quicker game or do you want to view all Pokémon (enter 'no')? ").strip().lower()

            if choice == 'yes':
                # Fetch from a random offset ranging from 0 to 1290, in 20 increments
                max_increment = 1290 // 20
                offset = random.randint(0, max_increment) * 20
                pokemon_name = self.encounter_pokemon(offset=offset)  # Pass offset only

            elif choice == 'no':
                # Fetch from all Pokémon
                pokemon_name = self.encounter_pokemon()

            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

        else:
            print("Invalid choice. Please enter 'yes' or 'all'.")
        
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
