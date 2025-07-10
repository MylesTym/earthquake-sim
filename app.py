import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import time
import matplotlib.pyplot as plt
import seaborn as sns

## —— Page set up ——
st.set_page_config(page_title="Earthquake Detecion Simulation", layout="centered")
st.title("Earthquake warning system")
st.markdown("Simulating real-time earthquakes using real data and anaomly detection")

## —— Page set up ——
st.set_page_config(page_title="Earthquake Detecion Simulation", layout="centered")
st.title("Earthquake warning system")
st.markdown("Simulating real-time earthquakes using real data and anaomly detection")

## —— Load data ——
@st.cache_data
def load_data():
    df = pd.read_csv("A3_data.csv")
    return df
df = load_data()

## —— Feature selection ——
features = df.columns[:5]
x = df[features]
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

## —— Model training ——
model = IsolationForest(contamination=0.01, random_state=25)
model.fit(x_scaled)
scores = model.decision_function(x_scaled)
preds = model.predict(x_scaled)

## —— Sidebar ——
st.sidebar.header("Simulation Settings")
threshold = st.sidebar.slider("Detection Threshold", float(min(scores)), float(max(scores)), float(np.percentile(scores, 1)), step=0.001)
speed = st.sidebar.slider("Simulation Speed", 0.01, 1.0, 0.1, 0.01)

## —— Streamlit ——
score_chart = st.line_chart()
alert_log = st.empty()

## —— Simulation loop ——
st.subheader("Anomaly Monitoring")
anomaly_log = []

for i in range(len(scores)):
    current_score = scores[i]

    score_chart.add_rows(pd.DataFrame([current_score], columns=["Anomaly Score"]))


    if current_score < threshold:
        anomaly_log.append(f"Anomaly at index {i} | Score: {current_score:.4f}")
    
    if anomaly_log:
        alert_log.markdown(" ### Alert Log")
        for msg in anomaly_log[-5:]:
            alert_log.markdown(f"- {msg}")
    
    time.sleep(speed)

st.success("Simulation complete.")