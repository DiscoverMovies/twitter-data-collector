import tweepy
from tweepy import OAuthHandler
from twitter_data_collector import database


def authorize(consumer_key,consumer_secret):
    return OAuthHandler(consumer_key,consumer_secret)

def get_tweet(auth,screen):
    api=tweepy.API(auth)
    user=api.get_user(screen_name=screen)
    tweets=[]
    new_tweets=api.user_timeline(screen_name=screen,count=1)
    tweets.extend(new_tweets)
    oldest=tweets[-1].id - 1
    while len(new_tweets)>0:
        new_tweets=api.user_timeline(screen_name=screen,count=200,max_id=oldest)
        for user1 in new_tweets:
            print(user1.text)
        tweets.extend(new_tweets)
        oldest = tweets[-1].id - 1
    print(len(tweets))
    return tweets


def get_data(auth,screen):
    api=tweepy.API(auth)
    user=api.get_user(screen_name=screen)
    print(user.id)
    print(user.name)
    print(user.description)
    print(user.location)
    data = {
        'id':user.id,
        'name':user.name,
        'place':user.location,
        'status':user.description,
        'screen_name':screen
    }
    return data