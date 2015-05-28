import gettwobj
import os
import simplejson as json


def do_tweet_stuff(tweetID):
	jTweet = gettwobj.get_tweet_json(tweetID)
	jTweetFileName = 'tweet.' + str(tweetID) + '.json'
	with open(os.path.basename(jTweetFileName), 'wb') as file:
	    file.write(json.dumps(jTweet))
	print('Created tweet file in JSON format: %s' % jTweetFileName)
	
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
	if jTweet['place'] is None:
		tweetLocation     = 'geolocation not enabled'
		tweetLocation_C01 = 'geolocation not enabled'
		tweetLocation_C02 = 'geolocation not enabled'
		tweetLocation_C03 = 'geolocation not enabled'
	else:
		tweetLocation     = jTweet['place']['full_name']
		tweetLocation_C01 = str(jTweet['place']['bounding_box']['coordinates'][0][0])
		tweetLocation_C02 = str(jTweet['place']['bounding_box']['coordinates'][0][1])
		tweetLocation_C03 = str(jTweet['place']['bounding_box']['coordinates'][0][2])
	
	jTweetInfoFileName = 'tweet.' + str(tweetID) + '.info'
	with open(os.path.basename(jTweetInfoFileName), 'wb') as file:
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
	print('Created tweet info file: %s' % jTweetInfoFileName)



def do_user_stuff(tUserName):
	jUser = gettwobj.get_user_json(tUserName)
	jUserFileName = 'user.' + tUserName + '.json'
	with open(os.path.basename(jUserFileName), 'wb') as file:
		file.write(json.dumps(jUser))
	print('Created user file in JSON format: %s' % jUserFileName)
	
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
	
	jUserInfoFileName = 'user.' + tUserName + '.info'
	with open(os.path.basename(jUserInfoFileName), 'wb') as file:
		file.write('Display name:         ' + uDisplayName + '\n')
		file.write('User name:            ' + uUserName + '\n')
		file.write('User ID:              ' + uUserID + '\n')
		file.write('Descirption:          ' + uBio + '\n')
		file.write('Created:              ' + uCreated + '\n')
		file.write('User time zone:       ' + uTimeZone + '\n')
		file.write('Home page (short):    ' + uHomepageShortened + '\n')
		file.write('Last tweet ID:        ' + uLastTweetID + '\n')
		file.write('Last tweet text:      ' + uLastTweetText + '\n')
		file.write('\n')
		file.write('All keys:       ' + userKeys + '\n')
	print('Created user info file: %s' % jUserInfoFileName)

	# and for good measure, get the last tweet
	do_tweet_stuff(jUser['status']['id'])


# one tweet with single hashtag and location
# one tweet with multiple hashtags and no location 
testingTweets = 602910280528564225, 603714808731574272
for testTweet in testingTweets:
	do_tweet_stuff(testTweet)

testUserName = 'packetdev'
do_user_stuff(testUserName)

# To get last set of tweets:
# timeline = gettwobj.get_user_timeline(tUserName)


