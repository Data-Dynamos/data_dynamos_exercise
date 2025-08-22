# File: Transformation/aggregate_global_temperatures.py

import pandas as pd
import os

# Input file path (update if needed)
input_csv_path = "../output/STG_GLOBAL_TEMPERATURES.csv"
output_csv_path = "../processed_output/aggregate_global_temperatures.csv"

# Read the input CSV
df = pd.read_csv(input_csv_path)

# Ensure 'Date' and temperature columns are in the correct types
df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')
df['LANDAVERAGETEMPERATURE'] = pd.to_numeric(df['LANDAVERAGETEMPERATURE'], errors='coerce')
df['LANDMAXTEMPERATURE'] = pd.to_numeric(df['LANDMAXTEMPERATURE'], errors='coerce')
df['LANDMINTEMPERATURE'] = pd.to_numeric(df['LANDMINTEMPERATURE'], errors='coerce')
df['LANDANDOCEANAVERAGETEMPERATURE'] = pd.to_numeric(df['LANDANDOCEANAVERAGETEMPERATURE'], errors='coerce')

# Extract the year from the 'Date' column
df['Year'] = df['DATE'].dt.year

# Group by Year and aggregate the temperatures
df_aggregated = df.groupby('Year', as_index=False).agg({
    'LANDAVERAGETEMPERATURE': 'mean',
    'LANDMAXTEMPERATURE': 'max',
    'LANDMINTEMPERATURE': 'min',
    'LANDANDOCEANAVERAGETEMPERATURE': 'mean'
})

# Save the result to a new CSV file
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
df_aggregated.to_csv(output_csv_path, index=False)
print(f"Aggregated global temperatures saved to: {output_csv_path}")
