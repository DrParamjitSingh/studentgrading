# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 02:39:30 2025

@author: Dell
"""

# Python script starts here
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Model training data
X = np.array([
    [2, 50, 60, 5],
    [3, 60, 65, 6],
    [4, 55, 70, 6],
    [5, 70, 80, 7],
    [6, 80, 90, 8],
    [7, 85, 95, 8]
])
y = np.array([55, 65, 60, 75, 85, 90])
model = LinearRegression().fit(X, y)

# Web UI
st.title("🎓 Student Grade Predictor")

hours = st.slider("Hours Studied", 0, 10, 5)
past = st.slider("Past Score (%)", 0, 100, 60)
attn = st.slider("Attendance (%)", 0, 100, 80)
sleep = st.slider("Sleep Hours", 0, 12, 7)

if st.button("Predict Grade"):
    pred = model.predict([[hours, past, attn, sleep]])
    st.success(f"Predicted Final Grade: {pred[0]:.2f}%")
