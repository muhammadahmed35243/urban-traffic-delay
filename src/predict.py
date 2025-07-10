# --- src/predict.py ---

import pandas as pd
import joblib
import os

# --- Load model ---
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "models", "xgboost_model.pkl")
model = joblib.load(model_path)

# --- Load the actual feature list used during training ---
features_path = os.path.join(BASE_DIR, "models", "feature_columns.pkl")
all_features = joblib.load(open(features_path, "rb"))

def prepare_input(user_input: dict):
    row = dict.fromkeys(all_features, 0)

    # Fill base numeric values
    for key in ['temp', 'rain_1h', 'snow_1h', 'clouds_all', 'hour', 'day', 'month', 'dayofweek']:
        if key in row:
            row[key] = user_input[key]

    # One-hot encode fields if they exist
    holiday_key = f"holiday_{user_input['holiday']}"
    if holiday_key in row:
        row[holiday_key] = 1

    weather_main_key = f"weather_main_{user_input['weather_main']}"
    if weather_main_key in row:
        row[weather_main_key] = 1

    weather_desc_key = f"weather_description_{user_input['weather_description']}"
    if weather_desc_key in row:
        row[weather_desc_key] = 1

    # Optional: engineered features (if needed)
    if 'is_weekend' in row:
        row['is_weekend'] = int(user_input['dayofweek'] in [5, 6])

    if 'is_peak_hour' in row:
        row['is_peak_hour'] = int(user_input['hour'] in [7, 8, 16, 17])

    if 'weather_severity' in row:
        row['weather_severity'] = int(user_input['rain_1h'] > 0 or user_input['snow_1h'] > 0)

    return pd.DataFrame([row])

def predict(user_input: dict):
    X = prepare_input(user_input)
    prediction = model.predict(X)[0]
    return int(prediction)
