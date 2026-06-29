import sqlite3
import pandas as pd

from config import PROCESSED_DATA_PATH

def load_db():
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

    print("Drivers loaded successfully!")

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

    print("Races loaded successfully!")

    cursor.execute("DROP TABLE IF EXISTS constructors")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS constructors ( 
            constructor_id text primary key,
            name text,
            nationality text
    )      
    """)

    constructor_df = pd.read_csv(f"{PROCESSED_DATA_PATH}/constructors.csv")

    constructor_df.to_sql("constructors", conn, if_exists="append", index=False)

    print("Constructors loaded successfully")

    cursor.execute("DROP TABLE IF EXISTS results")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        season INTEGER,
        round INTEGER,
        driver_id TEXT,
        constructor_id TEXT,
        grid INTEGER,
        position INTEGER,
        points INTEGER,
        laps INTEGER,
        status TEXT,
        timing TEXT,
        fastest_lap TEXT,
        fastest_lap_rank INTEGER,

        PRIMARY KEY (season, round, driver_id),

        FOREIGN KEY (driver_id)
            REFERENCES drivers(driver_id),

        FOREIGN KEY (constructor_id)
            REFERENCES constructors(constructor_id),

        FOREIGN KEY (season, round)
            REFERENCES races(season, round)
    )
    """)

    results_df = pd.read_csv(f"{PROCESSED_DATA_PATH}/results.csv")

    results_df.to_sql("results", conn, if_exists="append", index=False)

    print("Results loaded successfully")

    conn.commit()
    conn.close()
