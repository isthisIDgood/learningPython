##Function with default parameters

def bookInfo(bookName, bookAuthor, bookType="nonfiction"):

    """This function displays information about the book"""
    print ( bookName.title() + ' is a ' + bookType.lower() + ' book, that was written by ' + bookAuthor.title())


bookInfo(bookName='Inheritance', bookAuthor='Chris')

##Function with default parameters

def bookInfo(bookName, bookAuthor, bookType="fiction"):

    """This function displays information about the book"""
    print ( bookName.title() + ' is a ' + bookType.lower() + ' book, that was written by ' + bookAuthor.title())


bookInfo(bookName='Inheritance', bookAuthor='Chris', bookType='fiction')
