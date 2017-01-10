import tweepy

from tweepy import OAuthHandler

access_token = 
access_token_secret = 
consumer_key = 
consumer_secret = 

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

