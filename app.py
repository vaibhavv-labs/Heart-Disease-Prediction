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
st.write("Dataset: Heart Disease Dataset (Kaggle, originally from UCI Repository)")
st.write("Model Accuracy: 82%")

# ---------- HOW IT WORKS ----------
st.markdown("### ⚙️ How This Works")
st.write("This system uses a Machine Learning model trained on healthcare data to predict heart disease risk based on patient inputs.")

st.markdown("## 🫀 Enter Patient Data")

# ---------- INPUT SECTION ----------
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 1, 120, 45)
    sex = st.selectbox("Sex", ["Female", "Male"])
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    restecg = st.selectbox("Rest ECG", [0, 1, 2])

with col2:
    trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
    chol = st.number_input("Cholesterol", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar >120", ["No", "Yes"])

with col3:
    thalach = st.number_input("Max Heart Rate", value=150)
    exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
    oldpeak = st.number_input("Oldpeak", value=1.0)

slope = st.selectbox("Slope", [0, 1, 2])
ca = st.number_input("Number of Major Vessels", value=0)
thal = st.selectbox("Thal", [0, 1, 2, 3])

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
        prob = model.predict_proba(input_data)

    st.markdown("### 🩺 Prediction Result")

    if prediction[0] == 0:
        st.success("💚 Low Risk of Heart Disease")
        st.write("Maintain a healthy lifestyle and regular checkups.")
    else:
        st.error("💔 High Risk of Heart Disease")
        st.write("Consult a doctor and improve lifestyle habits immediately.")

    # ---------- CONFIDENCE ----------
    st.write(f"🔍 Confidence: {prob[0][1]*100:.2f}%")

    # ---------- REASONS ----------
    st.markdown("### 🔍 Possible Reasons (Based on Input Patterns)")

    reasons = []

    if age > 50:
        reasons.append("Higher age increases heart disease risk")

    if chol > 240:
        reasons.append("High cholesterol level")

    if trestbps > 140:
        reasons.append("High blood pressure")

    if exang == 1:
        reasons.append("Exercise induced angina")

    if thalach < 100:
        reasons.append("Low maximum heart rate")

    if oldpeak > 2:
        reasons.append("High ST depression (oldpeak)")

    if cp == 0:
        reasons.append("Typical chest pain type")

    # Show reasons
    if len(reasons) > 0:
        for r in reasons:
            st.write(f"• {r}")
    else:
        st.write("No strong risk factors detected")

    st.info("⚠️ This prediction is for educational purposes only. Not medical advice.")

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built by Vaibhav Bhoyate | AI & Data Science Project")
st.markdown("🔗 [View Source Code](https://github.com/vaibhavv-labs/Heart-Disease-Prediction)")
