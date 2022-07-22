# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions

# TODO: create a basic class

class Book:
    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'This is a secret attribute'
    def getprice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price*self._discount)
        else:
            return self.price
    def setdiscount(self,amount):
        self._discount = amount

# TODO: create instances of the class
pachinko = Book('Pachinko','MJL',500,500)
wap = Book('War and Peace','LT',1350,700)

# TODO: print the class and property
# print(pachinko.title)
# print(wap.getprice())
# wap.setdiscount(0.25)
# print(wap.getprice())
print(wap.__secret)
