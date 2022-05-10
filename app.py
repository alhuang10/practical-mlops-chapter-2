from flask import Flask, request
from textblob import TextBlob

app = Flask(__name__)


@app.route('/health')
def health():
    return "", 200

@app.route('/sentiment', methods=['POST'])
def sentiment():
    text = request.form.get('text')
    testimonial = TextBlob(text)
    sentiment_score_str = str(testimonial.polarity)
    return sentiment_score_str, 200