# sentiment_analysis.py

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(tweet_data):
    sentiment_data = []
    for tweet in tweet_data:
        score = sia.polarity_scores(tweet["text"])
        sentiment_data.append({
            "text": tweet["text"],
            "sentiment": "positive" if score["compound"] > 0 else "negative" if score["compound"] < 0 else "neutral",
            "compound_score": score["compound"]
        })
    return sentiment_data
