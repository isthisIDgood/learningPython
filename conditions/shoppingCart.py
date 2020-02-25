##Creating Shopping cart

shoppingCart = [
    'pants',
    'pens',
    'paper',
    'stapler'
]

##add each item to an order
for item in shoppingCart:
    if item == 'pens':
        print( "Sorry, " + item + " is out of stock." )
    else: 
        print ( "Adding " + item + " to your order!")

print ( "Order completed." )