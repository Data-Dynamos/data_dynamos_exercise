-- aggregate_global_temperatures should have year column in the format of YYYY
-- Therefore return records where this isn't true to make the test fail
select
    *
from {{ ref('aggregate_global_temperatures' )}}
where length("YEAR") != 4