import jsonpickle
import socketserver
from models import Book, BookStore, Library

class User:
    pass

class App:

    def __init__(self):
        self.__actions = {
        'ls': self.list_books,
        'new': self.new_book,
        'del': self.delete_book,
        'get': self.get_book,
        'save': self.save_to_disk,
        'exit': self.should_continue
        }
        self.__book_store = BookStore()
        self.__library = Library()
        self.__next_id = 0

    def should_continue(self):
        return False

    def list_books(self):
        self.__book_store.list()
        return True

    def new_book(self):
        #TODO: get data from client
        author, title, content = ('', '', '')
        book = Book(self.__next_id, author, title, content)
        self.__book_store.add(book)
        self.__next_id += 1
        return True

    def delete_book(self):
        #TODO: get data from client
        book_id = None
        self.__book_store.delete(book_id)
        return True

    def get_book(self):
        #TODO: get data from client
        book_id = None
        book = self.__book_store.get(book_id)
        print(book)
        return True

    def save_to_disk(self):
        # unpacking
        for filename, obj in [('my_lib.json', self.__library), ('my_book_store.json', self.__book_store)]:
            with open(filename, 'w') as lib_file:
                raw_json = jsonpickle.encode(obj)
                lib_file.write(raw_json)
        return True

    def run(self):
        pass
        #TODO: run server

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        pieces = [b'']
        total = 0
        while b'\n' not in pieces[-1] and total < 10_000:
            pieces.append(self.request.recv(2000))
            total += len(pieces[-1])
        self.data = b''.join(pieces)
        print(f"Received from {self.client_address[0]}:")
        print(self.data.decode("utf-8"))
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())
        # after we return, the socket will be closed.

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()



# if __name__ == '__main__':
#     app = App()
#     app.run()
    