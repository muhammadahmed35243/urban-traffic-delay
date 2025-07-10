# 🚦 Urban Traffic Delay Prediction

This project predicts **hourly traffic volume** on urban highways based on weather conditions, time, and holiday features using machine learning models. It includes data preprocessing, feature engineering, model training, evaluation, and deployment with Streamlit.

---

## 📌 Key Highlights

- **Model Used:** XGBoost (Best Performance)
- **Goal:** Predict `traffic_volume` using weather + time data
- **Source Dataset:** Metro Interstate Traffic Volume (Kaggle)
- **Visualization:** Correlation heatmap, feature importance, residuals
- **Deployment:** Streamlit App

---

## 📁 Project Structure

```
urban-traffic-delay/
│
├── app/                     # Streamlit App
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── Metro_Interstate_Traffic_Volume.csv
│   ├── cleaned/
│   │   ├── cleanedMITV.csv
│   │   └── final_engineered_MITV.csv
│   └── splits/
│       ├── X_train.csv, X_val.csv, X_test.csv
│       └── y_train.csv, y_val.csv, y_test.csv
│
├── models/
│   ├── xgboost_model.pkl
│   └── feature_columns.pkl
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_evaluation_visuals.ipynb
│
├── outputs/
│   ├── feature_importance.png
│   ├── full_correlation_heatmap.png
│   ├── top15_corr_heatmap.png
│   ├── val_actual_vs_pred.png
│   └── val_residuals.png
│
├── src/
│   └── predict.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📊 Features Used

- Numerical: `temp`, `rain_1h`, `snow_1h`, `clouds_all`, `hour`, `day`, `month`, `dayofweek`
- Categorical (one-hot encoded):  
  - `holiday_*`  
  - `weather_main_*`  
  - `weather_description_*`
- Engineered:
  - `is_weekend`
  - `is_peak_hour`
  - `weather_severity`

---

## 📈 Model Performance

| Model        | RMSE   | R² Score |
|--------------|--------|----------|
| Lasso        | 1577   | 0.37     |
| **XGBoost**  | **383**| **0.96** |

---

## 💻 How to Run Locally

### 1. Setup Environment

```bash
git clone https://github.com/your-username/urban-traffic-delay.git
cd urban-traffic-delay
python -m venv .venv
.venv\Scripts\activate        # On Windows
pip install -r requirements.txt
```

### 2. Launch App

```bash
streamlit run app/app.py
```

---

## 🌍 Deployment (Streamlit Cloud)

1. Push repo to GitHub
2. Go to: [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect GitHub → Select repo
4. Set entrypoint: `app/app.py`
5. Click Deploy 🚀

---

## 🔮 Future Ideas

- Auto-retraining on uploaded CSV
- Weather API for real-time prediction
- Dashboard for model comparison
- Save uploaded predictions to database

---

## ✍️ Author

**Muhammad Ahmed — "Electron ⚡"**  
GitHub: [muhammadahmed35243](https://github.com/muhammadahmed35243)  
Inspired by Andrew Ng’s ML Specialization

---
