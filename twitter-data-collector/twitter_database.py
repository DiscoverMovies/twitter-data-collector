import tweepy
import twitter_data
class database_twitter:
    __access_token=none
    __access_token_secret=none
    __consumer_key=none
    __consumer_secret=none
    __screen=none
    __auth=twitter_data.authorize(__consumer_key,__consumer_secret,__access_token,__access_token_secret)
    twitter_data.get_tweet(__screen,__auth)
