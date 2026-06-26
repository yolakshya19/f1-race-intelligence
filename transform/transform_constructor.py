import json
import pandas as pd
from config import RAW_DATA_PATH
from pprint import pprint
from transform.transform_drivers import load_and_fetch

constructors = load_and_fetch("constructors.json")["ConstructorTable"]["Constructors"]

constructors_df = pd.DataFrame(constructors)

print(constructors_df)
