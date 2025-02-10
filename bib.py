import json
# import jsonpickle
class Book:
    #dunder
    def __init__(self, id, title, author, content):
        self.__titre = title
        self.__auteur = author
        self.__contenu = content
        self.__id = id #do not expose the id
        
    @property
    def title(self):
        return self.__title
    @property
    def author(self):
        return self.__author
    @property
    def content(self):
        return self.__content
    @property
    def id(self):
        return self.__id
        
    @title.setter
    def title(self, value):
        self.title = value

    @author.setter
    def author(self, value):
        self.author = value

    @content.setter
    def content(self, value):
        self.content = value

    @id.setter
    def id(self, value):
        self.id = value
        

class BookStore:
    pass
class Library:
    pass
class User:
    pass


def list_books():
    print(book_store.list())

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    content = input("Content: ")
    book = Book(0, title, author, content)
    book_store.add(book)

def del_book():
    id = input("Id: ")
    book_store.delete(id)

if __name__ == '__main__': 
    book_store = BookStore()
    input_action = input("Action: ")
    actions = {
        "ls":list_books,
        "new":add_book,
        "del":del_book,
        } 
    print(actions[input_action]())
