-- aggregate_country_temperatures should not have leeny face character in AverageTemperature column
-- Therefore return records where this isn't true to make the test fail
select
    *
from {{ ref('aggregate_country_temperatures' )}}
where 
REGEXP_LIKE(AVERAGETEMPERATURE, '.*\\( ͡° ͜ʖ ͡°\\).*')