from flask import Flask, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def home():
    html = "<h3>TextBlob Sentiment Prediction Home: From Azure Pipelines (Continuous Delivery)</h3>"
    return html.format(format)


@app.route('/sentiment', methods=['POST'])
def sentiment():
    """
    Example POST request
    
    curl -X POST https://sentiment-ml-service.azurewebsites.net/sentiment \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "text=the soup was great"
    """
    text = request.form.get('text')
    testimonial = TextBlob(text)
    sentiment_score_str = str(testimonial.polarity)
    return f"The sentiment score is {sentiment_score_str}\n", 200