import streamlit as st
import joblib
import pandas as pd

# Load Trained Model
model = joblib.load("MODEL/credit_card_fraud_model.pkl")

# App Title
st.title("💳 Credit Card Fraud Detection System")

st.write("Enter transaction details below to predict whether the transaction is Genuine or Fraud.")

# Input Fields
time = st.number_input("Time", value=0.0)
amount = st.number_input("Amount", value=100.0)

features = []

# V1 to V28 Inputs
for i in range(1, 29):
    value = st.number_input(f"V{i}", value=0.0)
    features.append(value)

# Predict Button
if st.button("Predict"):

    data = [time] + features + [amount]

    columns = [
        "Time","V1","V2","V3","V4","V5","V6","V7","V8","V9",
        "V10","V11","V12","V13","V14","V15","V16","V17",
        "V18","V19","V20","V21","V22","V23","V24","V25",
        "V26","V27","V28","Amount"
    ]

    input_data = pd.DataFrame([data], columns=columns)

    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.success("✅ Genuine Transaction")
    else:
        st.error("🚨 Fraudulent Transaction")