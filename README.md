#  Early Prediction of Cardiac Arrest using Random Forest Classifier

##  Project Overview
This project is a Machine Learning-based system that predicts the risk of cardiac arrest using patient health parameters. It uses a Random Forest Classifier and is deployed using a Gradio web interface.

---

##  Model Used
- Random Forest Classifier
- SMOTE for handling class imbalance
- Feature importance analysis

---

## Dataset Features
- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Rest ECG (restecg)
- Max Heart Rate (thalach)
- Exercise Induced Angina (exang)
- Oldpeak
- Slope
- CA
- Thal

---

## Web Application
Built using **Gradio** for interactive prediction.

### How to Run
```bash
pip install -r requirements.txt
python app.py
