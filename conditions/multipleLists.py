##working with multiple arrays
inStock = [
    'blue pens',
    'paper',
    'staples'
]

shoppingCart = [
    'blue pens',
    'paper',
    'staples',
    'oranges'
]

for item in shoppingCart:
    if item in inStock: 
        print ( item + ' has/have been purchased!')
    else:
        print (item + ' is currently out of stock.')