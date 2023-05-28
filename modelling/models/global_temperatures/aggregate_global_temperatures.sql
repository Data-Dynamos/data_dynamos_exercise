
{{
  config(
    materialized = 'table'
    )
}}

{# Create View for Aggregate Global Temperatures
To analyze temperature measurements globally on an annual basis, you will create a view called aggregate_global_temperatures based on the stg_global_temperatures table in the global_temperatures schema . This view will group the data by year and provide aggregated temperature values using the appropriate aggregation functions.

To create the view and extract the desired columns:

Select the Date, LandAverageTemperature, LandMaxTemperature, LandMinTemperature, and LandAndOceanAverageTemperature columns from the stg_global_temperatures table.
Extract the year from the Date column to obtain only the year portion of the date.
Apply the suitable aggregation functions, such as AVG for average temperature, to calculate the desired values for each year.
Ignore any 'Uncertainty' columns for this project.
The resulting view should have the following columns:

Year: Integer
LandAverageTemperature: Float
LandMaxTemperature: Float
LandMinTemperature: Float
LandAndOceanAverageTemperature: Float
 #}
