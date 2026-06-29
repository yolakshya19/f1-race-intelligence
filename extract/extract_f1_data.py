import json
import requests

from config import BASE_URL, RAW_DATA_PATH, season

TABLE_MAPPING = {
    "drivers": ("DriverTable", "Drivers"),
    "constructors": ("ConstructorTable", "Constructors"),
    "races": ("RaceTable", "Races"),
    "results": ("RaceTable", "Races"),
}


def fetch_and_save(endpoint, file_name, paginate=False):
    url = f"{BASE_URL}/{season}/{endpoint}"

    if not paginate:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        with open(f"{RAW_DATA_PATH}/{file_name}", "w") as file:
            json.dump(response.json(), file, indent=2)

        print(f"{file_name} is saved")
        return

    # Pagination
    table_key, records_key = TABLE_MAPPING[endpoint]

    limit = 100
    offset = 0
    all_records = []
    final_data = None

    while True:
        response = requests.get(
            url,
            params={"limit": limit, "offset": offset},
            timeout=30,
        )
        response.raise_for_status()

        data = response.json()

        if final_data is None:
            final_data = data

        total = int(data["MRData"]["total"])

        records = data["MRData"][table_key][records_key]
        all_records.extend(records)

        offset += limit
        if offset >= total:
            break

    final_data["MRData"][table_key][records_key] = all_records

    with open(f"{RAW_DATA_PATH}/{file_name}", "w") as file:
        json.dump(final_data, file, indent=2)

    print(f"{file_name} is saved")


def extract_data():
    fetch_and_save("drivers", "drivers.json")
    fetch_and_save("constructors", "constructors.json")
    fetch_and_save("races", "races.json")
    fetch_and_save("results", "results.json", paginate=True)
