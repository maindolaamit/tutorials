import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Import the required libraries for text claning
import string
import re
import nltk

def get_data():
    df = pd.read_csv("Tweets.csv")
    # Drop unwanted columns
    df.drop(axis=1, labels=['tweet_id','name','negativereason_gold','airline_sentiment_gold',
                            'tweet_coord', 'tweet_created', 'tweet_location', 'user_timezone',
                           'retweet_count']
            , inplace=True)
    df['negativereason_confidence'].fillna(0, inplace=True)
    return df
    

def main():
    df = pd.read_csv("Tweets.csv")
    print(f"DataFrame shape, Rows :{df.shape[0]} Columns : {df.shape[1]}")

if __name__ == '__main__':
    main()
