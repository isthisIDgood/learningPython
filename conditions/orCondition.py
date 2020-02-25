## Or Condition

yourAge = input("How old are you?\n")
friendAge = input("Yeah but how old is your friend? haha\n")

if int(yourAge) >= 18 or int(friendAge) >=18:
    print ( "Congrats.  Welcome to the rest of your life." )
else:
    print ("You're both so young and naive.")