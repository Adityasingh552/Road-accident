import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("road_accident_model.pkl")

# App title
st.title("🚧 Road Accident Outcome Predictor")

# Sidebar for user input
st.sidebar.header("Enter Accident Details")

# Input form
def user_input():
    city = st.sidebar.selectbox("City", ['Agra', 'Chennai', 'Delhi', 'Mumbai', 'Kolkata'])  # add real options
    category = st.sidebar.selectbox("Cause Category", ['Overspeeding', 'Drunk Driving', 'Brake Failure'])
    subcategory = st.sidebar.selectbox("Cause Subcategory", ['Night Driving', 'Slippery Road', 'Fog'])
    count = st.sidebar.slider("Incident Count", 1, 100)

    # Convert to dataframe
    data = pd.DataFrame({
        'million_plus_cities': [city],
        'cause_category': [category],
        'cause_subcategory': [subcategory],
        'count': [count]
    })

    return data

# Get user input
input_df = user_input()

# Preprocess input like training
for col in input_df.columns:
    if input_df[col].dtype == 'object':
        input_df[col] = input_df[col].astype("category").cat.codes

# Predict
prediction = model.predict(input_df)[0]
outcome = "Fatal" if prediction == 1 else "Non-Fatal"

# Show prediction
st.subheader("Prediction")
st.write(f"🔍 The predicted outcome is: **{outcome}**")
