import streamlit as st
import numpy as np
import pickle
import time

st.set_page_config(page_title="Heart Health AI", layout="wide")

# ---------- TITLE ----------
st.title("❤️ Heart Disease Prediction System")
st.caption("AI-based system to predict heart disease risk")

# ---------- LOAD MODEL ----------
model = pickle.load(open("heart_model.pkl", "rb"))

# ---------- MODEL INFO ----------
st.markdown("### 🧠 Model Information")
st.write("Algorithm: Logistic Regression")
st.write("Dataset: UCI Heart Disease Dataset")
st.write("Accuracy: 82%")

st.markdown("## 🫀 Enter Patient Data")

# ---------- INPUT SECTION ----------
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=45)
    sex = st.selectbox("Sex", ["Female", "Male"])
    cp = st.number_input("Chest Pain Type", value=0)
    restecg = st.selectbox("Rest ECG", [0, 1, 2])

with col2:
    trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
    chol = st.number_input("Cholesterol", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar >120", ["No", "Yes"])

with col3:
    thalach = st.number_input("Max Heart Rate", value=150)
    exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
    oldpeak = st.number_input("Oldpeak", value=1.0)

slope = st.number_input("Slope", value=1)
ca = st.number_input("Number of Major Vessels", value=0)
thal = st.number_input("Thal", value=1)

# ---------- DATA CONVERSION ----------
sex = 1 if sex == "Male" else 0
fbs = 1 if fbs == "Yes" else 0
exang = 1 if exang == "Yes" else 0

# ---------- PREDICTION ----------
if st.button("🔍 Predict Now"):

    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])

    with st.spinner("Analyzing patient data..."):
        time.sleep(2)
        prediction = model.predict(input_data)

    st.markdown("### 🩺 Prediction Result")

    if prediction[0] == 0:
        st.success("💚 Low Risk of Heart Disease")
        st.write("Maintain a healthy lifestyle and regular checkups.")
    else:
        st.error("💔 High Risk of Heart Disease")
        st.write("Consult a doctor and improve lifestyle habits immediately.")

    st.info("⚠️ This prediction is for educational purposes only. Not medical advice.")

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built by Vaibhav Bhoyate | AI & Data Science Project")