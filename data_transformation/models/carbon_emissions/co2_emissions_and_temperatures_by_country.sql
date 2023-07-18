
{{
  config(
    materialized = 'table'
    )
}}

SELECT
  coalesce(INITCAP(em.Country), '')||'||'||em.Year||'||'|| coalesce(temp.AverageTemperature,0) as Country_AvgTemp_BKey,
  em.Year,
  INITCAP(em.Country) as Country,
  em.TotalEmissions,
  em.PerCapitaEmissions,
  em.ShareOfGlobalEmissions,
  temp.AverageTemperature
FROM
  {{ ref('co2_emissions_by_country') }} em 
  INNER JOIN {{ ref('aggregate_country_temperatures') }} temp
    ON  INITCAP(em.Country) = INITCAP(temp.Country) AND em.Year = temp.year
