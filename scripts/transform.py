def transform_data(df):
    """
    Clean the raw taxi trip DataFrame:
    - Drop null values
    - Remove trips with 0 passengers or 0 distance
    """
    print("[INFO] Before cleaning:", df.shape)
    
    df_cleaned = df.dropna()
    df_cleaned = df_cleaned[
        (df_cleaned["passenger_count"] > 0) &
        (df_cleaned["trip_distance"] > 0)
    ]

    print("[INFO] After cleaning:", df_cleaned.shape)
    return df_cleaned

# For local testing
if __name__ == "__main__":
    import pandas as pd
    df = pd.read_parquet("data/yellow_tripdata_2025-03.parquet")
    transform_data(df)
