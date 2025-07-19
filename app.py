import streamlit as st
import pandas as pd
import joblib

model = joblib.load('models/rf_model.pkl')
expected_columns = joblib.load('models/expected_columns.pkl')

st.title("Transaction Fraud Detection")

uploaded_file = st.file_uploader("Upload a CSV file with transaction(s):", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    if 'Class' in data.columns:
        data = data.drop('Class', axis=1)

    missing_cols = set(expected_columns) - set(data.columns)
    extra_cols = set(data.columns) - set(expected_columns)

    if missing_cols or extra_cols:
        st.error(f"Column mismatch. \nMissing: {missing_cols} \nUnexpected: {extra_cols}")
    else:
        prediction = model.predict(data)
        data['Prediction'] = prediction
        st.success("Prediction complete!")
        st.write(data)