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


def display_line_plot(data_frame, x, y, title, xaxis_title, yaxis_title,width):
    fig = px.line(data_frame, x=x, y=y, title=title)
    fig.update_layout(xaxis_title=xaxis_title, yaxis_title=yaxis_title,width=width)
    st.plotly_chart(fig)


if __name__ == '__main__':
    st.set_page_config(
        page_title="Data Dynamos",
        page_icon="./assets/favicon.ico",
        layout="wide",
        initial_sidebar_state="expanded",
    )


    session = snowflake_session()
    st.subheader('Exercise 2')
    st.title("Total Emissions and Average Temperature 🚀 ")
    emission_temp = "EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.AGGREGATE_COUNTRY_EMISSIONS_TEMPERATURES"
    query = f"SELECT COUNTRY, YEAR, PERCAPITAEMISSIONS, SHAREOFGLOBALEMISSIONS, TOTALEMISSIONS, AVERAGETEMPERATURE FROM {emission_temp}"
    emission_temperature = session._run_query(query)
    emission_temperature = pd.DataFrame(emission_temperature, columns=['COUNTRY', 'YEAR', 'PERCAPITAEMISSIONS', 'SHAREOFGLOBALEMISSIONS', 'TOTALEMISSIONS', 'AVERAGETEMPERATURE'])
    selected_country = st.selectbox('Select a country', emission_temperature['COUNTRY'].unique())
    filtered_data = emission_temperature[emission_temperature['COUNTRY'] == selected_country]
    filtered_data = filtered_data.sort_values('YEAR')
    year_range = st.slider('Select a range of years', min_value=min(filtered_data['YEAR']), max_value=max(filtered_data['YEAR']),
                        value=(min(filtered_data['YEAR']), max(filtered_data['YEAR'])), step=1)
    selected_year_data = filtered_data[filtered_data['YEAR'] == year_range[1]]
    average_temperature = selected_year_data['AVERAGETEMPERATURE'].values[0]
    total_emissions = selected_year_data['TOTALEMISSIONS'].values[0]

    previous_year_data = filtered_data[filtered_data['YEAR'] == year_range[1] - 1]
    previous_year_emissions = previous_year_data['TOTALEMISSIONS'].values[0]
    percentage_change_emission = ((total_emissions - previous_year_emissions) / previous_year_emissions) * 100
    previous_year_temperature = previous_year_data['AVERAGETEMPERATURE'].values[0]
    percentage_change_temperature = ((average_temperature - previous_year_temperature) / previous_year_temperature) * 100

    # Display metrics
    col1, col2,col3= st.columns(3)
    col1.metric("Year", f"{year_range[1]}")
    col2.metric("Total Emissions", f"{total_emissions:.2f}",f"{percentage_change_emission:.2f}%")
    col3.metric("Average Temperature", f"{average_temperature:.2f}°C", f"{percentage_change_temperature:.2f}%")

    filtered_data = filtered_data[(filtered_data['YEAR'] >= year_range[0]) & (filtered_data['YEAR'] <= year_range[1])]

    display_line_plot(filtered_data, 'YEAR', ['TOTALEMISSIONS', 'AVERAGETEMPERATURE'], f'Total Emissions and Average Temperature for {selected_country}', 'Year', 'Value',1300)
