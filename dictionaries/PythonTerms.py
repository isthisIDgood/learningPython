##Dictonary of Python Terms

pythonTerms = {
    'variable': 'Represents a value stored in memory',
    'string': 'A sequence of characters'
}

if 'float' in pythonTerms:
    print ('Dictionary contains float type')
else:
    print ('pythonTerms dictionary does not contain the float ty[e')
print ('Variable ' + pythonTerms['variable'])

terms = {}

terms['float'] = 'Represents a number with a decimal'
terms['integer'] = 'A whole number'

print ( '\nTerms dictionary:\n' + terms['float'])
print ( terms['integer'])
