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

def get_user_json(screen_name):
    auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
    auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
    api = tweepy.API(auth)

    t_user_lookup = api.get_user(screen_name)
    return t_user_lookup._json

def get_tweet_json(twID):
    auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
    auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
    api = tweepy.API(auth)

    t_tweet_lookup = api.get_status(twID)
    return t_tweet_lookup._json

def get_user_timeline(screen_name):
    auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
    auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
    api = tweepy.API(auth)

    t_user_timeline_lookup = api.user_timeline(id=screen_name, include_rts=True)
    return t_user_timeline_lookup

def get_user_timeline_json(screen_name):
    auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
    auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
    api = tweepy.API(auth)

    # Eventually let this be specified as user ID or screenname,
    # but for now assume screenname
    # Also add support for a range of tweet IDs
    # And, include_rts is not documented in the API but needs to be included to get retweets
    t_user_timeline_lookup = api.user_timeline(id=screen_name, include_rts=True)
    return t_user_timeline_lookup._json


