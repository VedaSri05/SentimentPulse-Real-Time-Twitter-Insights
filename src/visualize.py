# visualize.py

import matplotlib.pyplot as plt

def plot_sentiment_distribution(sentiment_data):
    sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}
    for sentiment in sentiment_data:
        sentiment_counts[sentiment["sentiment"]] += 1
    
    labels = sentiment_counts.keys()
    values = sentiment_counts.values()
    
    plt.bar(labels, values, color=["green", "red", "gray"])
    plt.title("Sentiment Distribution of Tweets")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()
