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
    try:
        # Use a slider widget to select a year from the DataFrame
        year_to_plot = None
        # Construct a SQL query to retrieve data EXERCISE_CO2_VS_TEMPERATURE.GLOBAL_TEMPERATURES.AGGREGATE_COUNTRY_TEMPERATURES
        # Will hold the SQL query to fetch data from the database like select statement from EXERCISE_CO2_VS_TEMPERATURE.GLOBAL_TEMPERATURES.AGGREGATE_COUNTRY_TEMPERATURES
        table_name = "EXERCISE_CO2_VS_TEMPERATURE.GLOBAL_TEMPERATURES.AGGREGATE_COUNTRY_TEMPERATURES"
        table = session.table(table_name)

        query = f""

            # Execute the SQL query and get the temperature data for the selected year
        data = session._run_query(query)

        # Create a DataFrame with 'year', 'averagetemperature', 'Country' column 
        df = None

        # Create two tabs for data and chart visualizations
        tab1, tab2 = st.tabs(["🗃 Data", "📈 Chart"])

        # Display the data frame in the first tab
        with tab1:
            display_data_frame(df)  # Assuming display_data_frame is a custom function to display a DataFrame

        # Display a choropleth map in the second tab, showing the average temperature around the world for the selected year
        with tab2:
            display_choropleth_map(df, "Country", "averagetemperature", [-10, 30], 'RdBu_r', f"Average Temperature in {year_to_plot}")
            # Assuming display_choropleth_map is a custom function that displays a choropleth map, taking the DataFrame, column names for country and temperature, temperature range, colormap, and title as arguments.
            # The map will visualize the average temperature of different countries on the map with a color scale from -10°C to 30°C.
            # The title will indicate the selected year.

    except Exception as e:
        st.error("Please Fill missing code 🪄")  
        with st.expander("Error Info ⚠️"):
            st.error("Error: {}".format(str(e)))



