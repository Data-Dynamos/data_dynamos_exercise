import streamlit as st

from utils.session import snowflake_session

st.set_page_config(
    page_title="Data Dynamos",
    page_icon="./assets/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Global Warming 🌡️ 📊")
st.text("Welcome to Data Dynamos visualization exercise. Navigate to the exercises and start implementing them!")
session = snowflake_session()
