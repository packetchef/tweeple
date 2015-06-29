#!/usr/bin/env python

import tweepy
import os
import simplejson as json
import optparse
import time
import sys


def checkKeys(testKeys):
    # Test routine to validate that the key file provided the required keys
    requiredKeys = ['apiConsumerKey', 'apiConsumerSecret', 'apiAccessToken',
                    'apiAccessTokenSecret']

    for key in requiredKeys:
        if key not in testKeys:
            raise ValueError('Key is not set: {key}'.format(key=key))
    # Assume we can safely return "True" if all required keys are present
    return True


def printAllKeys(**kwargs):
    # Test routine to enumerate the keys
    # Call with: printAllKeys(**keys)
    for name, value in kwargs.items():
        print('{name} :: {value}'.format(name=name, value=value))


def log(msg, sev='low'):
    # For now, debug will write to stdout and everything else does nothing
    if sev == 'debug' or sev == 'crit':
        print('[*] {log_message}'.format(log_message=msg))
    else:
        # Build out some sort of log facility later
        pass


def doStuff_User(twUser, twApi):
    # Wrapper to API call to retrieve a tweepy user object
    if debug:
        log('Get a user: {user}'.format(user=twUser), 'debug')
    try:
        user = twApi.get_user(twUser)
        return user
    except Exception as e:
        log('Failed to get user: {exc_msg}'.format(exc_msg=e.message), 'crit')
        sys.exit(1)


def doStuff_Tweet(twTweet, twApi):
    # Wrapper to API call to retrieve tweepy status object (aka tweet)
    if debug:
        log('Get a tweet: {tweet}'.format(tweet=twTweet), 'debug')
    try:
        tweet = twApi.get_status(twTweet)
        return tweet
    except Exception as e:
        log('Failed to get tweet: {exc_msg}'.format(exc_msg=e.message), 'crit')
        sys.exit(1)


def writeObjectJSON(outFile, twData):
    '''
    Simply, take a JSON dictionary and write it to a file.  This assumes that
    the caller took a tweepy user object and is sending the _json property.
    '''
    if debug:
        log('Writing object to file: {outFile}'.format(outFile=outFile),
            'debug')
    try:
        with open(os.path.abspath(outFile), 'w') as file:
            if isinstance(twData, dict):
                json.dump(twData, file)
            else:
                file.write(twData)
    except IOError as e:
        log('Unable to write outFile {outFile}: {exc_msg}'
            .format(outFile=outFile, exc_msg=os.strerror(e.errno)), 'crit')


def main(argv):
    # not really sure if this should be defined here or top of the file
    global debug
    now = time.time()

    progDesc = (
        'The get_twitter_object fetches a twitter user profile or'
        'tweet ("status").  The results are written to stdout and optionally '
        'to an auto-generated file in a specified directory.  When running '
        '%prog, you must specify whether you are searching for a user or a '
        'tweet.  Optional arguments include the path to your API key file and '
        'path to a directory where you want to write object output.'
    )

    optionParser = optparse.OptionParser(usage='Usage: %prog [options]',
                                         description=progDesc)
    optionParser.add_option('-d', '--debug', action='store_true', dest='debug',
                            help='Enable debug mode', default=False)
    optionParser.add_option('-k', '--keyfile', action='store',
                            help='Location of key file, default is keys.conf',
                            default='keys.conf')
    optionParser.add_option('-u', '--user', action='store',
                            help='Lookup user name (will change to '
                            'ID/username/screen name later)')
    optionParser.add_option('-t', '--tweet', action='store',
                            help='Lookup tweet status ID')
    optionParser.add_option('-w', '--write', action='store',
                            help='Directory for writing output (sorry, '
                            'filenames not configurable)')

    (options, args) = optionParser.parse_args()

    if options.debug:
        log('Debug mode enabled', 'debug')
        debug = True
    else:
        debug = False

    # Must select EITHER user OR tweet, but not both
    if not options.user and not options.tweet:
        optionParser.print_help()
        sys.exit(1)
    if options.user and options.tweet:
        optionParser.print_help()
        sys.exit(1)

    # Let's try to load our keyfile and verify we have all required keys
    try:
        with open(os.path.abspath(options.keyfile), 'r') as file:
            tweepleKeyData = json.load(file)
    except IOError as e:
        if e.errno == 2:
            log('Unable to open keyfile {f}'.format(f=options.keyfile), 'crit')
            sys.exit(1)
        else:
            log('IOError when trying to open keyfile {f}'
                .format(f=options.keyfile), 'crit')
            sys.exit(1)

    try:
        checkKeys(tweepleKeyData)
        apiConsumerKey = tweepleKeyData['apiConsumerKey']
        apiConsumerSecret = tweepleKeyData['apiConsumerSecret']
        apiAccessToken = tweepleKeyData['apiAccessToken']
        apiAccessTokenSecret = tweepleKeyData['apiAccessTokenSecret']
        if debug:
            log('apiConsumerKey: {k}'.format(k=apiConsumerKey), 'debug')
            log('apiConsumerSecret: {k}'.format(k=apiConsumerSecret), 'debug')
            log('apiAccessToken: {k}'.format(k=apiAccessToken), 'debug')
            log('apiAccessTokenSecret: {k}'.format(k=apiAccessTokenSecret),
                'debug')
    except ValueError as e:
        log('Error while checking keys.  {exc_msg}'.format(exc_msg=e.message),
            'crit')
        sys.exit(1)

    # Build the output filename's suffixes
    if options.write:
        outputDirectory = options.write
        outputFileName = ''.join([format(now, '.0f'), '.out'])
        if debug:
            log('outputDirectory: {od}'.format(od=outputDirectory), 'debug')
            log('outputFileName: {of}'.format(of=outputFileName), 'debug')

    # Build our tweepy API handler
    auth = tweepy.OAuthHandler(apiConsumerKey, apiConsumerSecret)
    auth.set_access_token(apiAccessToken, apiAccessTokenSecret)
    api = tweepy.API(auth)

    if options.user:
        getUser = options.user
        if debug:
            log('Getting user: {user}'.format(user=getUser), 'debug')
        myUser = doStuff_User(getUser, api)
        print(myUser._json)
        if options.write:
            outputFileName = ''.join([outputDirectory, '/', getUser, '.',
                                     outputFileName])
            writeObjectJSON(outputFileName, myUser._json)
    elif options.tweet:
        getTweet = options.tweet
        if debug:
            log('Getting tweet: {tweet}'.format(tweet=getTweet), 'debug')
        myTweet = doStuff_Tweet(getTweet, api)
        print(myTweet._json)
        if options.write:
            outputFileName = ''.join([outputDirectory, '/', 'tweet-', getTweet,
                                     '.', outputFileName])
            writeObjectJSON(outputFileName, myTweet._json)


if __name__ == '__main__':
    main(sys.argv[1:])

