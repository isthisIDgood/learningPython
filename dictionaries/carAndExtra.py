#dictionary with list

purchasedCar = {
    'type': 'four door',
    'extras': ['leather seats', 'climate control']
}

#summary of car
print ( 'You purchased a ' + purchasedCar['type'] + ' with the following features:')
for extra in purchasedCar['extras']:
    print ( '\t-' + extra )