##Returning a dictionary

def buildBook(bookName, bookAuthor):
    """Create a dictionary of book info"""
    book = {
        'name': bookName,
        'author': bookAuthor
    }
    return book

harryPotter = buildBook('Harry Potter', 'J.K Rowling')
print (harryPotter)