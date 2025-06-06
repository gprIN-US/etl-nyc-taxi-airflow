import pandas as pd
from sqlalchemy import create_engine
print("[DEBUG] Trying to connect to PostgreSQL...")
print(engine)

def load_data(df):
    """
    Load the cleaned DataFrame into the PostgreSQL database.
    """
    # PostgreSQL connection string (from docker-compose.yml)
    user = "airflow"
    password = "airflow"
    host = "localhost"
    port = "5432"
    db = "nyc_taxi"

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    try:
        df.to_sql("yellow_trips", engine, if_exists="replace", index=False)
        print("[INFO] Data successfully loaded into 'yellow_trips' table.")
    except Exception as e:
        print(f"[ERROR] Failed to load data: {e}")

# For local test
if __name__ == "__main__":
    from transform import transform_data
    df_raw = pd.read_parquet("data/yellow_tripdata_2025-03.parquet")
    df_cleaned = transform_data(df_raw)
    load_data(df_cleaned)
