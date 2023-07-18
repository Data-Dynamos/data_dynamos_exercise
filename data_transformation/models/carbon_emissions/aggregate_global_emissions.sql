
{{
  config(
    materialized = 'view'
    )
}}

select
sum(TotalEmissions) as TotalEmissions,
"YEAR" as Year
from {{ ref('co2_emissions_by_country') }} group by "YEAR"

