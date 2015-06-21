import tweepy
import simplejson as json

"""
REFERENCES
Tweepy API: http://docs.tweepy.org/en/latest/api.html
"""

def checkKeys(testKeys):
    requiredKeys = ['apiConsumerKey', 'apiConsumerSecret', 'apiAccessToken',
        'apiConsumerSecret']

    for key in requiredKeys:
        if key not in testKeys:
            raise ValueError('Key is not set: {0}'.format(key))

    # Assume we can safely return "True" if all required keys are present
    return True


def printAllKeys(**kwargs):
    # Test routine to enumerate the keys
    # Call with: printAllKeys(**keys)
    for name, value in kwargs.items():
        print('{0} :: {1}'.format(name, value))


def get_user(keys, screen_name):
    try:
        checkKeys(keys)
        auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
        auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
        api = tweepy.API(auth)

        t_user_lookup = api.get_user(screen_name)
        return t_user_lookup
    except ValueError as e:
        print('{0}'.format(e.message))


def get_tweet(keys, twID):
    try:
        checkKeys(keys)
        auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
        auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
        api = tweepy.API(auth)

        t_tweet_lookup = api.get_status(twID)
        return t_tweet_lookup
    except ValueError as e:
        print('{0}'.format(e.message))


def get_user_json(keys, screen_name):
    try:
        checkKeys(keys)
        auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
        auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
        api = tweepy.API(auth)

        t_user_lookup = api.get_user(screen_name)
        return t_user_lookup._json
    except ValueError as e:
        print('{0}'.format(e.message))


def get_tweet_json(keys, twID):
    try:
        checkKeys(keys)
        auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
        auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
        api = tweepy.API(auth)

        t_tweet_lookup = api.get_status(twID)
        return t_tweet_lookup._json
    except ValueError as e:
        print('{0}'.format(e.message))


def get_user_timeline(keys, screen_name):
    """
    Defaults to 20 most recent statuses
    TO DO
    (1) Let screen_name be a user ID or screen name
    (2) Let caller specify range of tweet IDs
    """
    try:
        checkKeys(keys)
        auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
        auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
        api = tweepy.API(auth)

        # include_rts is not documented in the API bu is required to get retweets
        t_user_timeline_lookup = api.user_timeline(id=screen_name, include_rts=True)
        return t_user_timeline_lookup
    except ValueError as e:
        print('{0}'.format(e.message))


