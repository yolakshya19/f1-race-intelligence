import requests
from config import BASE_URL, RAW_DATA_PATH, season
import json

def fetch_and_save(endpoint, file_name):
    url = f'{BASE_URL}/{season}/{endpoint}'
    
    # query_params = {'limit': 30}

    data = requests.get(url, timeout=30)
    data.raise_for_status()

    raw_data = data.json()

    with open(f'{RAW_DATA_PATH}/{file_name}', 'w') as file:
        json.dump(raw_data, file, indent=2)

    print(f'{file_name} is saved')
    # logging.info()

fetch_and_save("drivers", "drivers.json")
fetch_and_save("constructors", "constructors.json")
fetch_and_save("results", "results.json")
fetch_and_save("races", "races.json")
