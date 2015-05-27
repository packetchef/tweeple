import tweepy
import os
import simplejson as json

with open(os.path.basename('tweeple.keys'), 'r') as file:
        tweepleKeyData = json.load(file)

apiConsumerKey = tweepleKeyData['apiConsumerKey']
apiConsumerSecret = tweepleKeyData['apiConsumerSecret']
apiAccessToken = tweepleKeyData['apiAccessToken']
apiAccessTokenSecret = tweepleKeyData['apiAccessTokenSecret']

def get_user(screen_name):
    auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
    auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
    api = tweepy.API(auth)

    t_user_lookup = api.get_user(screen_name)
    return t_user_lookup

def get_tweet(twID):
    auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
    auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
    api = tweepy.API(auth)

    t_tweet_lookup = api.get_status(twID)
    return t_tweet_lookup

