##Removing all instance of a value from a list

movies = [
    'Star Wars',
    'Star Trek',
    'Back to the Future',
    'Star Wars',
    'The Dark Knight',
    'Star Wars'
]

print('\nOriginal Moves List:')
for film in movies:
    print ( '-' + film )

##remove all instances of Star Wars
overrated = 'Star Wars'
while overrated in movies:
    movies.remove(overrated)

print( '\nMoves list with Star Wars removed:')
for film in movies:
    print ( '-' + film )