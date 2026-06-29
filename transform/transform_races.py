import json
import pandas as pd
from config import PROCESSED_DATA_PATH
from transform.transform_drivers import load_and_fetch

def transform_races():
    races = load_and_fetch("races.json")["RaceTable"]["Races"]

    races_df = pd.DataFrame(races)
    races_df.drop(
        [
            "url",
            "Sprint",
            "SprintQualifying",
            "FirstPractice",
            "SecondPractice",
            "ThirdPractice",
            "Qualifying",
        ],
        axis=1,
        inplace=True,
    )

    # races_df["circuit_id"] = races_df["Circuit"].apply(lambda x: x["circuitId"])
    # races_df["circuit_name"] = races_df["Circuit"].apply(lambda x: x["circuitName"])

    # instead of repeated .apply() use json_normalize()
    circuits = pd.json_normalize(races_df["Circuit"])
    circuits = circuits[
        ["circuitId", "circuitName", "Location.country", "Location.locality"]
    ].rename(
        columns={
            "circuitId": "circuit_id",
            "circuitName": "circuit_name",
            "Location.country": "country",
            "Location.locality": "locality",
        }
    )

    races_df.drop("Circuit", axis=1, inplace=True)

    races_df = pd.concat([races_df, circuits], axis=1)

    races_df["round"] = races_df["round"].astype(int)

    races_df.rename(columns={"raceName": "race_name"}, inplace=True)
    # print(races_df.dtypes)

    races_df.to_csv(f"{PROCESSED_DATA_PATH}/races.csv", index=False)
