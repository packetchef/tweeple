import gettwobj
import os
import sys
import time

def get_tweet_metadata(tTweetID):
    targetTweet = gettwobj.get_tweet(tTweetID)
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


if __name__ == '__main__':
    if len(sys.argv) == 2:
        targetUserName = sys.argv[1]
        print('Target user: {0}'.format(targetUserName))
    elif len(sys.argv) > 2:
        sys.exit('Too many arguments')
    else:
        sys.exit('Missing argument: targetUser')

    now = time.time()
    runFileName = targetUserName + format(now, '.0f') + '.out'

    # get_tweet_metadata(targetTweetID)
    targetTimeline = gettwobj.get_user_timeline(targetUserName)
    print('Getting tweets:')
    for status in targetTimeline:
        statusID = status.id_str
        print(statusID)

    for status in targetTimeline:
        statusID = status.id_str
        print('-----------------------')
        get_tweet_metadata(statusID)


