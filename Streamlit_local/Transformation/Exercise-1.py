# File: Transformation/emissions_by_country.py

import pandas as pd
import os

# Update this path based on your actual file location
input_csv_path = "../output/STG_EMISSIONS_BY_COUNTRY.csv"
output_csv_path = "../processed_output/co2_emissions_by_country.csv"

# Read input CSV
df = pd.read_csv(input_csv_path)

# Transform data according to the SQL logic
df_transformed = pd.DataFrame({
    "Year": pd.to_numeric(df["Year"], errors="coerce").astype("Int64"),
    "Country": df["Entity"],
    "TotalEmissions": pd.to_numeric(df["Annual_CO2_emissions"], errors="coerce"),
    "PerCapitaEmissions": pd.to_numeric(df["Per_capita_CO2_emissions"], errors="coerce"),
    "ShareOfGlobalEmissions": pd.to_numeric(df["Share_of_global_CO2_emissions"], errors="coerce")
})

# Ensure output directory exists
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

# Save output
df_transformed.to_csv(output_csv_path, index=False)
print(f"Processed file saved to: {output_csv_path}")
