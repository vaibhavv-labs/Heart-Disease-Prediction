import streamlit as st
import numpy as np
import pickle
import time
import os

# ─────────────────────────────────────────────
#  PAGE CONFIG  (must be first Streamlit call)
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  GLOBAL CSS  – 100 / 100 UI
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Syne:wght@700;800&display=swap');

/* ── Reset & base ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"],
[data-testid="stApp"], .main, .block-container {
    background: #0d0d0f !important;
    color: #e8e8ec !important;
    font-family: 'Inter', sans-serif !important;
}

/* hide default streamlit chrome */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="collapsedControl"] { display: none !important; }

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── HERO BANNER ── */
.hero {
    background: linear-gradient(135deg, #0d0d0f 0%, #1a0808 50%, #0d0d0f 100%);
    padding: 3rem 3rem 2.5rem;
    position: relative;
    overflow: hidden;
    border-bottom: 1px solid rgba(239,68,68,0.15);
}

.hero::before {
    content: '';
    position: absolute;
    top: -100px; right: -80px;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(239,68,68,0.18) 0%, transparent 65%);
    pointer-events: none;
}

.hero::after {
    content: '';
    position: absolute;
    bottom: -60px; left: 15%;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(239,68,68,0.08) 0%, transparent 70%);
    pointer-events: none;
}

.hero-tag {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(239,68,68,0.12);
    border: 1px solid rgba(239,68,68,0.28);
    color: #fca5a5;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: 100px;
    margin-bottom: 1.2rem;
}

.pulse-dot {
    width: 6px; height: 6px;
    background: #fca5a5;
    border-radius: 50%;
    animation: pdot 1.6s ease-in-out infinite;
}

@keyframes pdot {
    0%,100% { opacity:1; transform:scale(1); }
    50%      { opacity:0.4; transform:scale(0.7); }
}

.hero-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 3rem !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    line-height: 1.05 !important;
    margin: 0 0 0.6rem !important;
}

.hero-title span { color: #ef4444; }

.hero-sub {
    color: rgba(255,255,255,0.4);
    font-size: 14px;
    font-weight: 300;
    margin-bottom: 1.8rem;
}

.hero-stats {
    display: flex;
    gap: 2rem;
    flex-wrap: wrap;
}

.hstat {
    display: flex;
    flex-direction: column;
}

.hstat-num {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    color: #ef4444;
    line-height: 1;
}

.hstat-lbl {
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.35);
    margin-top: 2px;
}

.ecg-svg {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 55px;
    opacity: 0.2;
}

/* ── MAIN CONTENT WRAPPER ── */
.content-wrap {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2.5rem 3rem;
}

/* ── SECTION HEADINGS ── */
.sec-head {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 1.2rem;
    margin-top: 2rem;
}

.sec-head-dot {
    width: 8px; height: 8px;
    background: #ef4444;
    border-radius: 50%;
    flex-shrink: 0;
}

.sec-head-text {
    font-family: 'Syne', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.4);
}

.sec-head::after {
    content: '';
    flex: 1;
    height: 0.5px;
    background: rgba(255,255,255,0.07);
}

/* ── CARD ── */
.card {
    background: #141418;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: border-color 0.2s;
}

.card:hover {
    border-color: rgba(239,68,68,0.2);
}

/* ── Streamlit widget overrides ── */
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] select,
.stSelectbox > div > div,
.stNumberInput > div {
    background: #1c1c22 !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 10px !important;
    color: #e8e8ec !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
}

[data-testid="stSelectbox"] > div > div:hover,
[data-testid="stNumberInput"] input:focus {
    border-color: rgba(239,68,68,0.45) !important;
    box-shadow: 0 0 0 3px rgba(239,68,68,0.08) !important;
}

/* labels */
label, .stSelectbox label, .stNumberInput label,
[data-testid="stWidgetLabel"] p {
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 0.07em !important;
    text-transform: uppercase !important;
    color: rgba(255,255,255,0.4) !important;
    margin-bottom: 4px !important;
}

