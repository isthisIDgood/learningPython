## not in keyword

adminUser = [
    'Brent',
    'Trent'
]

otherUser = [
    'Richard',
    'Jael'
]

userName = input ("Please enter your username: ")

if userName not in adminUser:
    print ("You do not have admin access")
else:
    print ("Admin access granted.")