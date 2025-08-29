# LAFD Response Time Pipeline

This project processes the [LAFD Response Metrics - Raw Data](https://catalog.data.gov/dataset/lafd-response-metrics-raw-data) dataset (~7M rows) to analyze emergency response times for 2020 incidents. It uses Pandas for ETL, PostgreSQL for storage, SQLAlchemy for database interaction, and Seaborn for visualization.

## About dataset
The Los Angeles Fire Department (LAFD)’s Computer Aided Dispatch (CAD) system is a transactional, event‐driven system that records dates and time stamps based on events triggered by two distinct human interactions: interaction with CAD at the dispatch center via CAD workstation, and interaction with CAD via the Mobile Data Computer (MDC) installed in the responding LAFD unit, communicating with CAD through the LAFD’s Radio Network Controller (RNC).

more informations about raw file structure (https://data.lacity.org/Public-Safety/LAFD-Response-Metrics-Raw-Data/n44u-wxe4/about_data)

## Features
- Filters data for 2020 emergency incidents using `Randomized Incident Number`. (This number is generated with the year and quarter indicator with a six digits randomized number attached, i.e. – 201301345785, this number means it is in the year 2013 in the first quarter.)
- Calculates response times (`On Scene Time - Incident Creation Time`). TBD
- Loads data into PostgreSQL. TBD
- Visualizes average response times by PPE level. TBD

## Requirements
- Python 3.8+
- PostgreSQL
- Dependencies: `requirements.txt`

## Setup
1. Install PostgreSQL: `brew install postgresql`
2. Create database: `psql -U postgres -f sql/create_tables.sql`
3. Install dependencies: `pip install -r requirements.txt`
4. Place `lafd_response_metrics.csv` in `data/`.
5. Update PostgreSQL password in `scripts/etl_pipeline.py`.
6. Run: `python scripts/etl_pipeline.py`

## Output
- PostgreSQL table: 
- Visualization: `visualizations/TBD .png`

## License
CC0 1.0 Universal