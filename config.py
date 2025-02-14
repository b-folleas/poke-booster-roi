import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration API
API_KEY = os.getenv("POKEMON_TCG_API_KEY")
BASE_URL = "https://api.pokemontcg.io/v2"
HEADERS = {"X-Api-Key": API_KEY}
