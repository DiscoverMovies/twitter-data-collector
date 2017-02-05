#__all__=["database","twitter_data","database_create"]

import tweepy

from twitter_data_collector import database
from twitter_data_collector import twitter_data

class TwitterDataCollector:
    def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret,username,password,screen):
        self.consumer_key=consumer_key
        self.consumer_secret=consumer_secret
        self.access_token=access_token
        self.access_token_secret=access_token_secret
        self.username=username
        self.password=password
        self.screen=screen

    def set_database(self):
        auth1=twitter_data.authorize(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)
        database.initial(self.username,self.password)
        return auth1

    def insert_user_data(self,auth1):
        twitter_data.get_data(self.screen,auth1)
        twitter_data.get_tweet(self.screen,auth1)
