CREATE VIEW carbon_emissions.aggregate_global_emissions AS (
select
sum(TotalEmissions) as TotalEmissions,
"YEAR" as Year
from "CARBON_EMISSIONS"."CO2_EMISSIONS_BY_COUNTRY" group by "YEAR");