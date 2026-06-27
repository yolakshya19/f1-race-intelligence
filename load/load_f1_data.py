import sqlite3
import pandas as pd

from config import PROCESSED_DATA_PATH

conn = sqlite3.connect("database/f1.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS drivers")

cursor.execute("""
CREATE TABLE IF NOT EXISTS drivers (
    driver_id TEXT PRIMARY KEY,
    permanent_number INTEGER,
    code TEXT,
    given_name TEXT,
    family_name TEXT,
    date_of_birth DATE,
    nationality TEXT
)
""")

drivers_df = pd.read_csv(f"{PROCESSED_DATA_PATH}/drivers.csv")

drivers_df.to_sql("drivers", conn, if_exists="append", index=False)


cursor.execute("DROP TABLE IF EXISTS races")

cursor.execute("""
CREATE TABLE IF NOT EXISTS races (
    season INTEGER,
    round INTEGER,
    race_name TEXT,
    date DATE,
    time TEXT,
    circuit_id TEXT,
    circuit_name TEXT,
    country TEXT,
    locality TEXT,

    PRIMARY KEY (season, round)
)
""")

races_df = pd.read_csv(f"{PROCESSED_DATA_PATH}/races.csv")

races_df.to_sql("races", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("Drivers loaded successfully!")
