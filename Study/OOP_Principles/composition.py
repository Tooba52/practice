# book and bookshelf and independant classes that do not inherit 

class Book:
    def __init__(self, name:str, author:str, publication:int):
        self.__name =name
        self.__author = author
        self.__publication = publication

    def __str__(self):
        return f"{self.__name} was written by {self.__author} and published on {self.__publication}"
        
class Bookshelf:
    def __init__(self):
        self.__books = [] # bookshelf contains objects or type book 

    def add_book(self, book:Book):
        self.__books.append(book)

    def all_books(self):
        return self.__books
    
    def __iter__(self):
        return iter(self.__books)


bookshelf = Bookshelf()
book1 = Book("mistborn", "Brandon Sanderson", 2009)
book2 = Book("GOT", "Martin L", 2002)
book3= Book("Hunters", "Amy M", 2023)
bookshelf.add_book(book1)
bookshelf.add_book(book2)
bookshelf.add_book(book3)
for books in bookshelf:
    print(books)


