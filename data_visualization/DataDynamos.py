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


if __name__ == '__main__':
    st.set_page_config(
        page_title="Data Dynamos",
        page_icon="./assets/favicon.ico",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    session = snowflake_session()
    st.title("Data Dynamos 🦉")


    st.markdown('''
    <style>
    p {
        font-size: 18px;
    }
    ul {
        font-size: 18px;
        line-height: 1.6;
    }
    li {
        font-size: 18px;
        list-style-type: disc; 
        line-height: 1.6;         
    }
    h1 {
        color: #2f6372;
        font-size: 30px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>

    <p>
    Climate change is a contentious issue, with some believing it to be a critical threat and others dismissing it as a myth based on flawed science. 
    </p>
    
    <p>
                 In this project, we present a dataset that allows you to draw your own conclusions. 
    </p>

    <p>
    This dataset, compiled by the Berkeley Earth Surface Temperature Study, contains over 1.6 billion temperature reports from 16 archives and provides insights into long-term climate trends. The dataset includes global land and ocean temperatures, as well as temperatures by country, state, and city. 
    </p>

    <p>
    However, collecting this data has not been easy. Early temperature data was collected using mercury thermometers that were subject to variations in measurement depending on visit time, and the construction of airports in the 1940s forced many weather stations to be relocated. In the 1980s, electronic thermometers were introduced, but they were found to have a cooling bias. 
    </p>

    <p>
    Despite these challenges, three organizations - NOAA’s MLOST, NASA’s GISTEMP, and the UK’s HadCrut - have been collating and publishing climate trends data. We have repackaged the data from the Berkeley Earth Study, which offers cleaner and more organized data with source code and transformations. 
    </p>

    <h1>Climate Dashboard Project</h1>

    <p>
    Welcome to the Climate Dashboard Project! In this project, we aim to build an interactive dashboard that provides insights into climate-related data using open-source datasets from Open World in Data and Kaggle.
    </p>

    <p>
    The dashboard will focus on the following questions:
    </p>

    <ul>
    <li><b>Total Emissions and Average Temperature for different Countries 🧭:</b> Explore the relationship between total emissions and average temperature for various countries.</li>
    <li><b>Total Emissions and Average Temperature 🚀:</b> Analyze the correlation between total emissions and average temperature globally.</li>
    <li><b>Share of Global Emissions by Continent 🗺️:</b> Visualize the proportion of global emissions contributed by each continent.</li>
    <li><b>Average Temperature around the World 🌏:</b> Discover the average temperature trends across different regions of the world.</li>
    <li><b>Total Emission 🏭 around the world:</b> Examine the total emission trends from various sources around the world.</li>
    </ul>

    <p>
    Through data visualization and analysis, we hope to provide valuable insights into climate change, its impact, and the factors contributing to it. Let's explore the data together and draw meaningful conclusions.
    </p>
                
    ''', unsafe_allow_html=True)
