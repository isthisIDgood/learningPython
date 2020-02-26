##Passing an argument into a function

userName = input("Please enter your name: \n")

def helloUser(name):
    """say hi to the user"""
    print(' Hello, ' + name.title())

helloUser(userName)