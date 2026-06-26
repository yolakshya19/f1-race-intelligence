import json
import pandas as pd
from config import RAW_DATA_PATH
from pprint import pprint
from transform.transform_drivers import load_and_fetch

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
races_df["circuit_id"] = races_df["Circuit"].apply(lambda x: x["circuitId"])
races_df["circuit_name"] = races_df["Circuit"].apply(lambda x: x["circuitName"])
races_df["country"] = races_df["Circuit"].apply(lambda x: x["Location"]["country"])
races_df["city"] = races_df["Circuit"].apply(lambda x: x["Location"]["locality"])
races_df.drop("Circuit", axis=1, inplace=True)
print(races_df)
