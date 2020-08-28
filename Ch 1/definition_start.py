# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class

class Book:
	def __init__(self,title, author, price):
		self.title = title
		self.author = author
		self.price = price

	def setAuthor(self,author):
		self.author = author


	def getPrice(self):
		if(hasattr(self, "__discount")):
			self.price = self.price - self.price * (self.__discount/100)
		return self.price


	def getTitle(self):
		return self.title


	def addDiscount(self,amount):
		__discount = amount




book1 = Book("Cat","Man",30)
book2 = Book("Sparrow","Woman",50)

book2.setAuthor("Leo")
print("The Price for book",book1.getTitle(), "is : ", book1.getPrice())
print("\n\n")
book1.addDiscount(15)
print("The Price after discount for book",book1.getTitle(), "is : ", book1.getPrice())


print(book1.title)
print(book2.title)
# TODO: create instances of the class


# TODO: print the class and property
