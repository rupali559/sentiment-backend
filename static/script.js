document.getElementById('analyzeBtn').addEventListener('click', analyzeSentiment);

async function analyzeSentiment() {
    const text = document.getElementById('userText').value;
    const resultDiv = document.getElementById('result');
    
    if (!text.trim()) {
        alert('Please enter some text to analyze');
        return;
    }
    
    resultDiv.style.display = 'block';
    resultDiv.textContent = 'Analyzing...';
    resultDiv.className = 'loading';
    
    // try {
    //     const response = await fetch('/analyze', {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json',
    //         },
    //         body: JSON.stringify({ text: text })
    //     });

    try {
        const response = await fetch('http://127.0.0.1:5000/analyze', {  // <-- use backend URL
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        });
        
        const data = await response.json();
        
        // Update UI with result
        resultDiv.textContent = `Sentiment: ${data.sentiment} (${(data.score * 100).toFixed(1)}% confidence)`;
        
        // Apply color based on sentiment
        if (data.sentiment === 'Positive') {
            resultDiv.className = 'positive';
        } else if (data.sentiment === 'Negative') {
            resultDiv.className = 'negative';
        } else {
            resultDiv.className = 'neutral';
        }
        
    } catch (error) {
        resultDiv.textContent = 'Error analyzing text';
        resultDiv.className = 'negative';
        console.error('Error:', error);
    }
}