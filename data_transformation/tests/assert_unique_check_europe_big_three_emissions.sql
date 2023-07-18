-- europe_big_three_emissions should have unique values in year column
-- Therefore return records where this isn't true to make the test fail

select "YEAR",count(*) as cnt from 
    {{ ref('europe_big_three_emissions' )}} 
     group by  1 having cnt > 1