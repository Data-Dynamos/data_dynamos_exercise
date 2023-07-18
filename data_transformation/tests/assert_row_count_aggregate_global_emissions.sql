-- aggregate_global_emissions should have less than or equal to 270 rows as per dataset given.
-- Therefore return records where this isn't true to make the test fail
select
    count(*) as cnt
from {{ ref('aggregate_global_emissions' )}}
having cnt > 270