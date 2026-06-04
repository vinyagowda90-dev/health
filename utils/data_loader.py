import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv(
        "data/diabetes_012_health_indicators_BRFSS2015.csv"
    )
    return df
