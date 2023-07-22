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


def display_data_frame(data_frame):
    cellsytle_jscode = JsCode(
        """
        function(params) {
            if (params.value > 0) {
                return {
                    'color': 'white',
                    'backgroundColor': 'forestgreen'
                }
            } else if (params.value < 0) {
                return {
                    'color': 'white',
                    'backgroundColor': 'crimson'
                }
            } else {
                return {
                    'color': 'white',
                    'backgroundColor': 'slategray'
                }
            }
        };
        """
    )

    gridOptions = {
        'columnDefs': [
            {
                'field': column_name.replace("'", "\\'"),
                'cellStyle': cellsytle_jscode
            }
            for column_name in data_frame.columns
        ]
    }

    AgGrid(data_frame.head(20), gridOptions=gridOptions, allow_unsafe_jscode=True)


def display_choropleth_map(data_frame, locations_column, color_column, color_range, color_scale, title):
    fig = px.choropleth(data_frame, locations=locations_column,locationmode="country names", color=color_column,
                        range_color=color_range, color_continuous_scale=color_scale, title=title)
    fig.update_layout(geo=dict(showframe=False, showcoastlines=False, projection_type="equirectangular"),
                              height=600,  # Set the height of the figure
        width=1300 )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_traces(locations=data_frame[locations_column])
    st.plotly_chart(fig)

if __name__ == '__main__':
    st.set_page_config(
        page_title="Data Dynamos",
        page_icon="./assets/favicon.ico",
        layout="wide",
        initial_sidebar_state="expanded",
    )


    session = snowflake_session()
    st.title("Total Emission 🏭 around the world")
    st.subheader('Exercise 4')
    year_to_plot = st.slider("Select a year", 1880, 2013, 2000,key='temperature_year')


    emission_table = "EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.CO2_EMISSIONS_AND_TEMPERATURES_BY_COUNTRY"
    query = f"SELECT year, TOTALEMISSIONS, Country  FROM {emission_table} WHERE year={year_to_plot}"
    emission = session._run_query(query) 
    em = pd.DataFrame(emission, columns=['year', 'TOTALEMISSIONS', 'Country'])
    tab1, tab2 = st.tabs(["🗃 Data","📈 Chart"])
    with tab1:
        display_data_frame(em)
    with tab2:
        display_choropleth_map(em, "Country", "TOTALEMISSIONS", [0, 9000], 'Hot_r', f"Total emission in {year_to_plot}")


