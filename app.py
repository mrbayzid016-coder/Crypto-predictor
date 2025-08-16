from flask import Flask, jsonify
import pandas as pd
from indicators import generate_signals
from utils import get_latest_data

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Crypto Predictor API is running 🚀"}

@app.route("/predict", methods=["GET"])
def predict():
    df = get_latest_data()
    signal = generate_signals(df)
    return jsonify({"prediction": signal})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
