# etl-nyc-taxi-airflow
End-to-End ETL pipeline for NYC Taxi data using Apache Airflow and PostgreSQL
# NYC Taxi Data ETL Pipeline 

An end-to-end ETL pipeline to extract, clean, and load NYC Yellow Taxi trip data using:

- **Apache Parquet** files
- **Python (pandas, SQLAlchemy)**
- **PostgreSQL** in Docker
- **Adminer** as the DB GUI

## Project Structure
etl-nyc-taxi-airflow/
├── data/ # Raw data (Parquet format)
├── dags/ # (Optional) Airflow DAGs
├── scripts/
│ ├── extract.py # Reads Parquet data
│ ├── transform.py # Cleans and filters data
│ └── load.py # Loads data to PostgreSQL
├── docker-compose.yml # Spins up Postgres + Adminer
├── requirements.txt # Python packages used
└── README.md
## � How to Run

1. Clone the repo, dataset is huge so download it at https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page, under 2025,march :  Yellow Taxi Trip Records (PARQUET) 
2. Install Python requirements  
3. Start containers:  
   `docker-compose up -d`  
4. Run the ETL scripts:  
   `python3 scripts/extract.py`  
   `python3 scripts/transform.py`  
   `python3 scripts/load.py`

##  Output

Check your data in Adminer:  
[http://localhost:8080](http://localhost:8080)  
- System: PostgreSQL  
- Server: `postgres`  
- User: `airflow`  
- Password: `airflow`  
- DB: `nyc_taxi`



