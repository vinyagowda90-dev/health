import streamlit as st
from utils.data_loader import load_data

df = load_data()

st.title("📊 Dataset Overview")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", df.isnull().sum().sum())
col4.metric("Diabetes Cases", df['Diabetes_012'].sum())

st.dataframe(df.head())
