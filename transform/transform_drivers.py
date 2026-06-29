import json
import pandas as pd
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH


def load_and_fetch(filename):
    with open(f"{RAW_DATA_PATH}/{filename}", "r") as f:
        data = json.load(f)

    return data["MRData"]


def transform_drivers():
    drivers = load_and_fetch("drivers.json")["DriverTable"]["Drivers"]

    drivers_df = pd.DataFrame(drivers)

    drivers_df.rename(
        columns={
            "driverId": "driver_id",
            "permanentNumber": "permanent_number",
            "givenName": "given_name",
            "familyName": "family_name",
            "dateOfBirth": "date_of_birth",
        },
        inplace=True,
    )

    drivers_df.fillna("Unknown", inplace=True)

    drivers_df["permanent_number"] = pd.to_numeric(
        drivers_df["permanent_number"], errors="coerce"
    ).astype("Int64")
    
    drivers_df.drop(columns=['url'], inplace=True)

    # print(drivers_df)

    drivers_df.to_csv(f"{PROCESSED_DATA_PATH}/drivers.csv", index=False)
