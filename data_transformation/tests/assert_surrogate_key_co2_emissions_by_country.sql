-- co2_emissions_by_country should have primary combination of year and country to be unique.
-- Therefore return records where this isn't true to make the test fail
select
    "YEAR", country, count(*) as cnt
from {{ ref('co2_emissions_by_country' )}}
group by "YEAR", country
having cnt > 1