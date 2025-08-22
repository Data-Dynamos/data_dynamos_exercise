# File: Transformation/aggregate_country_temperatures.py

import pandas as pd
import os
import re

# File paths (update as needed)
input_csv_path = "../output/STG_TEMPERATURES_BY_COUNTRY.csv"
output_csv_path = "../processed_output/aggregate_country_temperatures.csv"

# Function to clean the temperature data by extracting values inside curly braces and cleaning unwanted characters
def clean_temperature(temp):
    if isinstance(temp, str):
        # Step 1: Remove any unwanted symbols or non-standard characters
        temp = re.sub(r'[^\x00-\x7F]+', '', temp)  # Removes non-ASCII characters
        # Step 2: Extract the number, removing any non-numeric characters
        match = re.search(r'(-?\d+(\.\d+)?)', temp)  # Capture numbers, including floats
        if match:
            return match.group(1)  # Return the first matched number
        else:
            return None
    return temp

# Read the input CSV
df = pd.read_csv(input_csv_path)

# Clean the temperature data
df['AverageTemperature'] = df['AverageTemperature'].apply(clean_temperature)

# Convert 'AverageTemperature' to float (handle missing or invalid values)
df['AverageTemperature'] = pd.to_numeric(df['AverageTemperature'], errors='coerce')

# Convert 'Date' to Year (assuming 'Date' is in MM-dd-yyyy format)
df['Year'] = pd.to_datetime(df['Date'], format='%m-%d-%Y').dt.year

# Capitalize the 'Country' column
df['Country'] = df['Country'].str.title()

# Group by 'Country' and 'Year', and calculate the average temperature
aggregated_df = df.groupby(['Country', 'Year'], as_index=False).agg(
    AverageTemperature=('AverageTemperature', 'mean')
)

# Save the result to the output CSV file
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
aggregated_df.to_csv(output_csv_path, index=False)

print(f"Aggregated country temperatures saved to: {output_csv_path}")
