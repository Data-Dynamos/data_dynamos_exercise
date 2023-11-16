CREATE TABLE carbon_emissions.co2_emissions_and_temperatures_by_country as (
SELECT
  coalesce(INITCAP(em.Country), '')||'||'||em.Year||'||'|| coalesce(temp.AverageTemperature,0) as Country_AvgTemp_BKey,
  em.Year,
  INITCAP(em.Country) as Country,
  em.TotalEmissions,
  em.PerCapitaEmissions,
  em.ShareOfGlobalEmissions,
  temp.AverageTemperature
FROM
 "CARBON_EMISSIONS"."CO2_EMISSIONS_BY_COUNTRY" em 
  INNER JOIN "GLOBAL_TEMPERATURES"."AGGREGATE_COUNTRY_TEMPERATURES"  temp
    ON  INITCAP(em.Country) = INITCAP(temp.Country) AND em.Year = temp.year);