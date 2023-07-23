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

def display_pie_chart(data_frame, values, names, title, labels,width,height):
    fig = px.pie(data_frame, values=values, names=names, title=title, labels=labels)
    fig.update_layout(width=width, height=height, margin=dict(l=50, r=50, b=50, t=50, pad=4))
    st.plotly_chart(fig)



if __name__ == '__main__':
    st.set_page_config(
        page_title="Data Dynamos",
        page_icon="./assets/favicon.ico",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    session = snowflake_session()
    st.subheader('Exercise 3 ')
    st.title("Share of Global Emissions by Continent 🗺 ")
    try:
        # Construct a SQL query to retrieve data for selected continents ('Europe', 'Asia', 'Africa', 'North America', 'South America', 'Oceania')
        # Will hold the SQL query to fetch data from the database like select statement from
        # EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.AGGREGATE_COUNTRY_EMISSIONS_TEMPERATURES
        query = f""
        # Execute the SQL query and get the emission data
        emission_data = session._run_query(query)

        # Create a DataFrame from the emission data
        df_emission = None

        # Use a slider widget to select a year from the DataFrame
        year_to_plot = None

        # Filter the DataFrame to get data for the selected year
        df_filtered = None

        # Display a pie chart showing the share of global emissions by country for the selected year
        display_pie_chart(df_filtered, 'SHAREOFGLOBALEMISSIONS', 'COUNTRY', f'Share of Global Emissions by Country in {year_to_plot}', {'COUNTRY': 'Country', 'SHAREOFGLOBALEMISSIONS': 'Share of Global Emissions'}, 1000, 600)

    except Exception as e:
        st.error("Please Fill missing code 🪄")  
        with st.expander("Error Info ⚠️"):
            st.error("Error: {}".format(str(e)))    