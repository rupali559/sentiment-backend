from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Sentiment Analysis API is running. Use POST /analyze"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
