# main.py

from fetch_tweets import fetch_tweets_v2
from src.preprocess import preprocess_tweets
from src.sentiment_analysis import analyze_sentiment
from src.visualize import plot_sentiment_distribution

def main():
    query = "stock market"
    tweet_data = fetch_tweets_v2(query, count=100)

    if tweet_data:
        processed_data = preprocess_tweets(tweet_data)
        sentiment_data = analyze_sentiment(processed_data)
        plot_sentiment_distribution(sentiment_data)
    else:
        print("Failed to fetch tweets. Please try again later.")

if __name__ == "__main__":
    main()
