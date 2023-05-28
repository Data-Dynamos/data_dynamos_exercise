
{{
  config(
    materialized = 'view'
    )
}}

{# In this exercise, you will create a view called aggregate_global_emissions in the carbon_emissions schema. This view will aggregate the total CO2 emissions globally on an annual basis using the data from the co2_emissions_by_country table.

To create the view with the desired columns:

Select the Year column from the co2_emissions_by_country table.
Calculate the sum of TotalEmissions for each year to obtain the total emissions globally.
Assign meaningful aliases to the columns to improve readability and maintain consistency with the desired output table structure.
Store the results in the aggregate_global_emissions view within the carbon_emissions schema.

Your output view should contain:

Year: integer
TotalEmissions:float

 #}


