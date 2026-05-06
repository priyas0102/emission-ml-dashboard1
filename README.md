## 🌐 Live Demo
[Click here to view the app](https://emission-ml-dashboard1-rq9xu9xx683b6pdqsnfknj.streamlit.app/)

# 🌱 Agri Emission ML Dashboard

> End-to-End Machine Learning Pipeline for Vegetation Health Monitoring using Satellite NDVI and Weather Data

---

## 🚀 Overview

This project builds a complete data-to-deployment pipeline that predicts vegetation health (NDVI) by combining satellite imagery and weather data.

It demonstrates real-world skills in:
- Geospatial data processing
- Time-series feature engineering
- Machine learning modeling
- Interactive dashboard deployment

---

## 📊 Problem Statement

Monitoring crop health and environmental conditions is critical for agriculture and climate analysis.

Traditional methods are:
- Manual ❌
- Slow ❌
- Not scalable ❌

👉 This project solves it using **automated satellite + ML pipeline**

---

## 🧠 Solution

- Extract NDVI from Google Earth Engine
- Integrate weather data (temperature, rainfall, humidity)
- Train ML model to predict NDVI
- Deploy via interactive dashboard

---

## 🏗️ Architecture
Satellite Data (NDVI) 🌍
↓
Weather Data 🌦️
↓
Data Processing & Feature Engineering 📊
↓
Machine Learning Model 🤖
↓
Streamlit Dashboard 🌐


---

## ⚙️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Google Earth Engine API
- Streamlit
- Matplotlib

---

## 📈 Features

✅ NDVI extraction from satellite imagery  
✅ Weather data integration  
✅ Machine Learning prediction (Random Forest)  
✅ Interactive dashboard with visualization  
✅ Real-time NDVI prediction using user inputs  

---

## 📊 Dashboard Preview

<!-- Add your screenshot here -->
![Dashboard Screenshot](dashboard/screenshot.png)

---

## 🧪 Model Details

- Model: Random Forest Regressor
- Input Features:
  - Max Temperature
  - Min Temperature
  - Rainfall
- Target:
  - NDVI

### 📉 Performance

- Mean Squared Error (MSE): ~0.006  
- RMSE: ~0.07  

---

## 📁 Project Structure
agri_emission_project/
│
├── data/
│ └── final_dataset.csv
├── dashboard/
│ └── app.py
├── models/
│ └── model.pkl (ignored)
├── scripts/
├── README.md


---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/agri-emission-ml-dashboard.git
cd agri-emission-ml-dashboard

pip install -r requirements.txt
streamlit run dashboard/app.py


🌍 Future Improvements
Add geospatial map visualization (Folium)
Improve model with time-series features
Deploy on cloud (Streamlit Cloud / AWS)
Add multi-location support
