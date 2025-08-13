from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Load model
sentiment_analyzer = pipeline("sentiment-analysis")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = sentiment_analyzer(text)[0]  # e.g. {'label': 'POSITIVE', 'score': 0.99}
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
