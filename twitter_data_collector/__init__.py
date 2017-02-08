

import tweepy

from twitter_data_collector import database
from twitter_data_collector import twitter_data


class TwitterDataCollector:
    def __init__(self,access_token,access_token_secret,consumer_key,consumer_secret,username,password,screen):
        self.consumer_key=consumer_key
        self.consumer_secret=consumer_secret
        self.access_token=access_token
        self.access_token_secret=access_token_secret
        self.username=username
        self.password=password
        self.screen=screen

    def set_database(self):
        auth=twitter_data.authorize(self)
        database.initial(self)
        return auth


    def insert_user_data(self,auth):
        twitter_data.get_data(self,auth)
        twitter_data.get_tweet(self,auth)
