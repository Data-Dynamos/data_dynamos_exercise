import pandas as pd
import os

# File paths (update as needed)
input_csv_path = "../processed_output/co2_emissions_and_temperatures_by_country.csv"
output_csv_path = "../processed_output/europe_big_three_emissions.csv"

# Read the CO2 emissions and temperatures data
df = pd.read_csv(input_csv_path)

# Filter data for France, Germany, and United Kingdom
df_europe = df[df['Country'].isin(['France', 'Germany', 'United Kingdom'])]

# Pivot the TotalEmissions data for the selected countries
total_emissions_pivot = df_europe.pivot_table(
    index='Year',
    columns='Country',
    values='TotalEmissions',
    aggfunc='sum'
).reset_index()

# Pivot the PerCapitaEmissions data for the selected countries
per_capita_emissions_pivot = df_europe.pivot_table(
    index='Year',
    columns='Country',
    values='PerCapitaEmissions',
    aggfunc='sum'
).reset_index()

# Merge both pivots on 'Year'
merged_df = pd.merge(
    total_emissions_pivot,
    per_capita_emissions_pivot,
    on='Year',
    suffixes=('_TotalEmissions', '_PerCapitaEmissions')
)

# Rename columns to match the SQL query output format
merged_df = merged_df.rename(columns={
    'France_TotalEmissions': 'France_TotalEmissions',
    'France_PerCapitaEmissions': 'France_PerCapitaEmissions',
    'Germany_TotalEmissions': 'Germany_TotalEmissions',
    'Germany_PerCapitaEmissions': 'Germany_PerCapitaEmissions',
    'United Kingdom_TotalEmissions': 'UK_TotalEmissions',
    'United Kingdom_PerCapitaEmissions': 'UK_PerCapitaEmissions'
})

# Save the result to the output CSV file
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
merged_df.to_csv(output_csv_path, index=False)

print(f"Europe Big Three Emissions data saved to: {output_csv_path}")
