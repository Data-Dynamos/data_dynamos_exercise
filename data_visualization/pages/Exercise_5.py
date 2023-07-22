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
    st.title("Average Temperature around the World 🌏 ")
    st.subheader('Exercise 5')
    year_to_plot = st.slider("Select a year", 1880, 2013, 2000,key='temperature_year')


    table_name = "EXERCISE_CO2_VS_TEMPERATURE.GLOBAL_TEMPERATURES.AGGREGATE_COUNTRY_TEMPERATURES"
    table = session.table(table_name)
    query = f"SELECT * FROM {table_name} WHERE year={year_to_plot}"
    data = session._run_query(query)
    df = pd.DataFrame(data, columns=['year', 'averagetemperature', 'Country'])
    tab1, tab2 = st.tabs(["🗃 Data","📈 Chart"])
    with tab1:
        display_data_frame(df)
    with tab2:
        display_choropleth_map(df, "Country", "averagetemperature", [-10, 30], 'RdBu_r', f"Average Temperature in {year_to_plot}")


