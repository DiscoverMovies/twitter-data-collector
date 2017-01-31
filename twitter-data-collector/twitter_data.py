import tweepy
from tweepy import OAuthHandler
import database


def authorize(consumer_key,consumer_secret,access_token,access_token_secret):
    __auth = OAuthHandler(consumer_key, consumer_secret)
    __auth.set_access_token = (access_token, access_token_secret)
    return __auth


def get_tweet(screen, __auth):
    api=tweepy.API(__auth)
    user=api.get_user(screen_name=screen)
    tweets=[]
    new_tweets=api.user_timeline(screen_name=screen,count=1)
    tweets.extend(new_tweets)
    oldest=tweets[-1].id - 1
    while len(new_tweets)>0:
        new_tweets=api.user_timeline(screen_name=screen,count=1,max_id=oldest)
        for user1 in new_tweets:
            print(user1.text)
            database.insert_tweet(user.id,oldest,user1.text.encode('utf-8'),'root','asdf123!@')
        tweets.extend(new_tweets)
        oldest = tweets[-1].id - 1



def get_data(screen,__auth):
    api=tweepy.API(__auth)
    user=api.get_user(screen_name=screen)
    print(user.id)
    print(user.name)
    print(user.description)
    print(user.location)
    database.insert_user(user.id,user.name,screen,user.location,user.description,'root', 'asdf123!@')