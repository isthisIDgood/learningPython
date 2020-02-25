#organizing Array
#create list
months = ['February', 'March', 'April', 'October']
print ( 'Base Array: \n', months )
#apply sory method
months.sort()
print ( 'months.sort(): \n', months )
#reverse sort
months = ['February', 'March', 'April', 'October']
months.sort(reverse=True)
print ( 'months.sort(reverse=True): \n', months )
#sorted = temporary
months = ['February', 'March', 'April', 'October']
print( 'print( sorted( months )) \n',sorted( months ) )
print ( 'This is what the array still looks like after print(sorted(months)): \n', months )
#reverse the list based on original output
months = ['February', 'March', 'April', 'October']
months.reverse()
print ( 'months.reverse(): \n', months )