{{
  config(
    materialized = 'table'
    )
}}

SELECT 
  year(to_timestamp("DATE", 'MM-dd-yyyy')) AS Year,
  AVG(CAST(NULLIF (REGEXP_REPLACE(REPLACE(AVERAGETEMPERATURE, '( ͡° ͜ʖ ͡°)', ''), '[-#?()\\s]+', ''),'')AS FLOAT)) AS AVERAGETEMPERATURE,
  INITCAP(COUNTRY) AS COUNTRY
FROM {{ ref('stg_temperatures_by_country') }}
group by COUNTRY,Year