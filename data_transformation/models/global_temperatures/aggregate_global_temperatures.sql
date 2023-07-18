
{{
  config(
    materialized = 'table'
    )
}}

SELECT 
    SUBSTR("Date", 1, 4)::INTEGER AS Year,
    AVG(NULLIF(LandAverageTemperature, '')::float) AS LandAverageTemperature,
    MAX(NULLIF(LandMaxTemperature, '')::float) AS LandMaxTemperature,
    MIN(NULLIF(LandMinTemperature, '')::float) AS LandMinTemperature,
    AVG(NULLIF(LandAndOceanAverageTemperature, '')::float) AS LandAndOceanAverageTemperature
FROM {{ source ('psa' , 'stg_global_temperatures')}}
GROUP BY Year

