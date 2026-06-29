from extract.extract_f1_data import extract_data
from transform.transform_drivers import transform_drivers
from transform.transform_constructor import transform_constructors
from transform.transform_races import transform_races
from transform.transform_results import transform_results
from load.load_f1_data import load_db


def main():
    extract_data()
    transform_drivers()
    transform_constructors()
    transform_races()
    transform_results()
    load_db()


if __name__ == "__main__":
    main()
