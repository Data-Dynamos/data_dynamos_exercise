import pandas as pd
import os

# File paths (update as needed)
emissions_input_csv_path = "../processed_output/co2_emissions_by_country.csv"
temperatures_input_csv_path = "../processed_output/aggregate_country_temperatures.csv"
output_csv_path = "../processed_output/co2_emissions_and_temperatures_by_country.csv"

# Read the emissions and temperatures data
emissions_df = pd.read_csv(emissions_input_csv_path)
temperatures_df = pd.read_csv(temperatures_input_csv_path)

# Capitalize 'Country' column for consistency in matching
emissions_df['Country'] = emissions_df['Country'].str.title()
temperatures_df['Country'] = temperatures_df['Country'].str.title()

# Merge the data on 'Country' and 'Year' using an INNER JOIN
merged_df = pd.merge(emissions_df, temperatures_df, on=['Country', 'Year'], how='inner')

# Create the 'Country_AvgTemp_BKey' column with the required format
merged_df['Country_AvgTemp_BKey'] = (
    merged_df['Country'].fillna('') + '||' +
    merged_df['Year'].astype(str) + '||' +
    merged_df['AverageTemperature'].fillna(0).astype(str)
)

# Select the required columns: Country_AvgTemp_BKey, Year, Country, TotalEmissions, PerCapitaEmissions, ShareOfGlobalEmissions, AverageTemperature
result_df = merged_df[['Country_AvgTemp_BKey', 'Year', 'Country', 'TotalEmissions', 'PerCapitaEmissions', 'ShareOfGlobalEmissions', 'AverageTemperature']]

# Save the result to the output CSV file
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
result_df.to_csv(output_csv_path, index=False)

print(f"CO2 emissions and temperatures by country saved to: {output_csv_path}")
