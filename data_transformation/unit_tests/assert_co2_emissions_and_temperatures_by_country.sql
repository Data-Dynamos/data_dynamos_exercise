{{
    config(
        tags=['unit-test']
    )
}}

{% call dbt_unit_testing.test('co2_emissions_and_temperatures_by_country', 'assert_co2_emissions_and_temperatures_by_country') %}
  {% call dbt_unit_testing.mock_ref('co2_emissions_by_country') %}
  select  '1792' as  YEAR,
  'Germany' as  COUNTRY , 
  '0.468992' as TOTALEMISSIONS , 
  '0.03474' as PERCAPITAEMISSIONS,
  '2.141901' as SHAREOFGLOBALEMISSIONS
  {% endcall %}

  {% call dbt_unit_testing.mock_ref('aggregate_country_temperatures') %}
  select  '1792' as  YEAR,
  'Germany' as  COUNTRY ,
'16.754375' as  AVERAGETEMPERATURE
  {% endcall %}


  {% call dbt_unit_testing.expect() %}
  select  '1792' as  YEAR,
  'Germany' as  COUNTRY , 
  '0.468992' as TOTALEMISSIONS , 
  '0.03474' as PERCAPITAEMISSIONS,
  '2.141901' as SHAREOFGLOBALEMISSIONS,
  '16.754375' as  AVERAGETEMPERATURE
  {% endcall %} 

{% endcall %}

