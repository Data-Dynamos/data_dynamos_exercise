-- aggregate_global_emissions_temperatures should have year column in the format of YYYY
-- Therefore return records where this isn't true to make the test fail
select
    *
from {{ ref('aggregate_global_emissions_temperatures' )}}
where 
TYPEOF(YEAR) != 'INTEGER' or TYPEOF(TOTALEMISSIONS) != 'DOUBLE' 
or TYPEOF(LANDAVERAGETEMPERATURE) != 'DOUBLE' or TYPEOF(LANDMAXTEMPERATURE) != 'DOUBLE'
or TYPEOF(LANDMINTEMPERATURE) != 'DOUBLE' or TYPEOF(LANDANDOCEANAVERAGETEMPERATURE) != 'DOUBLE'