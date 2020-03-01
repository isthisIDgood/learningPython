##Passing a List to a Function

def booksAvailable(books):
    """Show a list of books available to buy"""
    print("The following titles are available for purchase: ")
    for book in books:
        print ('  -' + book.title())

available = [
    'Inheritance',
    'Game of Thrones',
    'Harry Potter',
    'Lord of the Rings'
]

booksAvailable(available)