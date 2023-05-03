
{{
  config(
    materialized = 'table'
    )
}}

select
 em.Year,
 em.TotalEmissions,
 temp.LandAverageTemperature,
 temp.LandMaxTemperature,
 temp.LandMinTemperature,
 temp.LandAndOceanAverageTemperature
from {{ ref('aggregate_global_emissions') }} em inner join  {{ ref('aggregate_global_temperatures') }}  temp on
em.Year = temp.Year

