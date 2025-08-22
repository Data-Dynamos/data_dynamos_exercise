# File: exercise3.py

import os
import streamlit as st
import plotly.express as px
import pandas as pd

# Set up Streamlit page
# st.set_page_config(
#     page_title="Data Dynamos",
#     page_icon="./assets/favicon.ico",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# Chart: Bar
def display_bar_chart(data_frame, x, y, title, xaxis_title, yaxis_title, width, height, color='lightblue'):
    fig = px.bar(data_frame, x=x, y=y, title=title, orientation='h')
    fig.update_traces(marker_color=color)
    fig.update_layout(width=width, height=height, margin=dict(l=50, r=50, b=50, t=50, pad=4))
    fig.update_xaxes(title=xaxis_title)
    fig.update_yaxes(title=yaxis_title)
    st.plotly_chart(fig)

# Chart: Pie
def display_pie_chart(data_frame, values, names, title, labels, width, height):
    fig = px.pie(data_frame, values=values, names=names, title=title, labels=labels)
    fig.update_layout(width=width, height=height, margin=dict(l=50, r=50, b=50, t=50, pad=4))
    st.plotly_chart(fig)

# Main content
st.subheader('Exercise 3')
st.title("Share of Global Emissions by Continent 🗺")

# CSV path (adjust as needed)
csv_path = "../processed_output/aggregate_country_emissions_temperatures.csv"
if not os.path.exists(csv_path):
    st.error("CSV file not found. Please generate the dataset first.")
    st.stop()

# Load CSV data
df = pd.read_csv(csv_path)

# Filter only continents (assuming those are entered as countries in your dataset)
continents = ['Europe', 'Asia', 'Africa', 'North America', 'South America', 'Oceania']
df = df[df['Country'].isin(continents)]

# Year slider
year_to_plot = st.slider("Select a year", min_value=int(df['Year'].min()), max_value=int(df['Year'].max()), value=2000)

df_filtered = df[df['Year'] == year_to_plot]

# Display pie chart
display_pie_chart(
    df_filtered,
    values='ShareOfGlobalEmissions',
    names='Country',
    title=f'Share of Global Emissions by Continent in {year_to_plot}',
    labels={'Country': 'Continent', 'ShareOfGlobalEmissions': 'Share of Global Emissions'},
    width=1000,
    height=600
)

# Display bar chart
display_bar_chart(
    df_filtered,
    x='ShareOfGlobalEmissions',
    y='Country',
    title='Share of Global Emissions by Continent',
    xaxis_title='Share of Global Emissions',
    yaxis_title='Continent',
    width=800,
    height=600
)
