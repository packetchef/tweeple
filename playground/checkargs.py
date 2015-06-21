import sys


#if we're running this as a script
if __name__ == '__main__':
    if len(sys.argv) == 3:
        print('got the right number of arguments, but are they good?')
        
        queryType = sys.argv[1]
        queryParameter = sys.argv[2]

        print('Query type:      %s' % queryType)
        print('Query parameter: %s' % queryParameter)

        if queryType == 'tweet':
            print('Check for tweet ID:  %s' % queryParameter)
        elif queryType == 'user':
            print('Check for user name: %s' % queryParameter)
        else:
            print('Bad query type: %s' % queryType)
    else:
        print('did not get the right arguments')


