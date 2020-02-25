##Editing Dictionaries

pythonTerms = {
    'integer': 'A number that contains a decimal place',
    'string': 'A sequence of characters'
}
print ( pythonTerms )
print ( pythonTerms.get('integer'))

pythonTerms['integer'] = 'A Whole Number'
print ( '\n' + pythonTerms.get('integer'))

print( pythonTerms )

del pythonTerms['integer']
print( '\nDictionary after deleting the integer key:')
print( pythonTerms )