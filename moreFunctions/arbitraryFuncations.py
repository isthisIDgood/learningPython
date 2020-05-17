###Arbitrary Functions - can take in as many parameters as are used in call

def createPassenger(*requests):
    ###Print user requests
    print(requests)

createPassenger('window seat', 'first class', 'comfort plus')  
