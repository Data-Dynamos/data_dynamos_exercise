CREATE TABLE carbon_emissions.co2_emissions_by_country as (
  SELECT
  CAST("Year" AS INTEGER) AS Year,
  ENTITY AS Country,
  CAST(NULLIF(Annual_CO2_emissions, '') AS FLOAT) AS TotalEmissions,
  CAST(NULLIF(Per_capita_CO2_emissions, '') AS FLOAT) AS PerCapitaEmissions,
  CAST(NULLIF(Share_of_global_CO2_emissions, '') AS FLOAT) AS ShareOfGlobalEmissions
FROM "PSA"."STG_EMISSIONS_BY_COUNTRY");

