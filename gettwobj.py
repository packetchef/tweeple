import tweepy
import simplejson as json
import os

with open(os.path.basename('tweeple.keys'), 'r') as file:
        data = file.readlines()

print data
jData = json.dumps(data)
print jData
