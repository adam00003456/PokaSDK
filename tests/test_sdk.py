import unittest
from src.poka.sdk import PokaSDK

class TestPokaSDKIntegration(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.sdk = PokaSDK()
    
    def test_poka_generation_specific_with_id(self):
        # Test calling the API with an ID
        generation_id = 1  # Known valid generation ID
        response = self.sdk.poka_generation_specific(generation_id)
        
        self.assertIn("pokemon_species", response)
        self.assertGreater(len(response["pokemon_species"]), 0, "No Pokémon species data found.")
        print(f"API response for generation ID {generation_id}:", response)

    def test_poka_generation_specific_with_name(self):
        # Test calling the API with a name
        generation_name = "generation-i"  # Known valid generation name
        response = self.sdk.poka_generation_specific(generation_name)
        
        self.assertIn("pokemon_species", response)
        self.assertGreater(len(response["pokemon_species"]), 0, "No Pokémon species data found.")
        print(f"API response for generation name '{generation_name}':", response)

    def test_invalid_id_or_name(self):
        # Test calling the API with an invalid ID/name
        invalid_id_or_name = "unknown-generation"
        response = self.sdk.poka_generation_specific(invalid_id_or_name)
        
        self.assertEqual(response, {}, "Expected empty dictionary for invalid generation.")
        print(f"API response for invalid ID/name '{invalid_id_or_name}':", response)

if __name__ == "__main__":
    unittest.main()
