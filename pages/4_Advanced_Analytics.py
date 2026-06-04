import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("📈 Advanced Analytics")

corr = df.corr()

fig = px.imshow(
    corr,
    text_auto=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)
