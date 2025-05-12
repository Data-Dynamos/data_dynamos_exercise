# Exercise-1.py

# File: Exercise-1.py

import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set page config
# st.set_page_config(
#     page_title="Data Dynamos",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

st.subheader('Exercise 1')
st.title("Total Emissions and Average Temperature for Different Countries 🧭")

# Load data from processed CSV
csv_path = "../processed_output/aggregate_country_emissions_temperatures.csv"
if not os.path.exists(csv_path):
    st.error("CSV file not found. Please generate the dataset first.")
    st.stop()

df = pd.read_csv(csv_path)

# Dropdowns for filters
year_options = sorted(df['Year'].dropna().unique())
selected_year = st.selectbox('Select a year', year_options)

country_options = sorted(df['Country'].dropna().unique())
selected_countries = st.multiselect('Select countries', country_options, key='country A')

# Filtered dataset
filtered_df = df[
    (df['Year'] == selected_year) &
    (df['Country'].isin(selected_countries))
]

# Plotting function
def display_bar_chart(data_frame, x, y, title, xaxis_title, yaxis_title, width, height, color='lightblue'):
    fig = px.bar(data_frame, x=x, y=y, title=title, orientation='h')
    fig.update_traces(marker_color=color)
    fig.update_layout(width=width, height=height, margin=dict(l=50, r=50, b=50, t=50, pad=4))
    fig.update_xaxes(title=xaxis_title)
    fig.update_yaxes(title=yaxis_title)
    st.plotly_chart(fig)

# Show bar chart
if not filtered_df.empty:
    display_bar_chart(
        filtered_df,
        x='TotalEmissions',
        y='Country',
        title='Total Emissions for Selected Countries',
        xaxis_title='Total Emissions',
        yaxis_title='Country',
        width=800,
        height=600,
        color='#ff0000'
    )
else:
    st.warning("No data available for selected filters.")