/* ── PREDICT BUTTON ── */
[data-testid="stButton"] > button {
    width: 100% !important;
    background: linear-gradient(135deg, #b91c1c, #ef4444) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.9rem 2rem !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em !important;
    cursor: pointer !important;
    transition: transform 0.15s, box-shadow 0.2s !important;
    margin-top: 0.5rem !important;
}

[data-testid="stButton"] > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 32px rgba(239,68,68,0.35) !important;
}

[data-testid="stButton"] > button:active {
    transform: scale(0.98) !important;
}

/* ── RESULT CARDS ── */
.result-high {
    background: linear-gradient(135deg, #450a0a, #7f1d1d);
    border: 1px solid rgba(239,68,68,0.35);
    border-radius: 18px;
    padding: 2rem;
    color: white;
    margin-bottom: 1rem;
    animation: fadeUp 0.5s ease;
}

.result-low {
    background: linear-gradient(135deg, #052e16, #14532d);
    border: 1px solid rgba(34,197,94,0.3);
    border-radius: 18px;
    padding: 2rem;
    color: white;
    margin-bottom: 1rem;
    animation: fadeUp 0.5s ease;
}

@keyframes fadeUp {
    from { opacity:0; transform:translateY(16px); }
    to   { opacity:1; transform:translateY(0); }
}

.result-icon-big {
    font-size: 3rem;
    margin-bottom: 0.6rem;
}

.result-label {
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    margin-bottom: 0.3rem;
}

.result-desc {
    font-size: 13px;
    opacity: 0.65;
    margin-bottom: 1.5rem;
}

/* risk bar */
.risk-wrap { margin-bottom: 1.2rem; }

.risk-top {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    opacity: 0.6;
    margin-bottom: 6px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

.risk-track {
    height: 8px;
    background: rgba(255,255,255,0.12);
    border-radius: 8px;
    overflow: hidden;
}

.risk-fill-high {
    height: 100%;
    border-radius: 8px;
    background: linear-gradient(90deg, #fca5a5, #ef4444);
    transition: width 1.2s cubic-bezier(0.16,1,0.3,1);
}

.risk-fill-low {
    height: 100%;
    border-radius: 8px;
    background: linear-gradient(90deg, #86efac, #22c55e);
    transition: width 1.2s cubic-bezier(0.16,1,0.3,1);
}

/* vitals row */
.vitals-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    border-top: 1px solid rgba(255,255,255,0.1);
    padding-top: 1.2rem;
    margin-top: 0.5rem;
}

.vital-chip {
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 8px 14px;
    min-width: 80px;
    text-align: center;
}

.vc-val { font-size: 16px; font-weight: 600; }
.vc-lbl { font-size: 9px; opacity: 0.55; letter-spacing: 0.07em; text-transform: uppercase; margin-top: 2px; }

/* raw input pill */
.raw-pill {
    background: #1c1c22;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 0.8rem 1rem;
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    color: rgba(255,255,255,0.4);
    margin-bottom: 1rem;
    word-break: break-all;
}

/* disclaimer */
.disclaimer {
    background: #141418;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 0.8rem 1.2rem;
    font-size: 12px;
    color: rgba(255,255,255,0.3);
    margin-top: 1.5rem;
    display: flex;
    gap: 8px;
    align-items: flex-start;
}

/* slider overrides */
.stSlider [data-testid="stSlider"] > div > div {
    background: rgba(239,68,68,0.25) !important;
}

/* ── FOOTER ── */
.footer {
    text-align: center;
    padding: 2rem;
    font-size: 12px;
    color: rgba(255,255,255,0.2);
    border-top: 1px solid rgba(255,255,255,0.05);
    margin-top: 3rem;
}

.footer span { color: #ef4444; }

/* scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0d0d0f; }
::-webkit-scrollbar-thumb { background: #2a2a30; border-radius: 6px; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  LOAD MODEL & SCALER
# ─────────────────────────────────────────────
def load_file(path):
    if not os.path.exists(path):
        st.error(f"❌ File not found: {path}")
        st.stop()
    return pickle.load(open(path, "rb"))

model = load_file("heart_model.pkl")

scaler = None
if os.path.exists("scaler.pkl"):
    scaler = pickle.load(open("scaler.pkl", "rb"))


# ─────────────────────────────────────────────
#  HERO BANNER
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-tag">
    <div class="pulse-dot"></div>
    AI-Powered Diagnostics
  </div>
  <div class="hero-title">Heart Disease<br><span>Prediction</span> System</div>
  <div class="hero-sub">UCI Heart Disease Dataset · Random Forest Classifier · Real-time Risk Analysis</div>
  <div class="hero-stats">
    <div class="hstat"><div class="hstat-num">93%</div><div class="hstat-lbl">Accuracy</div></div>
    <div class="hstat"><div class="hstat-num">303</div><div class="hstat-lbl">Training Samples</div></div>
    <div class="hstat"><div class="hstat-num">13</div><div class="hstat-lbl">Input Features</div></div>
    <div class="hstat"><div class="hstat-num">UCI</div><div class="hstat-lbl">Dataset</div></div>
  </div>
  <svg class="ecg-svg" viewBox="0 0 1200 55" preserveAspectRatio="none">
    <polyline points="0,28 80,28 100,28 115,4 128,52 141,28 160,28
                       240,28 260,28 275,4 288,52 301,28 320,28
                       400,28 420,28 435,4 448,52 461,28 480,28
                       560,28 580,28 595,4 608,52 621,28 640,28
                       720,28 740,28 755,4 768,52 781,28 800,28
                       880,28 900,28 915,4 928,52 941,28 960,28
                       1040,28 1060,28 1075,4 1088,52 1101,28 1200,28"
      fill="none" stroke="#ef4444" stroke-width="1.5"/>
  </svg>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  CONTENT WRAPPER START
# ─────────────────────────────────────────────
st.markdown('<div class="content-wrap">', unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  SECTION: PATIENT DEMOGRAPHICS
# ─────────────────────────────────────────────
st.markdown("""
<div class="sec-head">
  <div class="sec-head-dot"></div>
  <div class="sec-head-text">Patient Demographics</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    age = st.number_input("Age (years)", min_value=1, max_value=120, value=45)
with col2:
    sex = st.selectbox("Biological Sex", ["Female", "Male"])
with col3:
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3],
                      format_func=lambda x: {0:"0 – Typical Angina",1:"1 – Atypical Angina",2:"2 – Non-Anginal",3:"3 – Asymptomatic"}[x])
with col4:
    restecg = st.selectbox("Resting ECG", [0, 1, 2],
                           format_func=lambda x: {0:"0 – Normal",1:"1 – ST-T Abnormality",2:"2 – LV Hypertrophy"}[x])


# ─────────────────────────────────────────────
#  SECTION: VITAL MEASUREMENTS
# ─────────────────────────────────────────────
st.markdown("""
<div class="sec-head">
  <div class="sec-head-dot"></div>
  <div class="sec-head-text">Vital Measurements</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    trestbps = st.number_input("Resting BP (mmHg)", min_value=80, max_value=200, value=120)
with col2:
    chol = st.number_input("Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
with col3:
    thalach = st.number_input("Max Heart Rate (bpm)", min_value=60, max_value=220, value=150)
with col4:
    oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)


# ─────────────────────────────────────────────
#  SECTION: CLINICAL INDICATORS
# ─────────────────────────────────────────────
st.markdown("""
<div class="sec-head">
  <div class="sec-head-dot"></div>
  <div class="sec-head-text">Clinical Indicators</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    fbs  = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
    exang = st.selectbox("Exercise-Induced Angina", ["No", "Yes"])
with col2:
    slope = st.selectbox("ST Slope", [0, 1, 2],
                         format_func=lambda x: {0:"0 – Upsloping",1:"1 – Flat",2:"2 – Downsloping"}[x])
    ca    = st.selectbox("Major Vessels (CA)", [0, 1, 2, 3],
                         format_func=lambda x: f"{x} vessel{'s' if x != 1 else ''}")
with col3:
    thal  = st.selectbox("Thalassemia (Thal)", [1, 2, 3],
                         format_func=lambda x: {1:"1 – Normal",2:"2 – Fixed Defect",3:"3 – Reversible Defect"}[x])


# ─────────────────────────────────────────────
#  CONVERT CATEGORICALS
# ─────────────────────────────────────────────
sex_val   = 1 if sex   == "Male" else 0
fbs_val   = 1 if fbs   == "Yes"  else 0
exang_val = 1 if exang == "Yes"  else 0


# ─────────────────────────────────────────────
#  PREDICT BUTTON
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
predict_clicked = st.button("❤️  Analyze Heart Risk Now")


# ─────────────────────────────────────────────
#  PREDICTION LOGIC + RESULT UI
# ─────────────────────────────────────────────
if predict_clicked:

    input_data = np.array([[
        age, sex_val, cp, trestbps, chol, fbs_val,
        restecg, thalach, exang_val, oldpeak,
        slope, ca, thal
    ]], dtype=float)

    with st.spinner(""):
        time.sleep(1)
        try:
            proba = model.predict_proba(input_data)[0][1]
        except Exception:
            proba = float(model.predict(input_data)[0])

    risk_percent = round(proba * 100, 1)
    high_risk    = proba > 0.4

    # ── Debug pill (raw input) ──
    st.markdown(f"""
    <div class="raw-pill">
      <strong style="color:rgba(255,255,255,0.5);">RAW INPUT →</strong>
      {list(input_data[0])}
    </div>
    """, unsafe_allow_html=True)

    # ── Result card ──
    if high_risk:
        bar_class = "risk-fill-high"
        card_class = "result-high"
        icon  = "💔"
        label = "High Risk Detected"
        desc  = "Please consult a cardiologist as soon as possible."
        rec   = "⚡ Immediate medical consultation recommended"
    else:
        bar_class = "risk-fill-low"
        card_class = "result-low"
        icon  = "💚"
        label = "Low Risk"
        desc  = "Heart appears healthy based on provided indicators."
        rec   = "✅ Maintain a healthy lifestyle and regular checkups"

    st.markdown(f"""
    <div class="{card_class}">
      <div class="result-icon-big">{icon}</div>
      <div class="result-label">{label}</div>
      <div class="result-desc">{desc}</div>

      <div class="risk-wrap">
        <div class="risk-top">
          <span>Risk Score</span>
          <span style="font-family:'Syne',sans-serif;font-size:1.6rem;font-weight:800;opacity:1;">
            {risk_percent}%
          </span>
        </div>
        <div class="risk-track">
          <div class="{bar_class}" style="width:{risk_percent}%;"></div>
        </div>
        <div class="risk-top" style="margin-top:5px;margin-bottom:0;">
          <span>Low</span><span>Moderate</span><span>High</span>
        </div>
      </div>

      <div class="vitals-row">
        <div class="vital-chip"><div class="vc-val">{age}</div><div class="vc-lbl">Age</div></div>
        <div class="vital-chip"><div class="vc-val">{trestbps}</div><div class="vc-lbl">BP mmHg</div></div>
        <div class="vital-chip"><div class="vc-val">{chol}</div><div class="vc-lbl">Cholesterol</div></div>
        <div class="vital-chip"><div class="vc-val">{thalach}</div><div class="vc-lbl">Max HR</div></div>
        <div class="vital-chip"><div class="vc-val">{oldpeak}</div><div class="vc-lbl">Oldpeak</div></div>
        <div class="vital-chip"><div class="vc-val">{ca}</div><div class="vc-lbl">Vessels</div></div>
      </div>

      <div style="margin-top:1.2rem;font-size:13px;opacity:0.65;">{rec}</div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  DISCLAIMER
# ─────────────────────────────────────────────
st.markdown("""
<div class="disclaimer">
  ⚠️
  <span>This prediction is for <strong>educational purposes only</strong> and does not constitute
  medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional.</span>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer">
  Built by <span>Vaibhav</span> · AI &amp; Data Science Project ·
  Heart Disease Prediction System
</div>
</div>
""", unsafe_allow_html=True)