# File: exercise4.py

import os
import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid
from st_aggrid.shared import JsCode

# Set up Streamlit page
# st.set_page_config(
#     page_title="Data Dynamos",
#     page_icon="./assets/favicon.ico",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# Function: AG Grid with conditional formatting
def display_data_frame(data_frame):
    cellsytle_jscode = JsCode("""
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
    """)

    gridOptions = {
        'columnDefs': [
            {'field': column, 'cellStyle': cellsytle_jscode}
            for column in data_frame.columns
        ]
    }

    AgGrid(data_frame.head(20), gridOptions=gridOptions, allow_unsafe_jscode=True)

# Function: Choropleth map
def display_choropleth_map(data_frame, locations_column, color_column, color_range, color_scale, title):
    fig = px.choropleth(
        data_frame,
        locations=locations_column,
        locationmode="country names",
        color=color_column,
        range_color=color_range,
        color_continuous_scale=color_scale,
        title=title
    )
    fig.update_layout(
        geo=dict(showframe=False, showcoastlines=False, projection_type="equirectangular"),
        height=600,
        width=1300
    )
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)

# Main UI
st.title("Total Emission 🏭 around the world")
st.subheader('Exercise 4')

# Load CSV (adjust path if needed)
csv_path = "../processed_output/co2_emissions_and_temperatures_by_country.csv"
if not os.path.exists(csv_path):
    st.error("CSV file not found. Please make sure the dataset exists.")
    st.stop()

df = pd.read_csv(csv_path)

# Ensure expected columns exist
required_columns = ['Year', 'Country', 'TotalEmissions']
if not all(col in df.columns for col in required_columns):
    st.error("CSV missing required columns: 'Year', 'Country', 'TotalEmissions'")
    st.stop()

# Filter by year
year_to_plot = st.slider("Select a year", min_value=int(df['Year'].min()), max_value=int(df['Year'].max()), value=2000, key='temperature_year')
df_filtered = df[df['Year'] == year_to_plot]

# Tabs for data and chart
tab1, tab2 = st.tabs(["🗃 Data", "📈 Chart"])
with tab1:
    display_data_frame(df_filtered[['Year', 'Country', 'TotalEmissions']])
with tab2:
    display_choropleth_map(
        df_filtered,
        locations_column="Country",
        color_column="TotalEmissions",
        color_range=[0, 9000],
        color_scale='Hot_r',
        title=f"Total Emission in {year_to_plot}"
    )
