# preprocess.py

import re
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def clean_text(text):
    # Remove special characters and URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove URLs
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)  # Remove punctuation
    return text

def preprocess_tweets(tweet_data):
    processed_data = []
    for tweet in tweet_data:
        cleaned_text = clean_text(tweet["text"])
        processed_data.append({
            "text": cleaned_text,
            "created_at": tweet["created_at"],
            "user": tweet["user"],
        })
    return processed_data
