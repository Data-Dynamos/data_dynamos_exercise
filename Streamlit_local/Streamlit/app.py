import streamlit as st
st.set_page_config(
    page_title="Data Dynamos",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Now you can add other Streamlit components like title, tabs, etc.
st.title("🌍 Data Dynamos Dashboard")
st.markdown("Explore insights across multiple exercises using the tabs below.")

# Load each exercise as a tab
tabs = st.tabs(["📊 Exercise 1", "📈 Exercise 2", "🗺 Exercise 3", "🏭 Exercise 4", "🌡 Exercise 5"])

with tabs[0]:

    exec(open("Exercise-1.py").read())  # Running Exercise 1 code

with tabs[1]:

    exec(open("Exercise-2.py").read())  # Running Exercise 2 code

with tabs[2]:

    exec(open("Exercise-3.py").read())  # Running Exercise 3 code

with tabs[3]:

    exec(open("Exercise-4.py").read())  # Running Exercise 4 code

with tabs[4]:

    exec(open("Exercise-5.py").read())  # Running Exercise 5 code
