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

@st.cache_resource
def create_session():
    return Session.builder.configs({"account": os.environ["SNOWFLAKE_ACCOUNT"],
                                    "database": os.environ["SNOWFLAKE_DATABASE"],
                                    "user": os.environ["SNOWFLAKE_USER"],
                                    "password": os.environ["SNOWFLAKE_PASSWORD"],
                                    "role": "DEVELOPER",
                                    "warehouse": "COMPUTE_WH",
                                    "schema": "PSA",
                                    "client_session_keep_alive": True}).create()


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

    st.title("Total Emissions and Average Temperature for different Countries 🧭")
    session = create_session()

    # TODO: Fetch data from the AGGREGATE_COUNTRY_EMISSIONS_TEMPERATURES table
    # Add code here to retrieve the necessary data from the AGGREGATE_COUNTRY_EMISSIONS_TEMPERATURES table using a SQL query
    # and assign it to the 'emission_temp' variable

    query = f"" #  Will hold the SQL query to fetch data from the database like select statement from 
              #EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.AGGREGATE_COUNTRY_EMISSIONS_TEMPERATURES table
    emission_temperature = session._run_query(query)

    # TODO: Convert the retrieved data into a DataFrame
    # Add code here to convert the fetched data into a DataFrame, using pandas or other appropriate methods

    emission_temperature = pd.DataFrame(emission_temperature, columns=['None'])

   # TODO
    # Create selectbox to choose the Year
    # Hint To aviod duplicates in your selectbox using unique function in the your dataframe and assign it to the year_options variable
    # Fill year_options 
    year_options = None
    selected_year = st.selectbox('Select a year', year_options)

    # TODO Create multi selectbox to choose the Year
    # Hint To aviod duplicates in your selectbox using unique function in the your dataframe and assign it to thecountry_options  variable
    # Fill country_options 
    country_options = None
    selected_countries = st.multiselect('Select countries',country_options, key='country A')

    # TODO 
    # Filter out the countries only from country_options and year_options from the data frame emission_temperature
    filtered_data_bar = emission_temperature[None]

   # TODO Define X and Y Parameters for plotting the bar chart
    display_bar_chart(filtered_data_bar, x='', y='',
                    title='',
                    xaxis_title='', yaxis_title='', width=800, height=600,color='#ff0000')
    