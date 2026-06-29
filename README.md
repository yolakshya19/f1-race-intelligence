# 🏎️ F1 Race Intelligence - ETL Pipeline

An end-to-end Data Engineering project that extracts Formula 1 data from the Jolpica (Ergast) API, transforms it into an analytics-friendly data model, and loads it into a SQLite database for SQL analysis and visualization.

---

## Project Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline using Python.

The pipeline:

- Extracts F1 data from the Jolpica API
- Handles API pagination
- Cleans and transforms the raw JSON data
- Creates normalized CSV datasets
- Loads the data into a relational SQLite database
- Enables SQL-based analysis and dashboarding

---

## 🛠️ Tech Stack

<table>
<tr>
<td align="center" width="110">
<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" width="55" height="55"/><br>
<b>Python</b>
</td>

<td align="center" width="110">
<img src="https://github.com/devicons/devicon/blob/master/icons/pandas/pandas-original.svg" width="55" height="55"/><br>
<b>Pandas</b>
</td>

<td align="center" width="110">
<img src="https://github.com/devicons/devicon/blob/master/icons/sqlite/sqlite-original.svg" width="55" height="55"/><br>
<b>SQLite</b>
</td>

<td align="center" width="110">
<img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original.svg" width="55" height="55"/><br>
<b>Git</b>
</td>

<td align="center" width="110">
<img src="https://cdn.simpleicons.org/github/ffffff" width="55" height="55"/><br>
<b>GitHub</b>
</td>

<td align="center" width="110">
<img src="https://github.com/devicons/devicon/blob/master/icons/vscode/vscode-original.svg" width="55" height="55"/><br>
<b>VS Code</b>
</td>
</tr>
</table>

---

## Project Structure

```text
f1-race-intelligence/

│
├── analysis/                  # SQL queries and analysis
│
├── data/
│   ├── raw/                   # Raw API JSON files
│   └── processed/             # Clean CSV files
│
├── database/
│   └── f1.db                  # SQLite database
│
├── extract/
│   └── extract_f1_data.py
│
├── transform/
│   ├── transform_drivers.py
│   ├── transform_constructors.py
│   ├── transform_races.py
│   └── transform_results.py
│
├── load/
│   └── load_f1_data.py
│
├── config.py
├── main.py
└── requirements.txt
```

---

## ETL Pipeline

```
Jolpica API
      │
      ▼
Extract JSON
      │
      ▼
Transform
      │
      ▼
Processed CSV Files
      │
      ▼
SQLite Database
      │
      ▼
SQL Analysis
```

---

## Database Schema

The project follows a simple star schema.

### Drivers

- driver_id (PK)
- permanent_number
- code
- given_name
- family_name
- date_of_birth
- nationality

### Constructors

- constructor_id (PK)
- name
- nationality

### Races

Composite Primary Key

- season
- round

Other columns

- race_name
- date
- circuit_name
- country
- locality

### Results (Fact Table)

Composite Primary Key

- season
- round
- driver_id

Foreign Keys

- driver_id → drivers
- constructor_id → constructors
- (season, round) → races

Race Metrics

- grid
- position
- points
- laps
- status
- timing
- fastest_lap
- fastest_lap_rank

---

## Features

- API pagination support
- Modular ETL architecture
- Data cleaning and preprocessing
- Duplicate removal
- Data type conversion
- Relational database design
- SQL analytics ready

---

## Running the Project

Clone the repository

```bash
git clone <repo-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the complete pipeline

```bash
python main.py
```

The pipeline will:

1. Download raw F1 data
2. Transform the data
3. Generate processed CSV files
4. Load the data into SQLite

---

## Example SQL Analysis

Some example analyses performed on the database:

- Driver Championship Standings
- Constructor Championship Standings
- Average Driver Finish Position
- Points by Constructor
- Driver Performance by Circuit
- Grid Position vs Finish Position

---

## Learning Outcomes

This project helped me understand:

- REST API integration
- Pagination handling
- ETL pipeline design
- Data normalization
- Relational database modeling
- SQLite
- SQL joins and aggregations
- Modular Python project structure

---

## Future Improvements

- PostgreSQL implementation
- Docker support
- Apache Airflow orchestration
- Logging
- Unit testing
- Power BI dashboard
- Incremental data loading
- GitHub Actions for automated pipeline execution

---

## Data Source

Jolpica F1 API (Ergast)

https://api.jolpi.ca/

---

## Author

**Lakshya**
