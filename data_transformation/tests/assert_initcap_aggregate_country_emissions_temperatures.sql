-- aggregate_country_emissions_temperatures should have Country column in initcap format
-- Therefore return records where this isn't true to make the test fail

select * 
    from 
    {{ ref('aggregate_country_emissions_temperatures' )}} 
    where Country  != INITCAP(Country)