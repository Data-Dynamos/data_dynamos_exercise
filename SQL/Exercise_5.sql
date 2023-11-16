CREATE TABLE global_temperatures.aggregate_country_temperatures AS (
SELECT
    year(to_timestamp("DATE", 'MM-dd-yyyy')) AS Year,
    AVG(CAST(NULLIF(REGEXP_REPLACE(REPLACE(AVERAGETEMPERATURE, '( ͡° ͜ʖ ͡°)', ''), '[-#?()\\s]+', ''), '') AS FLOAT)) AS AVERAGETEMPERATURE,
    INITCAP(COUNTRY) AS COUNTRY
FROM psa.stg_temperatures_by_country 
GROUP BY COUNTRY,Year);