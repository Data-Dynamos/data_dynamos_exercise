# Modified from Johannes Rieke's example code

import streamlit as st
from snowflake.snowpark import Session
import plotly.express as px
import pandas as pd
import time

st.title('❄️ How to connect Streamlit to a Snowflake database')

# Establish Snowflake session
@st.cache_resource
def create_session():
    return Session.builder.configs(st.secrets.snowflake).create()



session = create_session()
success_message = st.success("Connected to Snowflake!")

  



st.subheader("Average Temperature around the World 🌏 ")
table_name = "EXERCISE_CO2_VS_TEMPERATURE.GLOBAL_TEMPERATURES.AGGREGATE_COUNTRY_TEMPERATURES"
table = session.table(table_name)

st.dataframe(table.limit(100))
year_to_plot = st.slider("Select a year", 1880, 2013, 2000)
query = f"SELECT * FROM {table_name} WHERE year={year_to_plot}"
data = session._run_query(query)
df = pd.DataFrame(data, columns=['year', 'averagetemperature', 'Country'])
fig = px.choropleth(df, locations="Country", locationmode="country names", color="averagetemperature", range_color=[-10,30], 
                    color_continuous_scale='RdBu_r',title=f"Average Temperature in {year_to_plot}")
fig.update_layout(geo=dict(showframe=False, showcoastlines=False, projection_type="equirectangular"))

# Display the map using Streamlit
st.plotly_chart(fig)

st.subheader("Total Emission 🏭 around the world")
emission_table = "EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.CO2_EMISSIONS_AND_TEMPERATURES_BY_COUNTRY"
year_to_plot_emission = st.slider("Select a year (emissions)", 1880, 2013, 2000, key='emission_year')
query = f"SELECT year, TOTALEMISSIONS, Country  FROM {emission_table} WHERE year={year_to_plot_emission}"
emission = session._run_query(query)
em = pd.DataFrame(emission, columns=['year', 'TOTALEMISSIONS', 'Country'])
st.dataframe(em)
fig_1 = px.choropleth(em, locations="Country", locationmode="country names", color="TOTALEMISSIONS", range_color=[0,9000], 
                    color_continuous_scale='Hot_r',title=f"Total emission in {year_to_plot}")
fig_1.update_layout(geo=dict(showframe=False, showcoastlines=False, projection_type="equirectangular"))

st.plotly_chart(fig_1)