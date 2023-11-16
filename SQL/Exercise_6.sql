CREATE VIEW carbon_emissions.aggregate_country_emissions_temperatures as (
SELECT
  em.Year,
  INITCAP(em.Country) as Country,
  em.TotalEmissions,
  em.PerCapitaEmissions,
  em.ShareOfGlobalEmissions,
  temp.AverageTemperature
FROM
  "CARBON_EMISSIONS"."CO2_EMISSIONS_BY_COUNTRY" AS em
LEFT JOIN
   "GLOBAL_TEMPERATURES"."AGGREGATE_COUNTRY_TEMPERATURES" AS temp
ON
  INITCAP(em.Country) = INITCAP(temp.Country) AND em.Year = temp.Year);