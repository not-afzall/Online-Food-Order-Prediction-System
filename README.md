# 🍔 Online Food Order Prediction System

## Overview

This project predicts whether a customer will place a food order using a machine learning model. It covers data preprocessing, model training, and deployment using a simple web application.

## Tech Stack

Python, Pandas, NumPy, Scikit-learn, Flask, HTML

## Features

* Data preprocessing and encoding
* Random Forest model for prediction
* Accuracy and confusion matrix evaluation
* Simple web interface using Flask

## Project Structure

```
food-order-prediction/
├── food_order_data.csv
├── model_training.py
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## Dataset

Features include Age, Gender, Location, Income, Order History
Target: Ordered (Yes/No)

## How to Run

Clone the repository, install requirements using `pip install -r requirements.txt`, run `model_training.py`, then run `app.py` and open `http://127.0.0.1:5000` in your browser.

## Future Improvements

Add more features, improve model accuracy, and deploy the project online.

## Author

Mohammed Abzel F
