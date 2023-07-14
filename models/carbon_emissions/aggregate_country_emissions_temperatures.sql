
{{
  config(
    materialized = 'view'
    )
}}

{# In this exercise, you will create a table that combines the results of the co2_emissions_by_country table and the aggregate_country_temperatures table. You will perform an INNER JOIN between these two tables and standardize the country name using the initcap function.

To create the table aggregate_country_emissions_temperatures with the desired columns in the carbon_emissions schema :

Perform an INNER JOIN between the co2_emissions_by_country table and the aggregate_country_temperatures table on the "Year" and "Country" columns.
Use the initcap function to standardize the country name in the "Country" column.


Select the following columns for the output table:

Year: Integer
Country: String
TotalEmissions: Float
PerCapitaEmissions: Float
ShareOfGlobalEmissions: Float
AverageTemperature: Float

 #}
