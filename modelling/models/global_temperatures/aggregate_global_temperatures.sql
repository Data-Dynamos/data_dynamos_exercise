
{{
  config(
    materialized = 'table'
    )
}}

SELECT 
    SUBSTR("Date", 1, 4)::INTEGER AS Year,
    AVG(NULLIF(LandAverageTemperature, '')) AS LandAverageTemperature,
    MAX(NULLIF(LandMaxTemperature, '')) AS LandMaxTemperature,
    MIN(NULLIF(LandMinTemperature, '')) AS LandMinTemperature,
    AVG(NULLIF(LandAndOceanAverageTemperature, '')) AS LandAndOceanAverageTemperature
FROM {{ ref('stg_global_temperatures') }}
GROUP BY Year

