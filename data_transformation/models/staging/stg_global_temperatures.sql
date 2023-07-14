
{{
  config(
    materialized = 'view'
    )
}}

select  

PARSE_JSON(JSON_STRING):"Date":: VARCHAR AS  "Date",
PARSE_JSON(JSON_STRING):"LandAndOceanAverageTemperature":: VARCHAR AS  {{replace_invalid_chars("LandAndOceanAverageTemperature") }} ,
PARSE_JSON(JSON_STRING):"LandAndOceanAverageTemperatureUncertainty":: VARCHAR AS  {{replace_invalid_chars("LandAndOceanAverageTemperatureUncertainty")}},
PARSE_JSON(JSON_STRING):"LandAverageTemperature":: VARCHAR AS  {{replace_invalid_chars("LandAverageTemperature") }} ,
PARSE_JSON(JSON_STRING):"LandAverageTemperatureUncertainty":: VARCHAR AS   {{replace_invalid_chars("LandAverageTemperatureUncertainty") }},
PARSE_JSON(JSON_STRING):"LandMaxTemperature":: VARCHAR AS {{replace_invalid_chars("LandMaxTemperature") }}, 
PARSE_JSON(JSON_STRING):"LandMaxTemperatureUncertainty":: VARCHAR AS {{replace_invalid_chars("LandMaxTemperatureUncertainty") }},
PARSE_JSON(JSON_STRING):"LandMinTemperature":: VARCHAR AS  {{replace_invalid_chars("LandMinTemperature") }},
PARSE_JSON(JSON_STRING):"LandMinTemperatureUncertainty":: VARCHAR AS {{replace_invalid_chars("LandMinTemperatureUncertainty")}}
from  {{ source ('psa' , 'globaltemperatures')}}