{{
    config(
        tags=['unit-test']
    )
}}

{% call dbt_unit_testing.test('co2_emissions_and_temperatures_by_country', 'assert_co2_emissions_and_temperatures_by_country') %}
  {% call dbt_unit_testing.mock_ref('co2_emissions_by_country') %}
{# 
Provide Mock data
#}

  {% endcall %}

  {% call dbt_unit_testing.mock_ref('aggregate_country_temperatures') %}
{# 
Provide Mock data
#}

  {% endcall %}

  {% call dbt_unit_testing.expect() %}
{# 
Provide Mock data
#}
  {% endcall %} 

{% endcall %}
