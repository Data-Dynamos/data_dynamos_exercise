
{{
  config(
    materialized = 'view'
    )
}}

select   
  PARSE_JSON(JSON_STRING):"Annual CO2 emissions":: VARCHAR AS  {{replace_invalid_chars("Annual CO2 emissions") }},      
  PARSE_JSON(JSON_STRING):"Annual CO2 growth (%)"::VARCHAR AS  {{replace_invalid_chars("Annual CO2 growth (%)") }},
  PARSE_JSON(JSON_STRING):"Annual CO2 growth (abs)"::VARCHAR AS {{replace_invalid_chars("Annual CO2 growth (abs)") }},
  PARSE_JSON(JSON_STRING):"Annual consumption-based CO2 emissions"::VARCHAR AS {{replace_invalid_chars("Annual consumption-based CO2 emissions")}},
  PARSE_JSON(JSON_STRING):"CO2 emissions embedded in trade"::VARCHAR AS {{replace_invalid_chars("CO2 emissions embedded in trade")}},
  PARSE_JSON(JSON_STRING):"CO2 emissions from bunkers"::VARCHAR AS {{replace_invalid_chars("CO2 emissions from bunkers")}},
  PARSE_JSON(JSON_STRING):"CO2 emissions from cement"::VARCHAR AS {{replace_invalid_chars("CO2 emissions from cement")}},
  PARSE_JSON(JSON_STRING):"CO2 emissions from coal"::VARCHAR AS {{replace_invalid_chars("CO2 emissions from coal")}},
  PARSE_JSON(JSON_STRING):"CO2 emissions from flaring"::VARCHAR AS {{replace_invalid_chars("CO2 emissions from flaring")}},
  PARSE_JSON(JSON_STRING):"CO2 emissions from gas"::VARCHAR AS {{replace_invalid_chars("CO2 emissions from gas")}},
  PARSE_JSON(JSON_STRING):"CO2 emissions from oil"::VARCHAR AS {{replace_invalid_chars("CO2 emissions from oil")}},
  PARSE_JSON(JSON_STRING):"CO2 emissions from other industry"::VARCHAR AS {{replace_invalid_chars("CO2 emissions from other industry")}},
  PARSE_JSON(JSON_STRING):"CO2 per GDP (kg per $PPP)"::VARCHAR AS {{replace_invalid_chars("CO2 per GDP (kg per $PPP)")}},
  PARSE_JSON(JSON_STRING):"CO2 per unit energy (kgCO2 per kilowatt-hour)"::VARCHAR AS  {{replace_invalid_chars("CO2 per unit energy (kgCO2 per kilowatt-hour)")}},
  PARSE_JSON(JSON_STRING):"Cement emissions (per capita)"::VARCHAR AS {{replace_invalid_chars("Cement emissions (per capita)")}},
  PARSE_JSON(JSON_STRING):"Coal emissions (per capita)"::VARCHAR AS {{replace_invalid_chars("Coal emissions (per capita)")}},
  PARSE_JSON(JSON_STRING):"Consumption-based CO2 per GDP (kg per $PPP)"::VARCHAR AS {{replace_invalid_chars("Consumption-based CO2 per GDP (kg per $PPP)")}},
  PARSE_JSON(JSON_STRING):"Cumulative CO2 emissions"::VARCHAR AS {{replace_invalid_chars("Cumulative CO2 emissions")}},
  PARSE_JSON(JSON_STRING):"Cumulative cement emissions"::VARCHAR AS {{replace_invalid_chars("Cumulative cement emissions")}},
  PARSE_JSON(JSON_STRING):"Cumulative coal emissions"::VARCHAR AS {{replace_invalid_chars("Cumulative coal emissions")}},
  PARSE_JSON(JSON_STRING):"Cumulative flaring emissions"::VARCHAR AS {{replace_invalid_chars("Cumulative flaring emissions")}},
  PARSE_JSON(JSON_STRING):"Cumulative gas emissions"::VARCHAR AS {{replace_invalid_chars("Cumulative gas emissions")}},
  PARSE_JSON(JSON_STRING):"Cumulative oil emissions"::VARCHAR AS {{replace_invalid_chars("Cumulative oil emissions")}},
  PARSE_JSON(JSON_STRING):"Cumulative other industry emissions"::VARCHAR AS {{replace_invalid_chars("Cumulative other industry emissions")}},
  PARSE_JSON(JSON_STRING):"Emissions embedded in trade per capita"::VARCHAR AS  {{replace_invalid_chars("Emissions embedded in trade per capita")}},
  PARSE_JSON(JSON_STRING):"Entity"::VARCHAR AS {{replace_invalid_chars("Entity")}},
  PARSE_JSON(JSON_STRING):"Flaring emissions (per capita)"::VARCHAR AS {{replace_invalid_chars("Flaring emissions (per capita)")}},
  PARSE_JSON(JSON_STRING):"Gas emissions (per capita)"::VARCHAR AS {{replace_invalid_chars("Gas emissions (per capita)")}},
  PARSE_JSON(JSON_STRING):"Oil emissions (per capita)"::VARCHAR AS {{replace_invalid_chars("Oil emissions (per capita)")}},
  PARSE_JSON(JSON_STRING):"Other emissions (per capita)"::VARCHAR AS {{replace_invalid_chars("Other emissions (per capita)")}},
  PARSE_JSON(JSON_STRING):"Per capita CO2 emissions"::VARCHAR AS {{replace_invalid_chars("Per capita CO2 emissions")}},
  PARSE_JSON(JSON_STRING):"Per capita consumption-based CO2 emissions"::VARCHAR AS {{replace_invalid_chars("Per capita consumption-based CO2 emissions")}},
  PARSE_JSON(JSON_STRING):"Share of CO2 emissions embedded in trade"::VARCHAR AS {{replace_invalid_chars("Share of CO2 emissions embedded in trade")}},
  PARSE_JSON(JSON_STRING):"Share of global CO2 emissions"::VARCHAR AS {{replace_invalid_chars("Share of global CO2 emissions")}},
  PARSE_JSON(JSON_STRING):"Share of global cement emissions"::VARCHAR AS {{replace_invalid_chars("Share of global cement emissions")}},
  PARSE_JSON(JSON_STRING):"Share of global coal emissions"::VARCHAR AS {{replace_invalid_chars("Share of global coal emissions")}},
  PARSE_JSON(JSON_STRING):"Share of global cumulative CO2 emissions"::VARCHAR AS {{replace_invalid_chars("Share of global cumulative CO2 emissions")}},
  PARSE_JSON(JSON_STRING):"Share of global cumulative cement emissions"::VARCHAR AS {{replace_invalid_chars("Share of global cumulative cement emissions")}},
  PARSE_JSON(JSON_STRING):"Share of global cumulative coal emissions"::VARCHAR AS {{replace_invalid_chars("Share of global cumulative coal emissions")}},
  PARSE_JSON(JSON_STRING):"Share of global cumulative flaring emissions"::VARCHAR AS {{replace_invalid_chars("Share of global cumulative flaring emissions")}},
  PARSE_JSON(JSON_STRING):"Share of global cumulative gas emissions"::VARCHAR AS {{replace_invalid_chars("Share of global cumulative gas emissions")}},
  PARSE_JSON(JSON_STRING):"Share of global cumulative oil emissions"::VARCHAR AS {{replace_invalid_chars("Share of global cumulative oil emissions")}},
  PARSE_JSON(JSON_STRING):"Share of global flaring emissions"::VARCHAR AS {{replace_invalid_chars("Share of global flaring emissions")}},
  PARSE_JSON(JSON_STRING):"Share of global gas emissions"::VARCHAR AS {{replace_invalid_chars("Share of global gas emissions")}},
  PARSE_JSON(JSON_STRING):"Share of global oil emissions"::VARCHAR AS {{replace_invalid_chars("Share of global oil emissions")}},
  PARSE_JSON(JSON_STRING):"Year"::VARCHAR AS "Year"
from {{ source ('psa' , 'emissionsbycountry')}}