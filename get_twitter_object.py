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
        log('{0} :: {1}'.format(name, value), 'debug')


def showUsage():
    usageText = (
        'usage: get_twitter_object.py [ [-t | --tweet] tweet | [-u | --user]'
        'username ] [ [-k | --keyfile] keyfile ] [ [-w | --write ] target ]\n'
        'Options and arguments:\n'
        '-t tweet, --tweet tweet       : tweet/status ID\n'
        '-u username, --user username  : username\n'
        '-k keyfile, --keyfile keyfile : keyfile (defaults to ./keys)\n'
        '-w target, --write target     : target directory for writing output\n'
        '\n'
        'You must choose to search for either a tweet ID or a username.\n'
        'keyfile is optional and defaults to \'keys.conf\' in the current\n' 
        'directory.\n'
        '\n'
        )
    print(usageText)
    sys.exit(1)


def log(msg, sev='low'):
    if sev == 'debug':
        print('{0} :: {1}'.format(sev, msg))
    else:
        # Build out some sort of log facility later
        pass

def doStuff_User(twUser):
    log('Get a user: {0}'.format(twUser))
    try:
        user = api.get_user(twUser)
        return user
    except Exception as e:
        log('Failed to get user: {0}'.format(e.message), 'debug')
        sys.exit(1)


def doStuff_Tweet(twTweet):
    log('Get a tweet: {0}'.format(twTweet))
    try:
        tweet = api.get_status(twTweet)
        return tweet
    except Exception as e:
        log('Failed to get tweet: {0}'.format(e.message), 'debug')
        sys.exit(1)


def writeObjectJSON(outFile, twData):
    try:
        with open(os.path.abspath(outFile), 'w') as file:
            if isinstance(twData, dict):
                json.dump(twData, file)
            else:
                file.write(twData)
    except IOError as e:
        log('Unable to write outFile {0}: {1}'.format(outFile, e.message), 
            'debug')    


if __name__ == '__main__':
    now = time.time()
    
    optionParser = optparse.OptionParser()
    optionParser.add_option('-k', '--keyfile', action='store',
        default='keys.conf')
    optionParser.add_option('-u', '--user', action='store')
    optionParser.add_option('-t', '--tweet', action='store')
    optionParser.add_option('-w', '--write', action='store')
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
            log('Unable to open keyfile {0}'.format(options.keyfile), 'debug')
            sys.exit(1)
        else:
            log('IOError when trying to open keyfile {0}' \
                .format(options.keyfile), 'debug')
            sys.exit(1)

    try:
        checkKeys(tweepleKeyData)
        apiConsumerKey = tweepleKeyData['apiConsumerKey']
        apiConsumerSecret = tweepleKeyData['apiConsumerSecret']
        apiAccessToken = tweepleKeyData['apiAccessToken']
        apiAccessTokenSecret = tweepleKeyData['apiAccessTokenSecret']
    except ValueError as e:
        log('Error while checking keys.  {0}'.format(e.message), 'debug')
        sys.exit(1)

    # Build the output filename's suffixes
    if options.write:
        outputDirectory = options.write
        outFileName = ''.join([format(now, '.0f'), '.out'])

    # Build our tweepy API handler
    auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
    auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
    api = tweepy.API(auth)

    if options.user:
        getUser = options.user
        myUser = doStuff_User(getUser)
        log(myUser._json)
        if options.write:
            outFileName = ''.join([outputDirectory, '/', getUser, '.', 
                outFileName])
            writeObjectJSON(outFileName, myUser._json)
    elif options.tweet:
        getTweet = options.tweet
        myTweet = doStuff_Tweet(getTweet)
        log(myTweet._json)
        if options.write:
            outFileName = ''.join([outputDirectory, '/', 'tweet-', getTweet, 
            '.', outFileName])
            writeObjectJSON(outFileName, myTweet._json)

