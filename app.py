import streamlit as st
import pandas as pd
import joblib

# 1. Page Configuration (must be the first Streamlit command)
st.set_page_config(page_title="Earth Defense Dashboard", page_icon="🌍", layout="wide")

# 2. Main Title and Intro
st.title("🌍 Earth Defense Dashboard")
st.markdown("### Near-Earth Object Hazard Predictor")
st.write("This dashboard analyzes NASA data to predict whether a near-Earth asteroid is potentially hazardous.")

# 3. Load Data & Model
@st.cache_data # This keeps the data loaded in memory so it doesn't reload on every click
def load_data():
    return pd.read_csv('neo_cleaned.csv')

try:
    df = load_data()
    # 4. Display a Data Table
    st.subheader("Asteroid Tracking Database")
    st.dataframe(df.head(10)) # Show the first 10 rows
except FileNotFoundError:
    st.error("Could not find 'neo_cleaned.csv'. Make sure you ran the data cleaning notebook!")

# 5. The Sidebar Simulator (For Exhibition Interactivity)
st.sidebar.header("Threat Simulator")
st.sidebar.write("Input asteroid data below:")

# Create some sliders (you will link these to your ML model in the next step)
velocity = st.sidebar.slider("Relative Velocity", 0.0, 200000.0, 50000.0)
miss_distance = st.sidebar.slider("Miss Distance", 0.0, 70000000.0, 10000000.0)
diameter = st.sidebar.slider("Estimated Diameter (Max)", 0.0, 100.0, 5.0)

if st.sidebar.button("Predict Hazard Status"):
    st.sidebar.info("Model prediction will appear here!")