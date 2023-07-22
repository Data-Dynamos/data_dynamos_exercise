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
    emission_temp_continent = "EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.AGGREGATE_COUNTRY_EMISSIONS_TEMPERATURES"
    query = f"SELECT COUNTRY, SHAREOFGLOBALEMISSIONS,YEAR FROM {emission_temp_continent} WHERE COUNTRY IN ('Europe', 'Asia', 'Africa', 'North America', 'South America', 'Oceania')"
    emission_data =  session._run_query(query) 
    df_emission = pd.DataFrame(emission_data, columns=['COUNTRY', 'SHAREOFGLOBALEMISSIONS','YEAR'])
    year_to_plot = st.slider("Select a year", 1800, 2013, 2000)
    df_filtered = df_emission[df_emission['YEAR'] == year_to_plot]

    display_pie_chart(df_filtered, 'SHAREOFGLOBALEMISSIONS', 'COUNTRY', f'Share of Global Emissions by Country in {year_to_plot}', {'COUNTRY': 'Country', 'SHAREOFGLOBALEMISSIONS': 'Share of Global Emissions'},1000,600)

    display_bar_chart(df_filtered, x='SHAREOFGLOBALEMISSIONS', y='COUNTRY', title='Share of Global Emissions by Continent', xaxis_title='Share of Global Emissions', yaxis_title='Continent', width=800, height=600)