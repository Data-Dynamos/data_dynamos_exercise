CREATE TABLE  global_temperatures.aggregate_global_emissions_temperatures as (
select
 em.Year,
 em.TotalEmissions,
 temp.LandAverageTemperature,
 temp.LandMaxTemperature,
 temp.LandMinTemperature,
 temp.LandAndOceanAverageTemperature
from "CARBON_EMISSIONS"."AGGREGATE_GLOBAL_EMISSIONS" em inner join "GLOBAL_TEMPERATURES"."AGGREGATE_GLOBAL_TEMPERATURES"  temp on
em.Year = temp.Year);