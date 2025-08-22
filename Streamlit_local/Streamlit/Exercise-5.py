import streamlit as st
import pandas as pd
import plotly.express as px

def display_data_frame(data_frame):
    st.dataframe(data_frame.head(20), use_container_width=True)

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
    st.plotly_chart(fig)

if __name__ == '__main__':
    # st.set_page_config(
    #     page_title="Data Dynamos",
    #     page_icon="🌍",
    #     layout="wide",
    #     initial_sidebar_state="expanded",
    # )

    st.title("Average Temperature around the World 🌏")
    st.subheader('Exercise 5')

    # Load CSV with correct filename and column cases
    df_temp = pd.read_csv("../processed_output/aggregate_country_temperatures.csv")

    # Ensure correct types
    df_temp['Year'] = df_temp['Year'].astype(int)
    df_temp['Country'] = df_temp['Country'].astype(str)
    df_temp['AverageTemperature'] = pd.to_numeric(df_temp['AverageTemperature'], errors='coerce').fillna(0)

    year_to_plot = st.slider("Select a year", int(df_temp['Year'].min()), int(df_temp['Year'].max()), 2000)

    df_year = df_temp[df_temp['Year'] == year_to_plot]

    tab1, tab2 = st.tabs(["🗃 Data", "📈 Chart"])
    with tab1:
        display_data_frame(df_year)
    with tab2:
        display_choropleth_map(
            df_year,
            "Country",
            "AverageTemperature",
            [-10, 30],
            'RdBu_r',
            f"Average Temperature in {year_to_plot}"
        )
