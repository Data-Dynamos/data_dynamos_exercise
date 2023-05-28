
{{
  config(
    materialized = 'table'
    )
}}

{# 
Create Table for Country Emissions and Average Temperatures
To create a table called co2_emissions_and_temperatures_by_country in the carbon_emissions schema,
you will use the data from the co2_emissions_by_country and aggregate_country_temperatures to analyze and populate the table.

Your output table should contain:
Year: integer
Country: string
TotalEmissions: float
PerCapitaEmissions: float
ShareOfGlobalEmissions: float 
AverageTemperature: float
#}