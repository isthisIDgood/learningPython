###Module to import - build function to print items.  Can take any number of values

def printItems(*items):
    """loops over array and returns all values"""
    print("The following items are in your list:")
    for item in items:
        print('  - ' + item)

def bookAndType(book, bookType):
    print(book.title() + ' is a ' + bookType + ' book.  Enjoy!')