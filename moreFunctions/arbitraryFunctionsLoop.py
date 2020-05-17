##Loop over all parameters

def requestLoop(*requests):
    ###Print user requests
    print("\nThis passenger has requested:")
    for request in requests:
        print('  - ' + request)

requestLoop('window seat', 'first class', 'comfort plus')  