-- co2_emissions_and_temperatures_by_country should have COUNTRY ,YEAR ,and AVERAGETEMPERATURE combined by '|' in COUNTRY_AVGTEMP_BKEY column
-- Therefore return records where this isn't true to make the test fail

select * from 
    {{ ref('co2_emissions_and_temperatures_by_country' )}} 
     where COUNTRY_AVGTEMP_BKEY != ( coalesce(INITCAP(Country), '') || '||' || "YEAR" || '||' || coalesce(AverageTemperature,0) )