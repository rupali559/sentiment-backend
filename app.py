from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Load a smaller model to save memory
model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    
    result = model(text)[0]
    sentiment = result['label']
    
    return jsonify({
        "sentiment": sentiment,
        "score": result['score']
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))