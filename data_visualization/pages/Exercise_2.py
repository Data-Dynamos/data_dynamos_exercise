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
    # TODO: Fetch data from the AGGREGATE_COUNTRY_EMISSIONS_TEMPERATURES table
    # Add code here to retrieve the necessary data from the AGGREGATE_COUNTRY_EMISSIONS_TEMPERATURES table using a SQL query
    # and assign it to the 'emission_temp' variable
    try:
        query = f""
         # Will hold the SQL query to fetch data from the database like select statement from
         # EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.AGGREGATE_COUNTRY_EMISSIONS_TEMPERATURES
        emission_temperature = session._run_query(query)


         # TODO: Convert the retrieved data into a DataFrame
        # Add code here to convert the fetched data into a DataFrame, using pandas or other appropriate methods
        # TODO: Specify the columns in the dataframe
        emission_temperature = pd.DataFrame(emission_temperature, columns=[None])

        # TODO Create  selectbox to choose the Country
        # Hint To aviod duplicates in your selectbox using unique function in the your dataframe and assign it to the  country_option  variable
        # Fill country_options        
        country_options = None
        selected_country = st.selectbox('Select a country', country_options)
        filtered_data = emission_temperature[emission_temperature['COUNTRY'] == selected_country]

        # Sort the data by 'YEAR' in ascending order
        filtered_data = filtered_data.sort_values('YEAR')

        # Create a slider to choose a range of years for analysis
        year_range = None

        # Filter the data for the selected year
        selected_year_data = None

        # Extract the average temperature and total emissions for the selected year

        average_temperature = selected_year_data['AVERAGETEMPERATURE'].values[0]
        total_emissions = selected_year_data['TOTALEMISSIONS'].values[0]

        # Filter the data for the previous year
        previous_year_data = filtered_data[filtered_data['YEAR'] == year_range[1] - 1]

        # Extract the total emissions for the previous year
        previous_year_emissions = previous_year_data['TOTALEMISSIONS'].values[0]

        # Calculate the percentage change in emissions compared to the previous year
        percentage_change_emission = ((total_emissions - previous_year_emissions) / previous_year_emissions) * 100

        # Extract the average temperature for the previous year
        previous_year_temperature = previous_year_data['AVERAGETEMPERATURE'].values[0]

        # Calculate the percentage change in average temperature compared to the previous year
        percentage_change_temperature = ((average_temperature - previous_year_temperature) / previous_year_temperature) * 100

        # Display metrics in a 3-column layout
        col1, col2, col3 = st.columns(3)
        col1.metric("Year", f"{year_range[1]}")
        col2.metric("Total Emissions", f"{total_emissions:.2f}", f"{percentage_change_emission:.2f}%")
        col3.metric("Average Temperature", f"{average_temperature:.2f}°C", f"{percentage_change_temperature:.2f}%")

        # Filter the data for the selected year range for the line plot
        filtered_line_plot = None

        # Display the line plot showing total emissions and average temperature for the selected country
        display_line_plot(filtered_line_plot, 'YEAR', ['TOTALEMISSIONS', 'AVERAGETEMPERATURE'],
                        f'Total Emissions and Average Temperature for {selected_country}', 'Year', 'Value', 1300)

        # Additional Instructions:
        # - The data has been sorted by 'YEAR' in ascending order to ensure proper visualization on the line plot.
        # - Use the slider to select a specific range of years for analysis.
        # - The metrics section displays the selected year, total emissions, and average temperature for the chosen year.
        # - The percentage change in emissions and temperature compared to the previous year is also displayed.
        # - The line plot showcases the trends in total emissions and average temperature over the selected year range.
        # - The line plot can be interactively zoomed and panned to explore the data further.
    
    except Exception as e:
        st.error("Please Fill missing code 🪄")  
        with st.expander("Error Info ⚠️"):
            st.error("Error: {}".format(str(e)))        