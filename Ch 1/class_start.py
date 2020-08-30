# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances

    Book_Types = ("Hardcover", "Paperback","EBook")
    # TODO: double-underscore properties are hidden from other classes
    @classmethod
    def getBookType(cls):
        return cls.Book_Types
    # TODO: create a class method

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def __init__(self, title,booktype):
        self.title = title
        if(booktype not in Book.Book_Types):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

    def getTitle(self):
        return self.title

    def setTitle(self, newtitle):
       self.title = newtitle 

# TODO: access the class attribute
print(Book.getBookType())

# TODO: Create some book instances
b1 = Book("Title 1","Hardcover")
b2 = Book("Title 2","Paperback")
title  = b2.getTitle()
print(title)

b2.setTitle("Hitelr's War")
print(b2.getTitle())

# TODO: Use the static method to access a singleton object
