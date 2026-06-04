import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/diabetes_012_health_indicators_BRFSS2015.csv"
    )

df = load_data()

st.title("📈 Correlation Analysis")

corr = df.corr(numeric_only=True)

fig = px.imshow(
    corr,
    text_auto=False,
    aspect="auto"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
