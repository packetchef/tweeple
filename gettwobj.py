import tweepy
import os
import simplejson as json

"""
TO DO
(1) Allow specifying path to key file

REFERENCES
Tweepy API: http://docs.tweepy.org/en/latest/api.html
"""
with open(os.path.basename('keys'), 'r') as file:
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
    """
    Defaults to 20 most recent statuses
    TO DO
    (1) Let screen_name be a user ID or screen name
    (2) Let caller specify range of tweet IDs
    """
    auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
    auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
    api = tweepy.API(auth)

    # include_rts is not documented in the API bu is required to get retweets
    t_user_timeline_lookup = api.user_timeline(id=screen_name, include_rts=True)
    return t_user_timeline_lookup


