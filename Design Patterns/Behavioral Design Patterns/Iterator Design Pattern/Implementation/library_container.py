from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class Agregate(ABC):
    def get_iterator(self):
        pass

class BookIterator(Iterator):
    def __init__(self, books):
        self.__i = 0 
        self.__books = books

    def has_next(self):
        return self.__i < len(self.__books)

    def next(self):
        curr = None
        if self.has_next():
            curr = self.__books[self.__i]
            self.__i += 1
        return curr

class LibraryCollection(Agregate):
    def __init__(self):
        self.__books = []

    def add(self, book):
        self.__books.append(book)

    def get_iterator(self):
        return BookIterator(self.__books) 

class Book:
    def __init__(self, name, author):
        self.__name = name 
        self.__author = author 
    
    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author
    
    def __str__(self):
        return f'Book: name : {self.__name} author : {self.__author}'

library = LibraryCollection()

library.add(Book('Harry Porter', 'JK Rowling'))
library.add(Book('One Piece', 'Eichiro Oda'))

iterator = library.get_iterator()

while(iterator.has_next()):
    print(iterator.next())
        