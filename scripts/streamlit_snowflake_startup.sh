#!/bin/bash

source $(poetry env info --path)/bin/activate
# Prompt for Snowflake credentials
read -p "Enter the SNOWFLAKE_ACCOUNT (Ex: px17463.ap-south-1.aws): " SNOWFLAKE_ACCOUNT
read -p "Enter the SNOWFLAKE_DATABASE (EXERCISE_CO2_VS_TEMPERATURE): " SNOWFLAKE_DATABASE
read -p "Enter the SNOWFLAKE_USER: " SNOWFLAKE_USER
read -sp "Enter the SNOWFLAKE_PASSWORD: " SNOWFLAKE_PASSWORD
echo

# Export Snowflake credentials as environment variables
export SNOWFLAKE_ACCOUNT="$SNOWFLAKE_ACCOUNT"
export SNOWFLAKE_DATABASE="$SNOWFLAKE_DATABASE"
export SNOWFLAKE_USER="$SNOWFLAKE_USER"
export SNOWFLAKE_PASSWORD="$SNOWFLAKE_PASSWORD"

# Check if streamlit is installed
if ! command -v streamlit >/dev/null 2>&1; then
    echo "Streamlit is not installed. Please install it first."
    exit 1
fi

# Run the Streamlit application
streamlit run data_visualization/DataDynamos.py # should be able to access the UI