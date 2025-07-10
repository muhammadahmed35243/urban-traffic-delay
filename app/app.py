# app/app.py

import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from predict import predict

st.set_page_config(page_title="🚦 Traffic Volume Predictor", layout="centered")
st.title("🚦 Urban Traffic Volume Predictor")
st.markdown("Fill in the details to predict hourly traffic volume for urban roads.")

# --- User Inputs ---
temp = st.slider("Temperature (Kelvin)", 250.0, 320.0, 295.0)
rain_1h = st.number_input("Rain in last hour (mm)", 0.0, 50.0, 0.0)
snow_1h = st.number_input("Snow in last hour (mm)", 0.0, 50.0, 0.0)
clouds_all = st.slider("Cloud Cover (%)", 0, 100, 40)
hour = st.slider("Hour of Day", 0, 23, 8)
day = st.slider("Day of Month", 1, 31, 15)
month = st.slider("Month", 1, 12, 7)
dayofweek = st.selectbox("Day of Week (0=Mon, 6=Sun)", list(range(7)))

# --- Dropdowns ---
holiday = st.selectbox("Holiday", [
    "No Holiday", "Columbus Day", "Independence Day", "Labor Day",
    "Martin Luther King Jr Day", "Memorial Day", "New Years Day",
    "State Fair", "Thanksgiving Day", "Veterans Day", "Washingtons Birthday"
])

weather_main = st.selectbox("Weather Main", [
    "Clouds", "Drizzle", "Fog", "Haze", "Mist", "Rain",
    "Smoke", "Snow", "Squall", "Thunderstorm"
])

weather_description = st.selectbox("Weather Description", [
    "sky is clear", "few clouds", "scattered clouds", "broken clouds",
    "light rain", "moderate rain", "heavy intensity rain",
    "light snow", "mist"
])

# --- Prediction ---
if st.button("Predict Traffic Volume"):
    user_input = {
        "temp": temp,
        "rain_1h": rain_1h,
        "snow_1h": snow_1h,
        "clouds_all": clouds_all,
        "hour": hour,
        "day": day,
        "month": month,
        "dayofweek": dayofweek,
        "holiday": holiday,
        "weather_main": weather_main,
        "weather_description": weather_description
    }

    result = predict(user_input)
    st.success(f"🚗 Estimated Traffic Volume: **{result:,} vehicles/hour**")
