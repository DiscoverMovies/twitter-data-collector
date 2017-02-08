import tweepy
from tweepy import OAuthHandler
from twitter_data_collector import database


def authorize(self):
    auth= OAuthHandler(self.consumer_key,self.consumer_secret)
    auth.set_access_token =(self.access_token,self.access_token_secret)
    return auth

def get_tweet(self,auth):
    api=tweepy.API(auth)
    user=api.get_user(screen_name=self.screen)
    tweets=[]
    new_tweets=api.user_timeline(screen_name=self.screen,count=1)
    tweets.extend(new_tweets)
    oldest=tweets[-1].id - 1
    while len(new_tweets)>0:
        new_tweets=api.user_timeline(screen_name=self.screen,count=1,max_id=oldest)
        for user1 in new_tweets:
            print(user1.text)
            database.insert_tweet(user.id,oldest,user1.text,'root','asdf123!@')
        tweets.extend(new_tweets)
        oldest = tweets[-1].id - 1


def get_data(self,auth):
    api=tweepy.API(auth)
    user=api.get_user(screen_name=self.screen)
    print(user.id)
    print(user.name)
    print(user.description)
    print(user.location)
    database.insert_user(user.id,user.name,self.screen,user.location,user.description,'root', 'asdf123!@')