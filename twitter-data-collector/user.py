"""
    Copyright (C) 2017 Sherin Ann Thomas

    This file is part of twitter-data-collector.

    twitter-data-collector is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    twitter-data-collector is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with twitter-data-collector.  If not, see <http://www.gnu.org/licenses/>.
"""

import tweepy

from tweepy import OAuthHandler

access_token = None
access_token_secret = None
consumer_key = None
consumer_secret = None

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

