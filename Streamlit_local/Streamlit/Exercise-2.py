# File: exercise2.py

import os
import streamlit as st
import plotly.express as px
import pandas as pd

# Set Streamlit page configuration
# st.set_page_config(
#     page_title="Data Dynamos",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

st.subheader('Exercise 2')
st.title("Total Emissions and Average Temperature 🚀")

# Path to CSV file (update if necessary)
csv_path = "../processed_output/aggregate_country_emissions_temperatures.csv"
if not os.path.exists(csv_path):
    st.error("CSV file not found. Please generate the dataset first.")
    st.stop()

# Load data
df = pd.read_csv(csv_path)

# Select country
country_options = sorted(df['Country'].dropna().unique())
selected_country = st.selectbox('Select a country', country_options)

filtered_data = df[df['Country'] == selected_country].sort_values('Year')

# Select year range
min_year = int(filtered_data['Year'].min())
max_year = int(filtered_data['Year'].max())

year_range = st.slider(
    'Select a range of years',
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    step=1
)

# Calculate current year metrics
current_year = year_range[1]
current_data = filtered_data[filtered_data['Year'] == current_year]

if not current_data.empty:
    avg_temp = current_data['AverageTemperature'].values[0]
    total_emissions = current_data['TotalEmissions'].values[0]

    # Calculate previous year metrics
    prev_data = filtered_data[filtered_data['Year'] == current_year - 1]
    if not prev_data.empty:
        prev_emissions = prev_data['TotalEmissions'].values[0]
        prev_temp = prev_data['AverageTemperature'].values[0]

        pct_change_emissions = ((total_emissions - prev_emissions) / prev_emissions) * 100
        pct_change_temp = ((avg_temp - prev_temp) / prev_temp) * 100
    else:
        pct_change_emissions = 0
        pct_change_temp = 0

    # Display metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Year", f"{current_year}")
    col2.metric("Total Emissions", f"{total_emissions:.2f}", f"{pct_change_emissions:.2f}%")
    col3.metric("Average Temperature", f"{avg_temp:.2f}°C", f"{pct_change_temp:.2f}%")
else:
    st.warning("No data found for the selected country and year.")

# Filter by year range for plot
plot_data = filtered_data[(filtered_data['Year'] >= year_range[0]) & (filtered_data['Year'] <= year_range[1])]

# Line plot function
def display_line_plot(data_frame, x, y, title, xaxis_title, yaxis_title, width):
    fig = px.line(data_frame, x=x, y=y, title=title)
    fig.update_layout(xaxis_title=xaxis_title, yaxis_title=yaxis_title, width=width)
    st.plotly_chart(fig)

# Display plot
if not plot_data.empty:
    display_line_plot(
        plot_data,
        x='Year',
        y=['TotalEmissions', 'AverageTemperature'],
        title=f'Total Emissions and Average Temperature for {selected_country}',
        xaxis_title='Year',
        yaxis_title='Value',
        width=1300
    )
else:
    st.warning("No data to display in the selected range.")
