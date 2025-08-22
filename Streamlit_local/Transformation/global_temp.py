import pandas as pd
import os
import json

# Update this path if needed
input_csv_path = "../SQL_Excercise/data/GLOBALTEMPERATURES_SAMPLE.csv"
output_csv_path = "../output/STG_GLOBAL_TEMPERATURES.csv"

# Read the raw CSV
df = pd.read_csv(input_csv_path)

# Parse the JSON_STRING column
parsed_rows = []
for json_str in df['JSON_STRING']:
    try:
        parsed = json.loads(json_str)
        parsed_rows.append(parsed)
    except json.JSONDecodeError as e:
        print("Skipping invalid JSON row:", e)
        parsed_rows.append({})

# Convert to DataFrame
parsed_df = pd.DataFrame(parsed_rows)

# Optional: Normalize column names if you want consistency with your SQL
parsed_df.columns = [col.upper().replace(" ", "") for col in parsed_df.columns]

# Create output directory if it doesn't exist
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

# Save the parsed output
parsed_df.to_csv(output_csv_path, index=False)
print(f"Saved parsed output to: {output_csv_path}")
