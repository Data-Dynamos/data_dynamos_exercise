import streamlit as st

from utils.session import snowflake_session

st.set_page_config(page_title="Exercise 2", page_icon="./assets/favicon.ico", layout="wide")
st.title("Exercise 2")
st.header("Worldwide Total CO2 Emission 🏭 Choropleth Map")

session = snowflake_session()
