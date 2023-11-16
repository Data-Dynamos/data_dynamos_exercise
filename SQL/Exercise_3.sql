
CREATE TABLE global_temperatures.aggregate_global_temperatures as (
SELECT 
    SUBSTR("Date", 1, 4)::INTEGER AS Year,
    AVG(NULLIF(LandAverageTemperature, '')::float) AS LandAverageTemperature,
    MAX(NULLIF(LandMaxTemperature, '')::float) AS LandMaxTemperature,
    MIN(NULLIF(LandMinTemperature, '')::float) AS LandMinTemperature,
    AVG(NULLIF(LandAndOceanAverageTemperature, '')::float) AS LandAndOceanAverageTemperature
FROM "PSA"."STG_GLOBAL_TEMPERATURES"
GROUP BY Year);