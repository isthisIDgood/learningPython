##using Keys Method:

birthdayMonths = {
    'Brent': 'April',
    'Trent': 'May',
    'Richard': 'October',
    'Jael': 'March',
    'Robin': 'February',
    'Guy': 'April'
}

#keys method
for name in birthdayMonths.keys():
    print (name.title())

print('---------')

#values method
for months in birthdayMonths.values():
    print (months.title())

print('---------')

#Sets must be unique
for months in set(birthdayMonths.values()):
    print (months.title())