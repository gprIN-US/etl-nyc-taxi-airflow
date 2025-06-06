import pandas as pd

# Define the file path
file_path = "data/yellow_tripdata_2025-03.parquet"

# Read the Parquet file
df = pd.read_parquet(file_path)

# Print the first 5 rows
print(df.head())

