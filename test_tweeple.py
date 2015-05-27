import gettwobj
import os
import simplejson as json

tweetID = 602910280528564225
jTweet = gettwobj.get_tweet(tweetID)._json
jTweetFileName = 'tweet.' + str(tweetID) + '.json'
with open(os.path.basename(jTweetFileName), 'wb') as file:
    file.write(json.dumps(jTweet))



