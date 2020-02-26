##Adding user input to a dictionary

favoriteMovies = {}
moreMovies = True

while moreMovies:
    #Get user input
    userName = input("Please enter your Name: \n")
    movie = input("Enter your favorite movie: \n")

    #Save user input
    favoriteMovies[userName] = movie

    #Ask if more movies
    friends = input("Do you have any friends?\n")
    if friends.lower() == 'no':
        moreMovies = False
    
##Print contents of dictionary
print ("--- People and their favorite movies ---")
for user, movies in favoriteMovies.items():
    print ( '    ' + user.title() + "'s favorite movie is " + movies.title() )