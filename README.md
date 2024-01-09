---

# Loan Eligibility Prediction Project

## Overview

This project aims to automate the loan eligibility process for Dream Housing Finance Company. The company receives online applications for home loans and wants to identify eligible customer segments based on various criteria, such as gender, marital status, education, income, credit history, and more. The goal is to develop a real-time loan eligibility prediction system to streamline the loan approval process.

## Problem Statement

Dream Housing Finance Company deals with home loans across urban, semi-urban, and rural areas. The traditional loan eligibility process involves manual validation of customer details, but the company now seeks an automated solution. The challenge is to predict loan eligibility based on customer information provided in the online application form.

The company aims to target specific customer segments that are eligible for a loan amount, enhancing efficiency and customer satisfaction.

## Dataset

The dataset provided is a partial set containing customer details. It serves as the foundation for training and testing the loan eligibility prediction model.

## Project Structure

```
|-- Dataset/
|   |-- train_data.csv
|   |-- train_data.csv
|-- notebooks/
|   |-- Loan_Eligibility_Prediction.ipynb
|-- app.py
|-- requirements.txt
|-- README.md
```

## Web Application

The `app.py` script implements a Flask web application for real-time loan eligibility prediction. Users can input their details, and the system provides instant eligibility results.

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/JenishRevaldo/End-to-End-Loan-Eligibility-Prediction-ML.git
   cd loan-eligibility-prediction
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Explore the Jupyter notebook (`notebooks/Loan_Eligibility_Prediction.ipynb`) for insights into data analysis and model development.

4. Run the Flask web application:

   ```bash
   python app.py
   ```

   Visit `http://localhost:5000` in your web browser to access the loan eligibility prediction application.

## Conclusion

This project demonstrates the development of an end-to-end solution for automating loan eligibility prediction. The model can be trained on a larger dataset for enhanced accuracy and deployed as a real-time web application.

---
