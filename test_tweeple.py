import gettwobj
import os
import simplejson as json

tweetID = 602910280528564225
jTweet = gettwobj.get_tweet_json(tweetID)
jTweetFileName = 'tweet.' + str(tweetID) + '.json'
with open(os.path.basename(jTweetFileName), 'wb') as file:
    file.write(json.dumps(jTweet))

tweetKeys = str(jTweet.keys())
# handle single hashtag:
tweetHashtags = jTweet['entities']['hashtags'][0]['text'].encode('ascii')
tweetText = jTweet['text'].encode('ascii')
tweetLocation = jTweet['place']['full_name']
tweetUserScreenname = jTweet['user']['screen_name']
tweetUserUserID = jTweet['user']['id_str']
tweetLocation_C01 = str(jTweet['place']['bounding_box']['coordinates'][0][0])
tweetLocation_C02 = str(jTweet['place']['bounding_box']['coordinates'][0][1])
tweetLocation_C03 = str(jTweet['place']['bounding_box']['coordinates'][0][2])

jTweetInfoFileName = 'tweet.' + str(tweetID) + '.info'
with open(os.path.basename(jTweetInfoFileName), 'wb') as file:
	file.write('Text:           ' + tweetText + '\n')
	file.write('Hashtags:       ' + tweetHashtags + '\n')
	file.write('Location:       ' + tweetLocation + '\n')
	file.write('Screen name:    ' + tweetUserScreenname  + '\n')
	file.write('User ID:        ' + tweetUserUserID + '\n')
	file.write('Coordinates 01: ' + tweetLocation_C01 + '\n')
	file.write('Coordinates 02: ' + tweetLocation_C02 + '\n')
	file.write('Coordinates 03: ' + tweetLocation_C03 + '\n')
	file.write('\n')
	file.write('All keys:       ' + tweetKeys + '\n')

