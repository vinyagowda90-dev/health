import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("🏥 Health Insights")

fig = px.histogram(
    df,
    x="BMI",
    color="Diabetes_012",
    nbins=30
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.box(
    df,
    x="Diabetes_012",
    y="BMI"
)

st.plotly_chart(fig2, use_container_width=True)
