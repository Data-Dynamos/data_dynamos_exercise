{% macro drop_user_environment() -%}

{%- if execute -%}
  
{% set participants = 'select * from EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.PARTICIPANTS' %}
{% set result = dbt_utils.get_query_results_as_dict(participants) %}

{% endif %}

{% for username in result['USERNAME'] %}

{% set database = username+'_EXERCISE_CO2_VS_TEMPERATURE' %}

{{ log('DROP DATABASE '+database, info=True) }}

{%- if execute -%}
  
{% set drop_database = 'DROP DATABASE IF EXISTS '~database%}
{% do run_query(drop_database)  %}

{% endif %}

{% endfor %}

{%- endmacro %}
