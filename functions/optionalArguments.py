##Make a function that takes optional arguments

def formattedName(firstName, middleName, lastName):
    """Combine the three names and format them."""
    fullName = firstName + " " + middleName + " " + lastName
    return fullName.title()

print ( formattedName('brent', 'david', 'nolan') )

##Don't make middle name required
def notRequiredMiddleName(fName, lName, mName=''):
    """Combine the three names and format them."""
    if mName:
        entireName = fName + " " + mName + " " + lName
    else:
        entireName = fName + " " + lName
    return entireName.title()

print ( notRequiredMiddleName('brent', 'nolan') )
print ( notRequiredMiddleName('brent', 'nolan', 'david') )