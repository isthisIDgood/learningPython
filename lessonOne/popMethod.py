#using the pop method
subs = ['bnolan@epic.com', 'b_nolan@att.net', 'example@testing.com']
print ( subs, '\n' )

#pop method pulls off the last index
poppedSub = subs.pop()
print('Using Pop method: \n', subs )
print( '\npoppedSub: \n\t', poppedSub , '\n')

subs.append(poppedSub)

#can pop other index of array if you specify
firstOfList = subs.pop(0)
print('First sub on the list was: ', firstOfList )
print('\nUnfortunately, ' + firstOfList + ' is no longer in the list: \n',subs )

#remove method
print('\nwe are now hard coding via remove method:')
removeSub='b_nolan@att.net'
subs.remove(removeSub)
print (subs)