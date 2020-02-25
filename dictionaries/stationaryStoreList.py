##dictionary within a list
stockItems = []

for bluePen in range(0,50):
    newBluePen = {
        'color': 'blue',
        'type': 'ballpoint',
        'price': 1.99
    }
    stockItems.append(newBluePen)

##change price for first 5 pens
for bluePen in stockItems[0:5]:
    if bluePen['price'] == 1.99:
        bluePen['price'] = 1.49
##print new price for these 
for bluePen in stockItems[0:5]:
    print ( bluePen )