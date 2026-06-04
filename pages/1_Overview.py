import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/diabetes_012_health_indicators_BRFSS2015.csv"
    )

df = load_data()

st.title("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", df.isnull().sum().sum())

st.subheader("First 10 Rows")
st.dataframe(df.head(10))

st.subheader("Dataset Information")
st.write(df.describe())
