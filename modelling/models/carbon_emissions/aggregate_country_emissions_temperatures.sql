
{{
  config(
    materialized = 'view'
    )
}}

SELECT
  em.Year,
  INITCAP(em.Country) as Country,
  em.TotalEmissions,
  em.PerCapitaEmissions,
  em.ShareOfGlobalEmissions,
  temp.AverageTemperature
FROM
  {{ ref('co2_emissions_by_country') }} AS em
LEFT JOIN
  {{ ref('aggregate_country_temperatures') }} AS temp
ON
  INITCAP(em.Country) = INITCAP(temp.Country) AND em.Year = temp.Year
