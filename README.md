<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Space+Mono&size=30&pause=1000&color=FF4466&center=true&vCenter=true&width=700&lines=Heart+Disease+Prediction+%E2%9D%A4%EF%B8%8F;ML-Powered+Risk+Classification;Random+Forest+%C2%B7+93%25+Accuracy;Real-Time+%7C+Confidence+Score+%7C+Streamlit" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Accuracy](https://img.shields.io/badge/Accuracy-82%25-00FF88?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-ff4466?style=for-the-badge)

<br/>

> ❤️ **Predict heart disease risk in real-time using patient health data — powered by Machine Learning with confidence scores and risk explanations.**

<br/>

### 🔗 [Try Live Demo →](https://heart-disease-prediction-vaibhav.streamlit.app)

<br/>

![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=20&height=120&section=header&text=Heart+Disease+Prediction&fontSize=30&fontColor=ffffff&animation=fadeIn&desc=ML-Based+Healthcare+Risk+Classifier&descSize=15&descAlignY=78)

</div>

---

## 🎯 Project Overview

This project predicts heart disease risk using Machine Learning based on patient medical data. The goal is to transform healthcare data into actionable insights with an AI-based prediction system that's simple to use and understand.

---

## ✨ Features

| Feature | Description |
|---|---|
| ⚕️ **Real-Time Prediction** | Instant heart disease risk assessment |
| 🎛️ **User-Friendly Form** | Simple input form for patient health data |
| 📊 **Confidence Score** | Shows how confident the model is in its prediction |
| 🔴🟢 **Risk Classification** | Clear High Risk / Low Risk output |
| 💡 **Risk Explanations** | Tells you which factors are contributing to risk |
| 🚀 **Deployed on Streamlit** | Accessible from any browser, no install needed |

---

## 🔍 How It Works

```
  🏥 Patient Input Data
  (age, cholesterol, BP, chest pain type...)
           │
           ▼
  🧹 Data Preprocessing
  (feature scaling, encoding)
           │
           ▼
  🧠 Logistic Regression Model
  (trained on UCI Heart Disease dataset)
           │
           ├── Probability ≥ 0.5 ──▶ 🔴 HIGH RISK
           │
           └── Probability < 0.5 ──▶ 🟢 LOW RISK
                                          │
                                          ▼
                              💡 Confidence Score + Risk Factor Explanation
```

---

## 📊 Key Insights from Data

- 📈 High cholesterol significantly increases prediction risk
- 🩺 Age is one of the strongest indicators
- 💓 Exercise-induced angina is a major flag
- 🫀 Certain chest pain types are strong positive predictors
- 🩸 Blood pressure plays a consistent role across all cases

---

## 🚧 Challenges Faced & Solutions

| Challenge | Solution |
|---|---|
| Choosing the right ML algorithm | Tested multiple models → Logistic Regression gave best balance |
| Data preprocessing & feature handling | Used Scikit-learn pipelines for clean transformations |
| Designing a simple UI | Streamlit forms with clear labels and grouped inputs |
| Making predictions understandable | Added confidence scores + factor-level explanations |
| Deployment | Deployed via Streamlit Cloud with zero config |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/vaibhavv-labs/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Heart-Disease-Prediction/
│
├── app.py               # 🖥️  Streamlit dashboard
├── model.pkl            # 🧠  Trained ML model
├── requirements.txt     # 📦  Dependencies
└── README.md            # 📄  Documentation
```

---

## 📈 Model Performance

| Metric | Score |
|---|---|
| Algorithm | Random Forest |
| Accuracy | **93%** |
| Dataset | UCI Heart Disease |
| Features Used | 13 clinical features |

---

## 🗺️ Roadmap

- [ ] 🧠 Improve model with XGBoost / advanced tuning
- [ ] 📊 Add SHAP values for explainability
- [ ] 📋 Multi-patient batch prediction (CSV upload)
- [ ] 📱 Mobile-responsive UI improvements
- [ ] 🏥 Doctor-friendly PDF report export

---

## 🙋 Author

**Vaibhav Bhoyate**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vaibhav-bhoyate-6328802a9/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/vaibhavv-labs)
[![Portfolio](https://img.shields.io/badge/Portfolio-00FF88?style=for-the-badge&logo=vercel&logoColor=black)](https://portfolio-vaibhav13.vercel.app/)

---

## 📄 License

This project is licensed under the **MIT License.**

<div align="center">

⭐ **Star this repo if it helped you!** ⭐

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=20&height=100&section=footer)

</div>
