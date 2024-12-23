# fetch_tweets.py

import tweepy
import json
import time
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Set up authentication
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def fetch_tweets_v2(query, count=100):
    tweet_data = []
    try:
        print(f"Fetching tweets for the query: '{query}'...")
        for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count):
            tweet_data.append({
                "text": tweet.full_text,
                "created_at": tweet.created_at,
                "user": tweet.user.screen_name
            })
        return tweet_data
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
