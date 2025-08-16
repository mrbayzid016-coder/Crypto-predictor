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
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Crypto Predictor API is running 🚀"})

# নতুন প্রেডিকশন এন্ডপয়েন্ট
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # ইউজার থেকে ডেটা নেবে (coin name, time frame ইত্যাদি)
    coin = data.get("coin", "BTC")
    timeframe = data.get("timeframe", "1h")

    # ডেমো প্রেডিকশন লজিক (random signal)
    signals = ["BUY", "SELL", "HOLD"]
    prediction = random.choice(signals)

    return jsonify({
        "coin": coin,
        "timeframe": timeframe,
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
