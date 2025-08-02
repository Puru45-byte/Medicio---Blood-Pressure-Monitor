import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load ML model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form = request.form
        features = [float(form[field]) for field in [
            'Gender', 'Age', 'Patient', 'Severity', 'BreathShortness',
            'VisualChanges', 'NoseBleeding', 'Whendiagnosed', 'Systolic',
            'Diastolic', 'ControlledDiet'
        ]]
        
        df = pd.DataFrame([features], columns=[
            'Gender', 'Age', 'Patient', 'Severity', 'BreathShortness',
            'VisualChanges', 'NoseBleeding', 'Whendiagnosed', 'Systolic',
            'Diastolic', 'ControlledDiet'
        ])

        prediction = model.predict(df)

        if prediction[0] == 0:
            result = "NORMAL"
        elif prediction[0] == 1:
            result = "HYPERTENSION (Stage-1)"
        elif prediction[0] == 2:
            result = "HYPERTENSION (Stage-2)"
        else:
            result = "HYPERTENSIVE CRISIS"

        return render_template('form.html', prediction_text=f"Your Blood Pressure stage is: {result}")

    except Exception as e:
        return render_template('form.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
