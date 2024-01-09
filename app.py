#import necessary libraries
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle

# Load your trained model using pickle
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('encoder.pkl', 'rb') as file:
    label_encoders = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        self_employed = request.form['self_employed']
        applicant_income = float(request.form['applicant_income'])
        coapplicant_income = float(request.form['coapplicant_income'])
        loan_amount = float(request.form['loan_amount'])
        loan_term = float(request.form['loan_term'])
        credit_history = float(request.form['credit_history'])
        property_area = request.form['property_area']

        # Create a DataFrame with the user input
        data = pd.DataFrame({
            'Gender': [gender],
            'Married': [married],
            'Dependents': [dependents],
            'Education': [education],
            'Self_Employed': [self_employed],
            'ApplicantIncome': [applicant_income],
            'CoapplicantIncome': [coapplicant_income],
            'LoanAmount': [loan_amount],
            'Loan_Amount_Term': [loan_term],
            'Credit_History': [credit_history],
            'Property_Area': [property_area]
        })

        for column, encoder in label_encoders.items():
            data[column] = encoder.transform(data[column])

        x = scaler.transform(data)
        y_pred = model.predict(x)[0]

        if y_pred == 1:
            prediction = 'You are eligible for Loan'
        else:
            prediction = 'You are not eligible for Loan'

        return render_template('result.html', results = prediction)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
