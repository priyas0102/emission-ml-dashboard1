import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.title("🌱 Agri Emission & NDVI Dashboard")

# Load data
df = pd.read_csv("data/final_dataset.csv")
df['date'] = pd.to_datetime(df['date'])

# Show data
st.subheader("📊 Dataset")
st.write(df.head())

# NDVI Trend
st.subheader("📈 NDVI Trend")
fig, ax = plt.subplots()
ax.plot(df['date'], df['ndvi'])
ax.set_xlabel("Date")
ax.set_ylabel("NDVI")
st.pyplot(fig)

# Load model (we'll save it next)
# model = joblib.load("models/model.pkl")

# User Input
st.subheader("🤖 Predict NDVI")

temp_max = st.slider("Max Temperature", 10, 50, 30)
temp_min = st.slider("Min Temperature", 0, 30, 15)
rainfall = st.slider("Rainfall", 0.0, 50.0, 5.0)

# Prediction button
if st.button("Predict NDVI"):
    # TEMP placeholder (we'll fix model load next)
    model = joblib.load("models/model.pkl")
    prediction = model.predict([[temp_max, temp_min, rainfall]])[0] # replace later
    st.success(f"Predicted NDVI: {prediction:.2f}")