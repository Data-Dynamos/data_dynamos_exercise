# File: Transformation/aggregate_global_emissions_temperatures.py

import pandas as pd
import os

# File paths (update as needed)
emissions_csv_path = "../processed_output/aggregate_global_emissions.csv"
temperatures_csv_path = "../processed_output/aggregate_global_temperatures.csv"
output_csv_path = "../processed_output/aggregate_global_emissions_temperatures.csv"

# Read the emission and temperature data CSVs
emissions_df = pd.read_csv(emissions_csv_path)
temperatures_df = pd.read_csv(temperatures_csv_path)

# Merge emissions and temperature data on the 'Year' column
merged_df = pd.merge(emissions_df, temperatures_df, on='Year', how='inner')

# Save the merged data to a new CSV file
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
merged_df.to_csv(output_csv_path, index=False)

print(f"Aggregated global emissions and temperatures saved to: {output_csv_path}")
