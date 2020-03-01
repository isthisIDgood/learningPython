###Adding a while loop in function

def getFormattedName(firstName, lastName):
    """Return a full name and format it"""
    fullName = firstName + ' ' + lastName
    return fullName.title()

while True:
    print('\nWhat is your name? ')
    print("Enter 'q' at any time to quit this program")
    firstName= input("First Name: ")

    if firstName== 'q':
        break
    lastName = input("Last Name: ")
    if lastName=='q':
        break
    
    formattedName=getFormattedName(firstName, lastName)
    print ('\nHello, ' + formattedName + '!')