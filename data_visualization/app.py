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

@st.cache_resource
def create_session():
    return Session.builder.configs({"account": os.environ["SNOWFLAKE_ACCOUNT"],
                                    "database": os.environ["SNOWFLAKE_DATABASE"],
                                    "user": os.environ["SNOWFLAKE_USER"],
                                    "password": os.environ["SNOWFLAKE_PASSWORD"],
                                    "role": "DEVELOPER",
                                    "warehouse": "COMPUTE_WH",
                                    "schema": "PSA",
                                    "client_session_keep_alive": True}).create()

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
        width=800 )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_traces(locations=data_frame[locations_column])
    st.plotly_chart(fig)


def display_line_plot(data_frame, x, y, title, xaxis_title, yaxis_title,width):
    fig = px.line(data_frame, x=x, y=y, title=title)
    fig.update_layout(xaxis_title=xaxis_title, yaxis_title=yaxis_title,width=width)
    st.plotly_chart(fig)

def display_pie_chart(data_frame, values, names, title, labels,width,height):
    fig = px.pie(data_frame, values=values, names=names, title=title, labels=labels)
    fig.update_layout(width=width, height=height, margin=dict(l=50, r=50, b=50, t=50, pad=4))
    st.plotly_chart(fig)

def display_bar_chart(data_frame, x, y, title, xaxis_title, yaxis_title, width, height,color=
                      'lightblue'):
    fig = px.bar(data_frame, x=x, y=y, title=title,orientation='h')
    fig.update_traces(marker_color=color)
    fig.update_layout(width=width, height=height, margin=dict(l=50, r=50, b=50, t=50, pad=4))
    fig.update_xaxes(title=xaxis_title)
    fig.update_yaxes(title=yaxis_title)
    st.plotly_chart(fig)

def display_multiple_bar_chart(data_frame, x, y, title, xaxis_title, yaxis_title, width, height):
    fig = px.bar(data_frame, x=x, y=y, barmode='group', title=title)
    fig.update_layout(width=width, height=height, margin=dict(l=50, r=50, b=50, t=50, pad=4))
    fig.update_xaxes(title=xaxis_title)
    fig.update_yaxes(title=yaxis_title)
    st.plotly_chart(fig)



