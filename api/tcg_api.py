import requests
from config import BASE_URL, HEADERS


def get_sets():
    """Get available sets."""
    url = f"{BASE_URL}/sets"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()["data"]
    else:
        print("Error when retrieving sets.")
        return []


def get_cards_from_set(set_id):
    """Get cards from a set (based on set id)."""
    url = f"{BASE_URL}/cards?q=set.id:{set_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()["data"]
    else:
        print("Error when retrieving cards.")
        return []
