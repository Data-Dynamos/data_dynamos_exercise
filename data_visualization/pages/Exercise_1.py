import os

import streamlit as st
from snowflake.snowpark import Session
from st_aggrid import AgGrid
from st_aggrid.shared import JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from snowflake.snowpark import Session
import plotly.express as px
import pandas as pd
from utils.session import snowflake_session


def display_bar_chart(data_frame, x, y, title, xaxis_title, yaxis_title, width, height,color=
                      'lightblue'):
    fig = px.bar(data_frame, x=x, y=y, title=title,orientation='h')
    fig.update_traces(marker_color=color)
    fig.update_layout(width=width, height=height, margin=dict(l=50, r=50, b=50, t=50, pad=4))
    fig.update_xaxes(title=xaxis_title)
    fig.update_yaxes(title=yaxis_title)
    st.plotly_chart(fig)


if __name__ == '__main__':
    st.set_page_config(
        page_title="Data Dynamos",
        page_icon="./assets/favicon.ico",
        layout="wide",
        initial_sidebar_state="expanded",
    )


    session = snowflake_session()
    st.subheader('Exercise 1')
    st.title("Total Emissions and Average Temperature for different Countries 🧭")

    emission_temp = "EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.AGGREGATE_COUNTRY_EMISSIONS_TEMPERATURES"
    query = f"SELECT COUNTRY, YEAR, PERCAPITAEMISSIONS, SHAREOFGLOBALEMISSIONS, TOTALEMISSIONS, AVERAGETEMPERATURE FROM {emission_temp}"
    emission_temperature = session._run_query(query)
    emission_temperature = pd.DataFrame(emission_temperature, columns=['COUNTRY', 'YEAR', 'PERCAPITAEMISSIONS', 'SHAREOFGLOBALEMISSIONS', 'TOTALEMISSIONS', 'AVERAGETEMPERATURE'])

    year_options = emission_temperature['YEAR'].unique()
    selected_year = st.selectbox('Select a year', year_options)
    selected_countries = st.multiselect('Select countries', emission_temperature['COUNTRY'].unique(), key='country A')
    filtered_data_bar = emission_temperature[emission_temperature['COUNTRY'].isin(selected_countries) & (emission_temperature['YEAR'] == selected_year)]

    display_bar_chart(filtered_data_bar, x='TOTALEMISSIONS', y='COUNTRY',
                    title='Total Emissions for Selected Countries',
                    xaxis_title='Country', yaxis_title='Total Emissions', width=800, height=600,color='#ff0000')