class Book:
    library = "City Central Library"

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def displayBook(self):
        return f'Title: {self.title}\n Author: {self.author}\n Price: {self.price}\n Library: {self.library}'
    
    @classmethod
    def from_string(cls, string):
        result = string.split('-')
        return cls(result[0], result[1], result[2])

# book = Book('Abc', 'abc', 400)
# print(book.displayBook())


book = Book.from_string('Atomic Habits-James Clear-499')
print(book.displayBook())


# Difference between the static method and class method
class Emp:

    @staticmethod
    def sayHello():
        print('Hiii')
        # Hiii
    

    @classmethod
    def sayHii(cls):
        print(cls)
        # <class '__main__.Emp'>

Emp.sayHello()
Emp.sayHii()