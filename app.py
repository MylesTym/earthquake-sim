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