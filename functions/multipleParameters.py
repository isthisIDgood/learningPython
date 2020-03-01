##Function with multiple parameters/arguments: Positional Arguments

def bookInfo(bookName, bookType, bookAuthor):
    """This function displays information about the book"""
    print ( bookName.title() + ' is a ' + bookType.lower() + ' book, that was written by ' + bookAuthor.title())

name = input( "Please enter a book name: \n" )
inputType = input( "What is the type of this book?\n" )
author = input( "Who is the author of this book?\n" )

bookInfo(name, inputType, author)
