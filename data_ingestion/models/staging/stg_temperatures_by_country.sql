{{
  config(
    materialized = 'view'
    )
}}

select 
PARSE_JSON(JSON_STRING):"AverageTemperature":: VARCHAR AS  {{replace_invalid_chars("AverageTemperature")}} ,
PARSE_JSON(JSON_STRING):"AverageTemperatureUncertainty":: VARCHAR AS {{replace_invalid_chars("AverageTemperatureUncertainty")}} ,
PARSE_JSON(JSON_STRING):"Country":: VARCHAR AS {{replace_invalid_chars("Country")}},
PARSE_JSON(JSON_STRING):"Date":: VARCHAR AS {{replace_invalid_chars("Date")}}
from  {{ source ('psa' , 'temperaturesbycountry')}}
