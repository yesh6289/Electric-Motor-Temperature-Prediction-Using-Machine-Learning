
import numpy as np
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("model.save")
scaler = joblib.load("transform.save")

@app.route("/")
def home():
    return render_template("manual_predict.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    features = [0] + features  # Add a zero at the beginning for the intercept term
    final = scaler.transform([features])
    prediction = model.predict(final)
    return render_template("sensor_predict.html",
                           prediction_text=f"Predicted Motor Temperature: {prediction[0]:.2f}")

if __name__ == "__main__":
    app.run(debug=True)
