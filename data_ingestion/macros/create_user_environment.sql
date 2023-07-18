{% macro create_user_environment() -%}

{%- if execute -%}
  
{% set participants = 'select * from EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.PARTICIPANTS' %}
{% set result = dbt_utils.get_query_results_as_dict(participants) %}

{% endif %}

{% for username in result['USERNAME'] %}

{% set database = username+'_EXERCISE_CO2_VS_TEMPERATURE' %}

{{ log(database, info=True) }}

{%- if execute -%}
  
{% set create_database = 'create database '~database%}
{{ log(create_database, info=True) }}
{% do run_query(create_database)  %}
{% set use_database = 'use database '~database%}
{{ log(use_database, info=True) }}
{% do run_query(use_database)  %}
{% endif %}

{%- if execute -%}

{% set create_psa_schema = 'create schema PSA' %}
{% do run_query(create_psa_schema)  %}

{% set create_carbon_emissions = 'create schema CARBON_EMISSIONS' %}
{% do run_query(create_carbon_emissions)  %}

{% set create_global_temperatures = 'create schema GLOBAL_TEMPERATURES' %}
{% do run_query(create_global_temperatures)  %}

{% endif %}

{%- if execute -%}

{% set create_emissionsbycountry = 'create or replace table PSA.EMISSIONSBYCOUNTRY as (
select * from EXERCISE_CO2_VS_TEMPERATURE.PSA.EMISSIONSBYCOUNTRY
)' %}
{% do run_query(create_emissionsbycountry)  %}
{% endif %}


{%- if execute -%}

{% set create_emissionsbycountry = 'create or replace table PSA.EMISSIONSBYCOUNTRY as (
select * from EXERCISE_CO2_VS_TEMPERATURE.PSA.EMISSIONSBYCOUNTRY
)' %}
{% do run_query(create_emissionsbycountry)  %}
{% endif %}

{%- if execute -%}
{% set create_globaltemperatures = 'create or replace table PSA.GLOBALTEMPERATURES as (
select * from EXERCISE_CO2_VS_TEMPERATURE.PSA.GLOBALTEMPERATURES
)' %}
{% do run_query(create_globaltemperatures)  %}
{% endif %}

{%- if execute -%}
{% set create_temperaturesbycountry = 'create or replace table PSA.TEMPERATURESBYCOUNTRY as (
select * from EXERCISE_CO2_VS_TEMPERATURE.PSA.TEMPERATURESBYCOUNTRY
)' %}
{% do run_query(create_temperaturesbycountry)  %}
{% endif %}

{%- if execute -%}
{% set create_stg_emissionsbycountry = 'create or replace view PSA.STG_EMISSIONS_BY_COUNTRY as (
select * from EXERCISE_CO2_VS_TEMPERATURE.PSA.STG_EMISSIONS_BY_COUNTRY
)' %}
{% do run_query(create_stg_emissionsbycountry )  %}
{% endif %}

{%- if execute -%}
{% set create_stg_globaltemperatures = 'create or replace view PSA.STG_GLOBAL_TEMPERATURES as (
select * from EXERCISE_CO2_VS_TEMPERATURE.PSA.STG_GLOBAL_TEMPERATURES
)' %}
{% do run_query(create_stg_globaltemperatures)  %}
{% endif %}

{%- if execute -%}
{% set create_stg_temperaturesbycountry = 'create or replace view PSA.STG_TEMPERATURES_BY_COUNTRY as (
select * from EXERCISE_CO2_VS_TEMPERATURE.PSA.STG_TEMPERATURES_BY_COUNTRY
)' %}
{% do run_query(create_stg_temperaturesbycountry)  %}

{% endif %}

{% endfor %}


{%- endmacro %}
