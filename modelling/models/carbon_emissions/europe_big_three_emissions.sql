
{{
  config(
    materialized = 'view'
    )
}}
 
 
SELECT 
  global.Year,
  france.TotalEmissions AS France_TotalEmissions,
  france.PerCapitaEmissions AS France_PerCapitaEmissions,
  germany.TotalEmissions AS Germany_TotalEmissions,
  germany.PerCapitaEmissions AS Germany_PerCapitaEmissions,
  uk.TotalEmissions AS UK_TotalEmissions,
  uk.PerCapitaEmissions AS UK_PerCapitaEmissions
FROM   
{{ ref('co2_emissions_and_temperatures_by_country') }} global
  JOIN {{ ref('co2_emissions_and_temperatures_by_country') }}  france ON global.Year = france.Year AND france.Country = 'France'
  JOIN {{ ref('co2_emissions_and_temperatures_by_country') }}  germany ON global.Year = germany.Year AND germany.Country = 'Germany'
  JOIN {{ ref('co2_emissions_and_temperatures_by_country') }}  uk ON global.Year = uk.Year AND uk.Country = 'United Kingdom'