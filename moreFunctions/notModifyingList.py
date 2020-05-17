##Passing a list to a function and modifying it

def showNotCheckedInPassengers(notChecked):
    """Display not checked in passengers"""
    print ( 'These passengers are not yet checked in: ' )
    for passenger in notChecked:
        print('  -' + passenger.title())

def checkInPassengers(notChecked,checked):
    """simulate passengers who are not checked in"""
    print('\nChecking in passengers...\n')
    while notChecked:
        currentPassenger = notChecked.pop()
        ##Simulate checking them in
        print( "Checking in " + currentPassenger.title() + "...")
        checked.append(currentPassenger)

def showCheckedPassengers(checked):
    """Show all passengers who have checked in"""
    print("\nThe following passengers have been checked in: ")
    for passenger in checked:
        print('  -' + passenger.title())
    
notChecked = [
    'Brent Nolan',
    'Tw Flem',
    'Judith',
    'Harry Potter'
]

checked = []
showNotCheckedInPassengers(notChecked)
checkInPassengers(notChecked[:],checked)
showCheckedPassengers(checked)