import os

import streamlit as st
from snowflake.snowpark import Session


@st.cache_resource
def snowflake_session():
    return Session.builder.configs({"account": os.environ["SNOWFLAKE_ACCOUNT"],
                                    "database": os.environ["SNOWFLAKE_DATABASE"],
                                    "user": os.environ["SNOWFLAKE_USER"],
                                    "password": os.environ["SNOWFLAKE_PASSWORD"],
                                    "role": "DEVELOPER",
                                    "warehouse": "COMPUTE_WH",
                                    "schema": "PSA",
                                    "client_session_keep_alive": True}).create()
