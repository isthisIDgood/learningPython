shoppingCart = []

if shoppingCart:
    for item in shoppingCart:
        print( "Adding " + item + " to your cart!" )
    print ( "Your order is complete!" )
else: 
    print ( "You must select an item before checking out." )