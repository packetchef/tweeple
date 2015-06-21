#!/usr/bin/env python

import tweepy
import os
import simplejson as json
import optparse
import time
import sys

def checkKeys(testKeys):
    requiredKeys = ['apiConsumerKey', 'apiConsumerSecret', 'apiAccessToken',
        'apiAccessTokenSecret']
    
    for key in requiredKeys:
        if key not in testKeys:
            raise ValueError('Key is not set: {0}'.format(key))
    # Assume we can safely return "True" if all required keys are present
    return True


def printAllKeys(**kwargs):
    # Test routine to enumerate the keys
    # Call with: printALlKeys(**keys)
    for name, value in kwargs.items():
        print('{0} :: {1}'.format(name, value))


def showUsage():
    print('''usage: {0} [ [-t | --tweet] tweet | [-u | --user] username ] 
         [ [-k | --keyfile] keyfile ]'''.format(sys.argv[0]))
    print('Options and arguments:')
    print('-t tweet, --tweet tweet       : tweet/status ID')
    print('-u username, --user username  : username')
    print('-k keyfile, --keyfile keyfile : keyfile (defaults to ./keys)')
    print('')
    print('You must choose to search for either a tweet ID or a username.')
    print('keyfile is optional and defaults to \'keys\' in current directory.')
    print('')
    sys.exit(1)


def doStuff_User(tUser):
    print('Get a user: {0}'.format(tUser))
    try:
        user = api.get_user(tUser)
        return user
    except Exception as e:
        print('Failed to get user: {0}'.format(e.message))
        sys.exit(1)


def doStuff_Tweet(tTweet):
    print('Get a tweet: {0}'.format(tTweet))


if __name__ == '__main__':
    optionParser = optparse.OptionParser()
    optionParser.add_option('-k', '--keyfile', action='store',
        default='keys.txt')
    optionParser.add_option('-u', '--user', action='store')
    optionParser.add_option('-t', '--tweet', action='store')
    options, remainder = optionParser.parse_args()

    # Must select EITHER user OR tweet, but not both
    if not options.user and not options.tweet:
        showUsage()
    if options.user and options.tweet:
        showUsage()

    # Let's try to load our keyfile and verify we have all required keys
    try:
        with open(os.path.abspath(options.keyfile), 'r') as file:
            tweepleKeyData = json.load(file)
    except IOError as e:
        if e.errno == 2:
            print('Unable to open keyfile {0}'.format(options.keyfile))
            sys.exit(1)
        else:
            print('IOError when trying to open keyfile {0}'.format(options.keyfile))
            sys.exit(1)

    try:
        checkKeys(tweepleKeyData)
        apiConsumerKey = tweepleKeyData['apiConsumerKey']
        apiConsumerSecret = tweepleKeyData['apiConsumerSecret']
        apiAccessToken = tweepleKeyData['apiAccessToken']
        apiAccessTokenSecret = tweepleKeyData['apiAccessTokenSecret']
    except ValueError as e:
        print('Error while checking keys.  {0}'.format(e.message))
        sys.exit(1)


    # Build our tweepy API handler
    auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
    auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
    api = tweepy.API(auth)

    if options.user:
        myUser = doStuff_User(options.user)
        print(myUser._json) 
    elif options.tweet:
        myTweet = doStuff_Tweet(options.tweet)
        print(myTweet._json)


