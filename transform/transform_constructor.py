import json
import pandas as pd
from config import PROCESSED_DATA_PATH
from transform.transform_drivers import load_and_fetch

constructors = load_and_fetch("constructors.json")["ConstructorTable"]["Constructors"]

constructors_df = pd.DataFrame(constructors)

# print(constructors_df)

constructors_df.to_csv(f'{PROCESSED_DATA_PATH}/constructors.csv', index=False)