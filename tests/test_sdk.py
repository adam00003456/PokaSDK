import unittest
import responses
from src.poka.sdk import PokaSDK

class TestPokaSDKIntegration(unittest.TestCase):
    def setUp(self):
        # Set up the SDK instance
        print("\nSetting up PokaSDK instance for testing.")
        self.sdk = PokaSDK()

    @responses.activate
    def test_poka_generation(self):
        print("Testing poka_generation with valid generation ID...")
        # Mock the URL for a specific generation with a paginated response
        generation_url = "https://pokeapi.co/api/v2/generation/1/"
        
        #TEST Pokemon name as well as number here

        # Mock first page of results
        responses.add(
            responses.GET,
            generation_url,
            json={
                "results": [{"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"}],
                "next": "https://pokeapi.co/api/v2/generation/1/?page=2",
            },
            status=200,
        )
        
        # Mock second page of results (last page with no `next`)
        responses.add(
            responses.GET,
            "https://pokeapi.co/api/v2/generation/1/?page=2",
            json={
                "results": [{"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"}],
                "next": None,
            },
            status=200,
        )

        # Call the SDK method
        results = self.sdk.poka_generation("1")

        # Output the results to confirm what was returned
        print("Results retrieved:", results)

        # Check that we received both items from the paginated response
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["name"], "bulbasaur")
        self.assertEqual(results[1]["name"], "ivysaur")

    @responses.activate
    def test_invalid_generation(self):
        print("Testing poka_generation with invalid generation ID...")
        # Mock an invalid generation URL
        responses.add(
            responses.GET,
            "https://pokeapi.co/api/v2/generation/invalid_id/",
            json={"detail": "Not found."},
            status=404,
        )

        # Check that an exception is raised with the correct error message
        with self.assertRaises(Exception) as context:
            self.sdk.poka_generation("invalid_id")
        
        # Output the exception message to confirm error handling
        print("Exception message:", str(context.exception))
        
        self.assertIn("Invalid response status code", str(context.exception))

if __name__ == "__main__":
    unittest.main()
