username = input("Welcome, please enter your username.\n")
password = input("Please enter your password.\n")

if username != 'brent' and password != 123:
    print ( "access denied. lol.")
else:
    print ( "Welcome back, " + username.title())