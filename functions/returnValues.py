##Create a function that retuns a value

def square(number):
    """return a number multiplied by itself"""
    return number * number

val = input('Please enter a number: ')
print(square(int(val)))

##Format name function
def formatName(firstName, lastName):
    """Format entered names"""
    return (firstName.title() + " " + lastName.title())

print ( formatName ('brent','nolan') )