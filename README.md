# Electric Motor Temperature Prediction Using Machine Learning

## Project Overview

This project predicts electric motor temperature using machine learning
models based on sensor data.\
It includes data preprocessing, model training, evaluation, and
deployment using a Flask web application.

## Features

-   Data preprocessing (missing values, normalization, feature
    selection)
-   Machine learning models:
    -   Linear Regression
    -   Decision Tree Regressor
    -   Random Forest Regressor
    -   Support Vector Machine (SVR)
-   Model evaluation using:
    -   R² Score
    -   RMSE
-   Flask web app for real-time prediction
-   HTML + CSS frontend interface

## Project Structure

    Virtual_Internship/
    │
    ├── Flask/
    │   ├── app.py
    │   ├── model.save
    │   ├── transform.save
    │   └── templates/
    │       ├── manual_predict.html
    │       └── result.html
    │
    ├── Dataset.zip
    ├── Electric_Motor_Project_Final_With_Evaluation.ipynb
    ├── Electric_Motor_Temperature_Prediction_Project.docx
    ├── model.save
    ├── pmss_temperature_data.csv
    ├── README.md
    └── transform.save


## Requirements

Install dependencies:

    pip install numpy pandas scikit-learn flask joblib matplotlib seaborn

## Running the Project

### 1. Train Model

Run the Jupyter notebook:

    Electric_Motor_Project_Final_With_Evaluation.ipynb

### 2. Start Flask App

    cd Flask
    python app.py

Open browser:

    http://127.0.0.1:5000/

## Input Features

-   Ambient Temperature
-   Coolant Temperature
-   Voltage d-component
-   Voltage q-component
-   Motor Speed
-   Current d-component
-   Current q-component

## Output

Predicted electric motor temperature.

## Future Improvements

-   Hyperparameter tuning
-   Deep learning models
-   Cloud deployment
-   Real-time IoT sensor integration

------------------------------------------------------------------------

**Author:** Yeshwanth N\
Machine Learning Internship Project
