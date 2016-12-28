

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "730811305951531008-L3E7hzt9cc0PbZgNjLSN2m8B9vXJBWZ"
access_token_secret = "p86kIjEL7LCav6MizcU2hPxWP60JiYE9rqrZgOnuPsIzt"
consumer_key = "RSadgT0OqyoMuQuaranwUyvat"
consumer_secret = "9bWvcyOmMCHobWG737B3fOLkOG1x5Cq3DN3DRcnRT36oXu8xmW"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data with #
    stream.filter(track=['#'])