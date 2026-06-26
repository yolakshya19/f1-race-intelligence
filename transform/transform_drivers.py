import json
import pandas as pd
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH

def load_and_fetch(filename):
    with open(f"{RAW_DATA_PATH}/{filename}", "r") as f:
        data = json.load(f)

    return data["MRData"]


if __name__ == "__main__":  # need t learn about this
    drivers = load_and_fetch("drivers.json")["DriverTable"]["Drivers"]

    drivers_df = pd.DataFrame(drivers)
    drivers_df.fillna("Unknown", inplace=True)

    # print(drivers_df)

    drivers_df.to_csv(f"{PROCESSED_DATA_PATH}/drivers.csv", index=False)