if __name__ == '__main__':
    st.set_page_config(
        page_title="Data Dynamos",
        page_icon="./assets/favicon.ico",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Global Warming 🌡️ 📊")
    session = create_session()

    
year_to_plot = st.slider("Select a year", 1880, 2013, 2000,key='temperature_year')

col1, col2 = st.columns([3, 2])



with col1:
    st.subheader("Average Temperature around the World 🌏 ")
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


with col2:
    st.subheader("Total Emission 🏭 around the world")
    emission_table = "EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.CO2_EMISSIONS_AND_TEMPERATURES_BY_COUNTRY"
    query = f"SELECT year, TOTALEMISSIONS, Country  FROM {emission_table} WHERE year={year_to_plot}"
    emission = session._run_query(query) 
    em = pd.DataFrame(emission, columns=['year', 'TOTALEMISSIONS', 'Country'])
    tab1, tab2 = st.tabs(["🗃 Data","📈 Chart"])
    with tab1:
        display_data_frame(em)
    with tab2:
        display_choropleth_map(em, "Country", "TOTALEMISSIONS", [0, 9000], 'Hot_r', f"Total emission in {year_to_plot}")

st.title("Share of Global Emissions by Continent 🗺 ")
emission_temp_continent = "EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.AGGREGATE_COUNTRY_EMISSIONS_TEMPERATURES"
query = f"SELECT COUNTRY, SHAREOFGLOBALEMISSIONS,YEAR FROM {emission_temp_continent} WHERE COUNTRY IN ('Europe', 'Asia', 'Africa', 'North America', 'South America', 'Oceania')"
emission_data =  session._run_query(query) 
df_emission = pd.DataFrame(emission_data, columns=['COUNTRY', 'SHAREOFGLOBALEMISSIONS','YEAR'])
year_to_plot = st.slider("Select a year", 1800, 2013, 2000)
df_filtered = df_emission[df_emission['YEAR'] == year_to_plot]
display_bar_chart(df_filtered, x='SHAREOFGLOBALEMISSIONS', y='COUNTRY', title='Share of Global Emissions by Continent', xaxis_title='Share of Global Emissions', yaxis_title='Continent', width=800, height=600)
display_pie_chart(df_filtered, 'SHAREOFGLOBALEMISSIONS', 'COUNTRY', f'Share of Global Emissions by Country in {year_to_plot}', {'COUNTRY': 'Country', 'SHAREOFGLOBALEMISSIONS': 'Share of Global Emissions'},1000,600)



st.title("Total Emissions and Average Temperature 🚀 ")
emission_temp = "EXERCISE_CO2_VS_TEMPERATURE.CARBON_EMISSIONS.AGGREGATE_COUNTRY_EMISSIONS_TEMPERATURES"
query = f"SELECT COUNTRY, YEAR, PERCAPITAEMISSIONS, SHAREOFGLOBALEMISSIONS, TOTALEMISSIONS, AVERAGETEMPERATURE FROM {emission_temp}"
emission_temperature = session._run_query(query)
emission_temperature = pd.DataFrame(emission_temperature, columns=['COUNTRY', 'YEAR', 'PERCAPITAEMISSIONS', 'SHAREOFGLOBALEMISSIONS', 'TOTALEMISSIONS', 'AVERAGETEMPERATURE'])
selected_country = st.selectbox('Select a country', emission_temperature['COUNTRY'].unique())
filtered_data = emission_temperature[emission_temperature['COUNTRY'] == selected_country]
filtered_data = filtered_data.sort_values('YEAR')
year_range = st.slider('Select a range of years', min_value=min(filtered_data['YEAR']), max_value=max(filtered_data['YEAR']),
                       value=(min(filtered_data['YEAR']), max(filtered_data['YEAR'])), step=1)
selected_year_data = filtered_data[filtered_data['YEAR'] == year_range[1]]
average_temperature = selected_year_data['AVERAGETEMPERATURE'].values[0]
total_emissions = selected_year_data['TOTALEMISSIONS'].values[0]

previous_year_data = filtered_data[filtered_data['YEAR'] == year_range[1] - 1]
previous_year_emissions = previous_year_data['TOTALEMISSIONS'].values[0]
percentage_change_emission = ((total_emissions - previous_year_emissions) / previous_year_emissions) * 100
previous_year_temperature = previous_year_data['AVERAGETEMPERATURE'].values[0]
percentage_change_temperature = ((average_temperature - previous_year_temperature) / previous_year_temperature) * 100

# Display metrics
col1, col2,col3= st.columns(3)
col1.metric("Year", f"{year_range[1]}")
col2.metric("Total Emissions", f"{total_emissions:.2f}",f"{percentage_change_emission:.2f}%")
col3.metric("Average Temperature", f"{average_temperature:.2f}°C", f"{percentage_change_temperature:.2f}%")




filtered_data = filtered_data[(filtered_data['YEAR'] >= year_range[0]) & (filtered_data['YEAR'] <= year_range[1])]

display_line_plot(filtered_data, 'YEAR', ['TOTALEMISSIONS', 'AVERAGETEMPERATURE'], f'Total Emissions and Average Temperature for {selected_country}', 'Year', 'Value',1300)

st.title("Total Emissions and Average Temperature for different Countries 🧭")
year_options = emission_temperature['YEAR'].unique()
selected_year = st.selectbox('Select a year', year_options)
selected_countries = st.multiselect('Select countries', emission_temperature['COUNTRY'].unique(), key='country A')
filtered_data_bar = emission_temperature[emission_temperature['COUNTRY'].isin(selected_countries) & (emission_temperature['YEAR'] == selected_year)]

display_bar_chart(filtered_data_bar, x='TOTALEMISSIONS', y='COUNTRY',
                  title='Total Emissions for Selected Countries',
                  xaxis_title='Country', yaxis_title='Total Emissions', width=800, height=600,color='#ff0000')