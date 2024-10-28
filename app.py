from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging
import traceback

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


def scale(payload):
    """Scales Payload"""

    LOG.info("Scaling Payload: %s", payload)
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict


@app.route("/")
def home():
    html = (
        "<h3>Boston Housing Price Prediction Home: From Azure Pipelines (Continuous Delivery)</h3>"
    )
    return html.format(format)


@app.route("/predict", methods=["POST"])
def predict():
    """Performs a prediction"""
    try:
        xgbr = joblib.load("models/xgb_housing_model.joblib")
    except Exception as e:
        LOG.error("Error loading model: %s", str(e))
        LOG.error("Exception traceback: %s", traceback.format_exc())
        return "Model not loaded"

    json_payload = request.json
    LOG.info("JSON payload: %s", json_payload)
    inference_payload = pd.DataFrame(json_payload)
    LOG.info("inference payload DataFrame: %s", inference_payload)
    scaled_payload = scale(inference_payload)
    prediction = list(xgbr.predict(scaled_payload))
    # Convert NumPy float32 to Python float
    prediction = [float(p) for p in prediction]
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
