{{
  config(
    materialized = 'table'
    )
}}

{# 
The objective of this exercise is to aggregate temperature measurements per country on an annual basis using the data from the stg_temperatures_by_country source. Additionally, you will need to clean up the "Country" column by removing leading/trailing spaces and converting the country names to the proper format.

To create a table called aggregate_country_temperatures with the desired columns in the global_temperatures schema:

Investigate the data in the stg_temperatures_by_country source for any data quality issues.
Clean up the "Country" column, removing leading/trailing spaces and converting the country names to the proper format using the initcap function.
Remove any occurrences of the Lenny face '( ͡° ͜ʖ ͡°)' from the AverageTemperature column.
Aggregate the temperature measurements per country on an annual basis.
Ignore any 'Uncertainty' columns for this project.

Select the following columns for the output table:

Year: Integer
Country: String
AverageTemperature: Float 

#}