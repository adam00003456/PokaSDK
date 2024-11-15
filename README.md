![download](https://github.com/user-attachments/assets/12f058e1-9ac2-48db-ae41-6994d3b50342)

# PokaSDK

PokaSDK is a Python SDK for interacting with the [Pokémon API](https://pokeapi.co/docs/v2), offering methods to retrieve Pokémon data by generation, name, or ID. It includes `exampleGame`, a sample game to demonstrate the SDK’s features.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/adam00003456/PokaSDK.git
   cd PokaSDK
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Tools Used

This project uses the following tools:

- **Hatch**: A modern Python project manager (version 1.7.0 or later recommended). It is used for running tests and managing the project environment.
- **pytest**: A framework for running tests.

Ensure that these tools are installed for smooth operation and testing.

## Usage

The SDK provides methods to interact with the Pokémon API:

- **`poka_generation_general()`**: Fetch paginated Pokémon generations.
- **`poka_generation_specific(idOrName)`**: Retrieve a generation by ID or name.
- **`poka_pokemon(idOrName)`**: Retrieve a specific Pokémon by ID or name.
- **`poka_random_pokemon_selector()`**: Randomly select a Pokémon, optionally by generation.

Example:

```python
from poka_sdk import PokaSDK
sdk = PokaSDK()
print(sdk.poka_generation_specific("generation-i"))
```

## Running `exampleGame`

Run `exampleGame.py` to see the SDK in action:

```bash
python exampleGame.py
```

This script showcases basic SDK usage by randomly selecting and interacting with Pokémon data.

## Modifying the SDK

Activate the `.venv` virtual environment to make and test changes without affecting the global Python setup. Restart or reload the environment after edits for the changes to take effect.

## Testing

1. **Install Testing Tools**

   ```bash
   pip install hatch pytest
   ```

2. **Run Tests Verbosely**
   ```bash
   hatch test -v
   ```

For more detailed output, use `-vv` with `hatch`.

## Design Decisions

Due to pagination with the APIs, I decided to allow for the user to be able to
fetch all data from an API by default unless an offset parameter is provided.

Also, in order to keep the number of SDK class methods to a mininum I used optional
parameters.

## License

This project is licensed under the MIT License. See LICENSE for details.
