# File: Transformation/aggregate_global_emissions.py

import pandas as pd
import os

# Input file path (update if needed)
input_csv_path = "../processed_output/co2_emissions_by_country.csv"
output_csv_path = "../processed_output/aggregate_global_emissions.csv"

# Read the input CSV
df = pd.read_csv(input_csv_path)

# Ensure 'Year' and 'TotalEmissions' are correct types
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['TotalEmissions'] = pd.to_numeric(df['TotalEmissions'], errors='coerce')

# Group by year and aggregate
df_aggregated = df.groupby('Year', as_index=False).agg({
    'TotalEmissions': 'sum'
})

# Save the result
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
df_aggregated.to_csv(output_csv_path, index=False)
print(f"Aggregated global emissions saved to: {output_csv_path}")
