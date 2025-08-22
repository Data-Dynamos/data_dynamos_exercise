import pandas as pd
import os
import json

# Define input and output paths
input_csv_path = "../SQL_Excercise/data/TEMPERATURESBYCOUNTRY_SAMPLE.csv"
output_csv_path = "../output/STG_TEMPERATURES_BY_COUNTRY.csv"

# Load raw data
df = pd.read_csv(input_csv_path, quotechar='"', escapechar='\\', engine='python', on_bad_lines='skip')

# Parse the JSON_STRING column
parsed_rows = []
for json_str in df['JSON_STRING']:
    try:
        parsed = json.loads(json_str)
        parsed_rows.append({
            "AverageTemperature": parsed.get("AverageTemperature", ""),
            "AverageTemperatureUncertainty": parsed.get("AverageTemperatureUncertainty", ""),
            "Country": parsed.get("Country", ""),
            "Date": parsed.get("Date", "")
        })
    except json.JSONDecodeError as e:
        print("Skipping invalid JSON row:", e)
        parsed_rows.append({
            "AverageTemperature": "",
            "AverageTemperatureUncertainty": "",
            "Country": "",
            "Date": ""
        })

# Convert to DataFrame
parsed_df = pd.DataFrame(parsed_rows)

# Make sure output directory exists
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

# Save parsed data to CSV
parsed_df.to_csv(output_csv_path, index=False)
print(f"Saved parsed output to: {output_csv_path}")
