import gettwobj
import os
import sys
import time
import optparse
import simplejson as json

def get_tweet_metadata(tTweetID):
    targetTweet = gettwobj.get_tweet(tweepleKeyData, tTweetID)
    if targetTweet:
        print('Got tweet: {0}'.format(str(targetTweet.id)))
    else:
        # Returns tweepy.error.TweepError
        sys.exit('Unable to get tweet ID {0}'.format(targetTweetID))

    #print('Checking hashtags')
    try:
        getattr(targetTweet, 'entities')
    except AttributeError:
        tweetHashtags = ''
    else:
        tweetHashtags = ''
        if targetTweet.entities['hashtags']:
            for tweetHashtag in targetTweet.entities['hashtags']:
                tweetHashtags += tweetHashtag['text'].encode('ascii') + '; '

    #print('Getting other metadata')
    tweetText = targetTweet.text.encode('ascii')
    tweetUserScreenname = targetTweet.user.screen_name
    tweetUserUserID = targetTweet.user.id_str
    tweetUserTimeZone = targetTweet.user.time_zone
    tweetCreatedTime = targetTweet.created_at

    #print('Checking geolocation')
    # Check if geolocation is enabled and act accordingly
    if targetTweet.place:
        tweetLocation = targetTweet.place.full_name
        tweetLocation_C01 = str(
            targetTweet.place.bounding_box.coordinates[0][0])
        tweetLocation_C02 = str(
            targetTweet.place.bounding_box.coordinates[0][1])
        tweetLocation_C03 = str(
            targetTweet.place.bounding_box.coordinates[0][2])
    else:
        tweetLocation = 'geolocation not enabled'
        tweetLocation_C01 = 'geolocation not enabled'
        tweetLocation_C02 = 'geolocation not enabled'
        tweetLocation_C03 = 'geolocation not enabled'

    print('Tweet ID:       {0}'.format(targetTweet.id_str))
    print('Text:           {0}'.format(tweetText))
    print('Hashtags:       {0}'.format(tweetHashtags))
    print('Location:       {0}'.format(tweetLocation))
    print('Created:        {0}'.format(tweetCreatedTime))
    print('User time zone: {0}'.format(tweetUserTimeZone))
    print('Screen name:    {0}'.format(tweetUserScreenname))
    print('User ID:        {0}'.format(tweetUserUserID))
    print('Coordinates 01: {0}'.format(tweetLocation_C01))
    print('Coordinates 02: {0}'.format(tweetLocation_C02))
    print('Coordinates 03: {0}'.format(tweetLocation_C03))


def showUsage():
    print('*' * 10)
    print('-u or --user: username')
    print('-k or --keyfile: keyfile')
    print('*' * 10)


if __name__ == '__main__':
    optionParser = optparse.OptionParser()
    optionParser.add_option('-k', '--keyfile', action='store', 
        default='keys.txt')
    optionParser.add_option('-u', '--user', action='store')
    optionParser.add_option('-t', '--tweet', action='store')
    options, remainder = optionParser.parse_args()

    """
    print options
    print options.user
    print options.tweet
    print options.keyfile
    """

    if not options.user and not options.tweet:
        showUsage()

    try:
        with open (os.path.abspath(options.keyfile), 'r') as file:
            tweepleKeyData = json.load(file)
    except IOError as e: 
        if e.errno == 2:
            print('Unable to open keyfile {0}'.format(options.keyfile))
        else:
            print('IOError when trying top open keyfile {0}'.format(options.keyfile))

"""
    if len(sys.argv) == 3:
        keyFile = sys.argv[1]
        targetUserName = sys.argv[2]
        print('Key file: {0}'.format(keyFile))
        print('Target user: {0}'.format(targetUserName))
    elif len(sys.argv) > 3:
        sys.exit('Too many arguments')
    else:
        sys.exit('Missing arguments')

    with open(os.path.abspath(keyFile), 'r') as file:
        tweepleKeyData = json.load(file)

    now = time.time()
    runFileName = targetUserName + format(now, '.0f') + '.out'

    # get_tweet_metadata(targetTweetID)
    targetTimeline = gettwobj.get_user_timeline(tweepleKeyData, targetUserName)
    print('Getting tweets:')
    for status in targetTimeline:
        statusID = status.id_str
        print(statusID)

    for status in targetTimeline:
        statusID = status.id_str
        print('-----------------------')
        get_tweet_metadata(statusID)
"""

