import requests

def cat_fact(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response_dict = response.json()
        fact = response_dict["fact"]
    except Exception:
        fact = "Could not fetch cat fact at this time."

    return fact
    