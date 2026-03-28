from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model and encoders
model = pickle.load(open("model.pkl", "rb"))
le_gender, le_location, le_target = pickle.load(open("encoders.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    gender = le_gender.transform([request.form['gender']])[0]
    location = le_location.transform([request.form['location']])[0]
    income = int(request.form['income'])
    history = int(request.form['history'])

    features = np.array([[age, gender, location, income, history]])
    prediction = model.predict(features)
    result = le_target.inverse_transform(prediction)[0]

    return render_template('index.html', prediction_text=f"Prediction: {result}")

if __name__ == '__main__':
    app.run(debug=True)