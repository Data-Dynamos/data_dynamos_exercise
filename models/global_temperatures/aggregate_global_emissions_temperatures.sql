
{{
  config(
    materialized = 'table'
    )
}}

{# 
To analyze the relationship between global emissions and temperatures, you will perform an INNER JOIN between the results of two views: aggregate_global_emissions and aggregate_global_temperatures. This join will combine the data from both views based on the common "Year" column.

To create a table called aggregate_global_emissions_temperatures with the desired columns in the global_temperatures schema:

Perform an INNER JOIN between the aggregate_global_emissions and aggregate_global_temperatures views on the "Year" column.
Select the following columns from the joined data:
Year: Integer
TotalEmissions: Float
LandAverageTemperature: Float
LandMaxTemperature: Float
LandMinTemperature: Float
LandAndOceanAverageTemperature: Float
Your output table, aggregate_global_emissions_temperatures , should have the above schema.
 #}