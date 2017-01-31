import tweepy
import database
import twitter_data


def database_twitter(consumer_key,consumer_secret,access_token,access_token_secret ):
    __auth = twitter_data.authorize(consumer_key,consumer_secret,access_token,access_token_secret)
    return __auth

def set_database(username,passwd):
    database.initial(username,passwd)

def insert_user_data(screen,auth):
    twitter_data.get_data(screen,auth)
    twitter_data.get_tweet(screen,auth)


class database_twitter:
    __access_token = none
    __access_token_secret = none
    __consumer_key = none
    __consumer_secret = none
    __screen = none
    __auth=database_twitter(__consumer_key,__consumer_secret,__access_token,__access_token_secret)
    set_database('root', 'asdf123!@')
    insert_user_data(__screen,__auth)