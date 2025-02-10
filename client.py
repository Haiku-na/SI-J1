import socket
import sys

class Client:

    def __init__(self):
        self.__actions = {
        'ls': self.list_books,
        'new': self.new_book,
        'del': self.delete_book,
        'get': self.get_book,
        'save': self.save_to_disk,
        'exit': self.should_continue
        }


    def should_continue(self):
        return False

    def list_books(self):
        #TODO: List from server
        return True

    def new_book(self):
        title = input('title: ')
        author = input('author: ')
        content = input('content: ')
        #TODO: send to the server
        return True

    def delete_book(self):
        book_id = int(input('Book id: '))

        #TODO: send to the server
        return True

    def get_book(self):
        book_id = input('Book id: ')
        book = None
        #TODO: get book from the server
        print(book)
        return True

    def run(self):
        should_continue = True
        while should_continue:
            action = input('Action? ')
            if action in self.__actions:
                should_continue = self.__actions[action]()
            else:
                print(f'Action not supported {action}')




HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data, "utf-8"))
    sock.sendall(b"\n")

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print("Sent:    ", data)
print("Received:", received)


if __name__ == '__main__':
    client = Client()
    client.run()