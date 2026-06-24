print("APP IS RUNNING")
import joblib
import pandas as pd
import gradio as gr

# load model
model = joblib.load("random_forest_model.pkl")

# prediction function
def predict(age, sex, cp, trestbps, chol, fbs, restecg,
            thalach, exang, oldpeak, slope, ca, thal):

    input_data = pd.DataFrame([[
        age, sex, cp, trestbps, chol, fbs, restecg,
        thalach, exang, oldpeak, slope, ca, thal
    ]], columns=[
        "age","sex","cp","trestbps","chol","fbs","restecg",
        "thalach","exang","oldpeak","slope","ca","thal"
    ])

    pred = model.predict(input_data)[0]

    if pred == 1:
        return "⚠ High Risk of Cardiac Arrest"
    else:
        return "✅ Low Risk of Cardiac Arrest"

# UI
iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Age"),
        gr.Number(label="Sex (1=Male,0=Female)"),
        gr.Number(label="Chest Pain Type"),
        gr.Number(label="Resting BP"),
        gr.Number(label="Cholesterol"),
        gr.Number(label="Fasting Blood Sugar"),
        gr.Number(label="Rest ECG"),
        gr.Number(label="Max Heart Rate"),
        gr.Number(label="Exercise Induced Angina"),
        gr.Number(label="Oldpeak"),
        gr.Number(label="Slope"),
        gr.Number(label="CA"),
        gr.Number(label="Thal")
    ],
    outputs="text",
    title="Cardiac Arrest Risk Predictor"
)

iface.launch(share=True)