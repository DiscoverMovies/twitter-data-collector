import tweepy
import twitter_data

access_token = None
access_token_secret = None
consumer_key = None
consumer_secret = None

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token = (access_token, access_token_secret)
twitter_data.getdata(screenname)
