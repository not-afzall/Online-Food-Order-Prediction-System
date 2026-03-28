# 🍔 Online Food Order Prediction System

## Overview

This project predicts whether a customer will place a food order using a machine learning model. It includes data preprocessing, model training, and a simple web interface for predictions.

## Tech Stack

Python, Pandas, NumPy, Scikit-learn, Flask, HTML

## Features

* Data preprocessing and encoding
* Random Forest model for prediction
* Model evaluation using accuracy and confusion matrix
* Simple web interface using Flask

## Project Structure

food-order-prediction/
├── food_order_data.csv
├── model_training.py
├── app.py
├── requirements.txt
├── README.md
└── templates/
  └── index.html

## Dataset

The dataset contains features such as Age, Gender, Location, Income, and Order History.
Target variable: Ordered (Yes/No)

## How to Run

Clone the repository and install dependencies using `pip install -r requirements.txt`
Run `model_training.py` to train the model
Run `app.py` and open `http://127.0.0.1:5000` in your browser

## Future Improvements

Improve model accuracy, add more features, and deploy the application online

## Author

Mohammed Abzel F
