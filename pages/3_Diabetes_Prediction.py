import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/diabetes_model.pkl")

st.title("🤖 Diabetes Risk Predictor")

bmi = st.slider("BMI",10,60,25)
age = st.slider("Age Category",1,13,5)
genhlth = st.slider("General Health",1,5,3)

if st.button("Predict"):
    
    sample = pd.DataFrame({
        "BMI":[bmi],
        "Age":[age],
        "GenHlth":[genhlth]
    })

    prediction = model.predict(sample)

    st.success(
        f"Predicted Class : {prediction[0]}"
    )
