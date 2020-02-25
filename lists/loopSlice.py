#Looping through a Slice

names = [
    'Brent',
    'Trent',
    'Jael',
    'Richard'
]

print('Here are the names of the last 3 registrations: ')
for name in names[-3:]:
    print(name.title())