import tweepy

from tweepy import OAuthHandler

access_token = "730811305951531008-L3E7hzt9cc0PbZgNjLSN2m8B9vXJBWZ"
access_token_secret = "p86kIjEL7LCav6MizcU2hPxWP60JiYE9rqrZgOnuPsIzt"
consumer_key = "RSadgT0OqyoMuQuaranwUyvat"
consumer_secret = "9bWvcyOmMCHobWG737B3fOLkOG1x5Cq3DN3DRcnRT36oXu8xmW"

def get_tweet(screen):

  auth=OAuthHandler(consumer_key,consumer_secret)
  auth.set_access_token=(access_token,access_token_secret)
  api=tweepy.API(auth)
  tweets= []
  newtweets=api.user_timeline(screen_name=screen,count=1)
  tweets.extend(newtweets)
  oldest =tweets[-1].id-1


  while len(newtweets)>0:
    newtweets=api.user_timeline(screen_name=screen,count=200,max_id=oldest)
    for user in newtweets:
      print(user.text)

    tweets.extend(newtweets)
    oldest = tweets[-1].id - 1
 
  
if __name__== '__main__':
  get_tweet('SidhinThomas')

