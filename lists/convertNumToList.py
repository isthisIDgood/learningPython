## Convert Numbers into a list
print ( "list(range1,6):" )
numbers = list(range(1,6))

print (numbers)

print ("\nlist(range(1,100,2):")
oddNumbers=list(range(1,100,2))
print (oddNumbers)

squares = []
for val in range (1, 11):
    square = val ** 2
    squares.append(square)
print ( "\nval in range (1,11): square = val ** 2:" ) 
print ( squares )

digits = [1,2,3,4,5]
print ("\nmin, max, and sum of digits:")
print ( min(digits) )
print ( max(digits) )
print ( sum(digits) )