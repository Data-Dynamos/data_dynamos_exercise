
{{
  config(
    materialized = 'table'
    )
}}


{# Create Table for Country Emissions
To create a table called co2_emissions_by_country in the carbon_emissions schema, you will use the data from the STG_EMISSIONS_BY_COUNTRY view to analyze and populate the table.

Your output table should contain:
Year: integer
Country: string
TotalEmissions: float
PerCapitaEmissions: float
ShareOfGlobalEmissions: float 

#}



