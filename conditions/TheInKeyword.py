##The in keyword

#Names registered
registeredNames = [
    'Brent',
    'Trent',
    'Jael',
    'Richard'
]

for name in registeredNames:
    print (name.title())

userName = input ("Please enter your username:\n")

if userName in registeredNames:
    print ("Username is already taken!")
else:
    print( userName + " account created!")