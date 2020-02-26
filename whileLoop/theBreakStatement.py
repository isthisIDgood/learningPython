##Using A Break to Exit

prompt = "To quit, enter 'q'."
prompt += '\nPlease enter the name of a book you have read recently: '

while True:
    book = input(prompt)
    if book == 'q':
        break
    else:
        print ( book.title() + ', huh?  Fuckin nerd.' )
