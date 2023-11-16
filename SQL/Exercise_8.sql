CREATE VIEW carbon_emissions.europe_big_three_emissions as (
WITH TotalEmissionsPivot AS (
  SELECT *
  FROM (
    SELECT Year, Country, TotalEmissions
    FROM "CARBON_EMISSIONS"."CO2_EMISSIONS_AND_TEMPERATURES_BY_COUNTRY"
    WHERE Country IN ('France', 'Germany', 'United Kingdom')
  )
  PIVOT (
    SUM(TotalEmissions) FOR Country IN ('France', 'Germany', 'United Kingdom')
  )
),

PerCapitaEmissionsPivot AS (
  SELECT *
  FROM (
    SELECT Year, Country, PerCapitaEmissions
    FROM "CARBON_EMISSIONS"."CO2_EMISSIONS_AND_TEMPERATURES_BY_COUNTRY"
    WHERE Country IN ('France', 'Germany', 'United Kingdom')
  )
  PIVOT (
    SUM(PerCapitaEmissions) FOR Country IN ('France', 'Germany', 'United Kingdom')
  )
)

SELECT 
  t.Year,
  t."'France'" AS France_TotalEmissions,
  p."'France'" AS France_PerCapitaEmissions,
  t."'Germany'" AS Germany_TotalEmissions,
  p."'Germany'" AS Germany_PerCapitaEmissions,
  t."'United Kingdom'" AS UK_TotalEmissions,
  p."'United Kingdom'" AS UK_PerCapitaEmissions
FROM TotalEmissionsPivot t
JOIN PerCapitaEmissionsPivot p ON t.Year = p.Year);


--- or --- 

CREATE VIEW carbon_emissions.europe_big_three_emissions as (
SELECT 
  DISTINCT
  global.Year,
  france.TotalEmissions AS France_TotalEmissions,
  france.PerCapitaEmissions AS France_PerCapitaEmissions,
  germany.TotalEmissions AS Germany_TotalEmissions,
  germany.PerCapitaEmissions AS Germany_PerCapitaEmissions,
  uk.TotalEmissions AS UK_TotalEmissions,
  uk.PerCapitaEmissions AS UK_PerCapitaEmissions
FROM   
 "CARBON_EMISSIONS"."CO2_EMISSIONS_AND_TEMPERATURES_BY_COUNTRY" global
  LEFT JOIN "CARBON_EMISSIONS"."CO2_EMISSIONS_AND_TEMPERATURES_BY_COUNTRY"  france ON global.Year = france.Year AND france.Country = 'France'
  LEFT JOIN "CARBON_EMISSIONS"."CO2_EMISSIONS_AND_TEMPERATURES_BY_COUNTRY"  germany ON global.Year = germany.Year AND germany.Country = 'Germany'
  LEFT JOIN "CARBON_EMISSIONS"."CO2_EMISSIONS_AND_TEMPERATURES_BY_COUNTRY"  uk ON global.Year = uk.Year AND uk.Country = 'United Kingdom' )