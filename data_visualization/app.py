import os

import streamlit as st
from snowflake.snowpark import Session


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


if __name__ == '__main__':
    st.set_page_config(
        page_title="Data Dynamos",
        page_icon="./assets/favicon.ico",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Global Warming 🌡️ 📊")
    session = create_session()
