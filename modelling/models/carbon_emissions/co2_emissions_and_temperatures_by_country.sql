
{{
  config(
    materialized = 'table'
    )
}}

SELECT 
  em.Year,
  em.Country,
  em.TotalEmissions,
  em.PerCapitaEmissions,
  em.ShareOfGlobalEmissions,
  temp.AverageTemperature
FROM
  {{ ref('co2_emissions_by_country') }} em 
  INNER JOIN {{ ref('aggregate_country_temperatures') }} temp
    ON em.COUNTRY = temp.country AND em.Year = temp.year
