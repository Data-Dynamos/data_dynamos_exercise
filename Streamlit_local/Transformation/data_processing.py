
import pandas as pd
import json
import os

# Define paths
input_path = os.path.join('../../..', 'SQL_Excercise', 'data', 'EMISSIONSBYCOUNTRY.csv')
output_path = os.path.join('../../..', 'output', 'STG_EMISSIONS_BY_COUNTRY.csv')

# Load CSV
df = pd.read_csv(input_path)

# Parse each JSON_STRING into a dict
def safe_parse_json(s):
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        return {}

# Apply JSON parsing
parsed_jsons = df['JSON_STRING'].apply(safe_parse_json)
parsed_df = pd.json_normalize(parsed_jsons)

# Rename columns to match SQL output
column_renames = {
    "Annual CO2 emissions": "Annual_CO2_emissions",
    "Annual CO2 growth (%)": "Annual_CO2_growth_percentage",
    "Annual CO2 growth (abs)": "Annual_CO2_growth_abs",
    "Annual consumption-based CO2 emissions": "Annual_consumption_based_CO2_emissions",
    "CO2 emissions embedded in trade": "CO2_emissions_embedded_in_trade",
    "CO2 emissions from bunkers": "CO2_emissions_from_bunkers",
    "CO2 emissions from cement": "CO2_emissions_from_cement",
    "CO2 emissions from coal": "CO2_emissions_from_coal",
    "CO2 emissions from flaring": "CO2_emissions_from_flaring",
    "CO2 emissions from gas": "CO2_emissions_from_gas",
    "CO2 emissions from oil": "CO2_emissions_from_oil",
    "CO2 emissions from other industry": "CO2_emissions_from_other_industry",
    "CO2 per GDP (kg per $PPP)": "CO2_per_GDP_kg_per_PPP",
    "CO2 per unit energy (kgCO2 per kilowatt-hour)": "CO2_per_unit_energy_kgCO2_per_kilowatt_hour",
    "Cement emissions (per capita)": "Cement_emissions_per_capita",
    "Coal emissions (per capita)": "Coal_emissions_per_capita",
    "Consumption-based CO2 per GDP (kg per $PPP)": "Consumption_based_CO2_per_GDP_kg_per_PPP",
    "Cumulative CO2 emissions": "Cumulative_CO2_emissions",
    "Cumulative cement emissions": "Cumulative_cement_emissions",
    "Cumulative coal emissions": "Cumulative_coal_emissions",
    "Cumulative flaring emissions": "Cumulative_flaring_emissions",
    "Cumulative gas emissions": "Cumulative_gas_emissions",
    "Cumulative oil emissions": "Cumulative_oil_emissions",
    "Cumulative other industry emissions": "Cumulative_other_industry_emissions",
    "Emissions embedded in trade per capita": "Emissions_embedded_in_trade_per_capita",
    "Entity": "Entity",
    "Flaring emissions (per capita)": "Flaring_emissions_per_capita",
    "Gas emissions (per capita)": "Gas_emissions_per_capita",
    "Oil emissions (per capita)": "Oil_emissions_per_capita",
    "Other emissions (per capita)": "Other_emissions_per_capita",
    "Per capita CO2 emissions": "Per_capita_CO2_emissions",
    "Per capita consumption-based CO2 emissions": "Per_capita_consumption_based_CO2_emissions",
    "Share of CO2 emissions embedded in trade": "Share_of_CO2_emissions_embedded_in_trade",
    "Share of global CO2 emissions": "Share_of_global_CO2_emissions",
    "Share of global cement emissions": "Share_of_global_cement_emissions",
    "Share of global coal emissions": "Share_of_global_coal_emissions",
    "Share of global cumulative CO2 emissions": "Share_of_global_cumulative_CO2_emissions",
    "Share of global cumulative cement emissions": "Share_of_global_cumulative_cement_emissions",
    "Share of global cumulative coal emissions": "Share_of_global_cumulative_coal_emissions",
    "Share of global cumulative flaring emissions": "Share_of_global_cumulative_flaring_emissions",
    "Share of global cumulative gas emissions": "Share_of_global_cumulative_gas_emissions",
    "Share of global cumulative oil emissions": "Share_of_global_cumulative_oil_emissions",
    "Share of global flaring emissions": "Share_of_global_flaring_emissions",
    "Share of global gas emissions": "Share_of_global_gas_emissions",
    "Share of global oil emissions": "Share_of_global_oil_emissions",
    "Year": "Year"
}

# Rename columns if they exist
parsed_df.rename(columns=column_renames, inplace=True)

# Append SYS_LOADED_ID if needed
if 'SYS_LOADED_ID' in df.columns:
    parsed_df['SYS_LOADED_ID'] = df['SYS_LOADED_ID']

# Save the parsed output
os.makedirs(os.path.dirname(output_path), exist_ok=True)
parsed_df.to_csv(output_path, index=False)

print(f"✅ Parsed data saved to: {output_path}")
