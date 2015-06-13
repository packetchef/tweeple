import os
import sys
import simplejson as json

def varIsSet(var):
    print('Variable {} is set'.format(var))
    return True

def varIsNotSet(var):
    print('Variable {} is not set'.format(var))
    return False

def printAllKeys(**kwargs):
    # A redundant way to enumerate the keys
    for name, value in kwargs.items():
        print('{0} :: {1}'.format(name, value))

def getKeys(jKeys):
    requiredKeys = ['apiConsumerKey', 'apiConsumerSecret',
        'apiAccessTokenSecret']
    # Test dict will cause failure because of 'apiSekrets' :
    #requiredKeys = ['apiConsumerKey', 'apiConsumerSecret',
    #    'apiSekrets', 'apiAccessToken', 'apiAccessTokenSecret']

    for key in requiredKeys:
        if key in jKeys:
            #varIsSet(key)
            print('Key {0} is set to {1}'.format(key, jKeys[key]))
        else:
            #varIsNotSet(key)
            sys.exit('Missing key: {}'.format(key))

if len(sys.argv) == 2:
    keyFile = sys.argv[1]
    with open(os.path.abspath(keyFile), 'r') as file:
        keys = json.load(file)
   
    print('---- Checking if keys are set ----') 
    getKeys(keys)
    print('---- Printing all keys ----')
    printAllKeys(**keys)
else:
    sys.exit('missing argument: keyFile')


