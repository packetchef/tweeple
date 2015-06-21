apiConsumerKey = tweepleKeyData['apiConsumerKey']
apiConsumerSecret = tweepleKeyData['apiConsumerSecret']
apiAccessToken = tweepleKeyData['apiAccessToken']
apiAccessTokenSecret = tweepleKeyData['apiAccessTokenSecret']

with open(os.path.basename('keys'), 'r') as file:
    tweepleKeyData = json.load(file)

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



