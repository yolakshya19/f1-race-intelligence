from transform.transform_drivers import load_and_fetch
from pprint import pprint
import pandas as pd
from config import PROCESSED_DATA_PATH

def transform_results():
    races = load_and_fetch("results.json")["RaceTable"]["Races"]

    results = []

    for race in races:
        for result in race["Results"]:
            row = {
                "season": race["season"],
                "round": race["round"],
                "driver_id": result["Driver"]["driverId"],
                "constructor_id": result["Constructor"]["constructorId"],
                "grid": result["grid"],
                "position": result["position"],
                "points": result["points"],
                "laps": result["laps"],
                "status": result["status"],
                "timing": result.get("Time", {}).get("time"),
                "fastest_lap": result.get("FastestLap", {}).get("Time", {}).get("time"),
                "fastest_lap_rank": result.get("FastestLap", {}).get("rank"),
            }

            results.append(row)
    results_df = pd.DataFrame(results)

    results_df = results_df.astype(
        {
            "season": "int",
            "round": "int",
            "grid": "Int64",
            "position": "Int64",
            "points": "Int64",
            "laps": "Int64",
            "fastest_lap_rank": "Int64",
        }
    )

    results_df.drop_duplicates(subset=['season', 'round', 'driver_id'], inplace=True)

    # print(results_df.isna().sum())

    results_df.to_csv(f"{PROCESSED_DATA_PATH}/results.csv", index=False)
