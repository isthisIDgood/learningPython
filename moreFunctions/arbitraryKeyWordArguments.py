###Dictionary - key/value pairs in arbitrary arguments

def passengerProfile(fname, lname, **passengerInfo):
    profile = {}
    profile ['firstName'] = fname.title()
    profile ['lastName'] = lname.title()
    for key, value in passengerInfo.items():
        profile [key] = value
    return profile
    
passengerMe = passengerProfile('brent','nolan', seatNumber = 40, comfortPlus = 'yes', breakfast = 'eggs')
print(passengerMe)