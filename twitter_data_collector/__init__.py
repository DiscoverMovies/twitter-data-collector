import tweepy

from twitter_data_collector import database
from twitter_data_collector import twitter_data


class TwitterDataCollector:
    def __init__(self, access_token, access_token_secret, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.auth = twitter_data.authorize(consumer_key, consumer_secret)
        self.auth.set_access_token = (access_token, access_token_secret)
        self.db = None

    def set_database(self, username, password):
        self.db = database.DatabaseTwitter(username, password)

    def insert_user_data(self, screen):
        data = twitter_data.get_data(self.auth, screen)
        tweets = twitter_data.get_tweet(self.auth, screen)
        self.db.insert_user(data)
        self.db.insert_tweet(tweets,data)
