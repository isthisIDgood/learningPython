##Updating a list in a while loop
##Example: verifying user email

verifiedUsers = []

unVerifiedUsers = [
    'Brent',
    'Moose',
    'Skwish'
]

##populate verifiedUsers with unVerifiedUsers

while unVerifiedUsers:
    currentUser = unVerifiedUsers.pop()
    print( 'Verifying ' + currentUser.title() + '.')
    verifiedUsers.append(currentUser)

print( '\nThe following users have been verified: ')
for verifiedUser in verifiedUsers:
    print ( '\t-' + verifiedUser.title())