import json
import pandas as pd
from config import PROCESSED_DATA_PATH
from transform.transform_drivers import load_and_fetch

def transform_constructors():
    constructors = load_and_fetch("constructors.json")["ConstructorTable"][
        "Constructors"
    ]

    constructors_df = pd.DataFrame(constructors)

    constructors_df.drop("url", axis=1, inplace=True)
    constructors_df.rename(columns={"constructorId": "constructor_id"}, inplace=True)

    constructors_df.to_csv(f"{PROCESSED_DATA_PATH}/constructors.csv", index=False)  
