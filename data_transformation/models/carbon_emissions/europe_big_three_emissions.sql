
{{
  config(
    materialized = 'view'
    )
}}
 
 
{#
   Create view for Europe Big Three Emissions

Use the source table co2_emissions_and_temperatures_by_country to create a view for the emissions data of the three major European countries: France, Germany, and the United Kingdom.

To create the view europe_big_three_emissions with the desired columns in the carbon_emissions schema :

Reshape the data to meet the following requirements:

Select the following columns for the output view:

Year: integer
France_TotalEmissions: float
France_PerCapitaEmissions: float
Germany_TotalEmissions: float
Germany_PerCapitaEmissions: float
UnitedKingdom_TotalEmissions: float
UnitedKingdom_PerCapitaEmissions: float
 #}