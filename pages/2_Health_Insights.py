import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/diabetes_012_health_indicators_BRFSS2015.csv"
    )

df = load_data()

st.title("🏥 Health Insights")

# Check if BMI exists
if "BMI" in df.columns:

    st.subheader("BMI Distribution")

    fig = px.histogram(
        df,
        x="BMI",
        nbins=30
    )

    st.plotly_chart(fig, use_container_width=True)

# Diabetes distribution
if "Diabetes_012" in df.columns:

    st.subheader("Diabetes Classes")

    counts = df["Diabetes_012"].value_counts()

    fig2 = px.pie(
        values=counts.values,
        names=counts.index
    )

    st.plotly_chart(fig2, use_container_width=True)
