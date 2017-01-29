import tweepy
from tweepy import OAuthHandler


def authorize(consumer_key,consumer_secret,access_token,access_token_secret):
    __auth = OAuthHandler(consumer_key, consumer_secret)
    __auth.set_access_token = (access_token, access_token_secret)
    return __auth

def get_tweet(screen,__auth):
    api=tweepy.API(__auth)
    tweets=[]
    new_tweets=api.user_timeline(screen_name=screen,count=1)
    tweets.extend(new_tweets)
    oldest=tweets[-1].id - 1

    while len(new_tweets)>0:
        new_tweets = api.user_timeline(screen_name=screen,count=200,max_id=oldest)
        for user in new_tweets:
            print(user.text)
        tweets.extend(new_tweets)
        oldest=tweets[-1].id-1




