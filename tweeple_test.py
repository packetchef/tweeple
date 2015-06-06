import gettwobj
import os
import simplejson as json

def do_tweet_stuff(tweetID):
    """
    REALITY CHECK
    This function works with Tweets as JSON, but most of the work could be done
    directly with the Tweepy objects.  For example, with a Status object named
    myTweet, these should return the same values:
    myTweet_as_object.text
    myTweet_as_json['text']
    Likewise, these should also return the same values:
    myTweet_as_object.place.full_name
    myTweet_as_json['place']['full_name']
    Careful, there are some differences.  For example, with myTweet_as_json,
    ['place'] is an object of type 'dict', whereas for myTweet_as_object,
    .place is an object of type tweepy.models.Place.  Be aware of this
    difference, as while the output may look the same the behavior can vary.
    """
    jTweet = gettwobj.get_tweet_json(tweetID)
    jTweetFileName = 'tests/tweet.' + str(tweetID) + '.json'
    with open(os.path.abspath(jTweetFileName), 'wb') as file:
        file.write(json.dumps(jTweet))
    print('Created tweet file in JSON format: {0}'.format(jTweetFileName))
    
    # Can't write a list to file without conversion to string first
    tweetKeys = str(jTweet.keys())
    
    # Build a list of our hashtags
    tweetHashtags = ''
    for tweetHashtag in jTweet['entities']['hashtags']:
    	tweetHashtags += tweetHashtag['text'].encode('ascii') + '; '
    
    tweetText = jTweet['text'].encode('ascii')
    tweetUserScreenname = jTweet['user']['screen_name']
    tweetUserUserID = jTweet['user']['id_str']
    tweetUserTimeZone = jTweet['user']['time_zone']
    tweetCreatedTime = jTweet['created_at']
    
    # Check if geolocation is enabled and act accordingly
    if jTweet['place']:
    	tweetLocation     = jTweet['place']['full_name']
    	tweetLocation_C01 = str(
            jTweet['place']['bounding_box']['coordinates'][0][0])
    	tweetLocation_C02 = str(
            jTweet['place']['bounding_box']['coordinates'][0][1])
    	tweetLocation_C03 = str(
            jTweet['place']['bounding_box']['coordinates'][0][2])
    else:
    	tweetLocation     = 'geolocation not enabled'
    	tweetLocation_C01 = 'geolocation not enabled'
    	tweetLocation_C02 = 'geolocation not enabled'
    	tweetLocation_C03 = 'geolocation not enabled'
    
    jTweetInfoFileName = 'tests/tweet.' + str(tweetID) + '.info'
    with open(os.path.abspath(jTweetInfoFileName), 'wb') as file:
    	file.write('Text:           ' + tweetText + '\n')
    	file.write('Hashtags:       ' + tweetHashtags + '\n')
    	file.write('Location:       ' + tweetLocation + '\n')
    	file.write('Created:        ' + tweetCreatedTime + '\n')
    	file.write('User time zone: ' + tweetUserTimeZone + '\n')	
    	file.write('Screen name:    ' + tweetUserScreenname  + '\n')
    	file.write('User ID:        ' + tweetUserUserID + '\n')
    	file.write('Coordinates 01: ' + tweetLocation_C01 + '\n')
    	file.write('Coordinates 02: ' + tweetLocation_C02 + '\n')
    	file.write('Coordinates 03: ' + tweetLocation_C03 + '\n')
    	file.write('\n')
    	file.write('All keys:       ' + tweetKeys + '\n')
    print('Created tweet info file: {0}'.format(jTweetInfoFileName))


def do_user_stuff(tUserName):
    jUser = gettwobj.get_user_json(tUserName)
    jUserFileName = 'tests/user.' + tUserName + '.json'
    with open(os.path.abspath(jUserFileName), 'wb') as file:
    	file.write(json.dumps(jUser))
    print('Created user file in JSON format: {0}'.format(jUserFileName))
    
    userKeys = str(jUser.keys())
    # check each of these to see if they exist first
    uDisplayName = jUser['name']
    uUserName = jUser['screen_name']
    uUserID = jUser['id_str']
    uBio = jUser['description']
    uCreated = jUser['created_at']
    uHomepageShortened = jUser['url']
    uTimeZone = jUser['time_zone']
    # uHomepage = juser['expanded_url'] <-- this is actually part of [entities][url]?
    # expand the shortened version at some point
    uLastTweetID = jUser['status']['id_str']
    uLastTweetText = jUser['status']['text']
    
    jUserInfoFileName = 'tests/user.' + tUserName + '.info'
    with open(os.path.abspath(jUserInfoFileName), 'wb') as file:
    	file.write('Display name:         ' + uDisplayName + '\n')
    	file.write('User name:            ' + uUserName + '\n')
    	file.write('User ID:              ' + uUserID + '\n')
    	file.write('Description:          ' + uBio + '\n')
    	file.write('Created:              ' + uCreated + '\n')
    	file.write('User time zone:       ' + uTimeZone + '\n')
    	file.write('Home page (short):    ' + uHomepageShortened + '\n')
    	file.write('Last tweet ID:        ' + uLastTweetID + '\n')
    	file.write('Last tweet text:      ' + uLastTweetText + '\n')
    	file.write('\n')
    	file.write('All keys:       ' + userKeys + '\n')
    print('Created user info file: {0}'.format(jUserInfoFileName))

    # and for good measure, get the last tweet
    do_tweet_stuff(jUser['status']['id'])


def do_timeline_stuff(tUserName):
    """
    Remember that while a result set of Status objects does not have a ._json
    property, the individual Status objects do, should you prefer.
    """
    tTimeline = gettwobj.get_user_timeline(tUserName)
    tTimelineFileName = 'tests/timeline.' + tUserName + '.info'
    with open(os.path.abspath(tTimelineFileName), 'wb') as file:
        file.write('Last status messages for ' + tUserName + '\n')
        for status in tTimeline:
            tStatusID = str(status.id)
            tStatusCreatedAt = str(status.created_at)
            tStatusText = status.text
            if status.place:
                tStatusPlace = status.place.full_name
            else:
                tStatusPlace = 'no geolocation'

            file.write('ID:        ' + tStatusID + '\n')
            file.write('Created:   ' + tStatusCreatedAt + '\n')
            file.write('Text:      ' + tStatusText + '\n')
            file.write('Place:     ' + tStatusPlace + '\n')
            file.write('\n')


# one tweet with single hashtag and location
# one tweet with multiple hashtags and no location 
testingTweets = 602910280528564225, 603714808731574272
for testTweet in testingTweets:
    do_tweet_stuff(testTweet)

testUserNames = 'packetdev',
for testUserName in testUserNames:
    do_user_stuff(testUserName)

testUserNames = 'packetdev',
for testUserName in testUserNames:
    do_timeline_stuff(testUserName)



