import socket
import threading

"""
this will handle the endpoint listening to receive files.
"""

def server(IP, PORT, ADDR, SIZE, FORMAT):
    print('Server has started.')
    print(f'Your IP Address is: { IP }')

    # initializing socket 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()

    while True:
        conn, addr = server.accept()
        print('New connection established')

        # accept any incoming file per FORMAT and sent via SIZE 

        # get the filename 
        filename = conn.recv(SIZE).decode(FORMAT)
        file = open(filename, 'w')
        conn.send('Filename received.').encode(FORMAT)

        # now get the data 
        data = conn.recv(SIZE).decode(FORMAT)
        print("Receiving file data...")
        file.write(data)
        conn.send("File received.")

        # don't leave file-like object open
        file.close()

        # close the socket 
        conn.close()
        print('Connection ended.')


class Server():
    def __init__(self, IP, PORT, ADDR, SIZE, FORMAT):
        # attributes to be passed in by computer
        self.IP = IP
        self.PORT = PORT 
        self.ADDR = ADDR 
        self.FORMAT = FORMAT 
        self.DIRECTORY = '' 
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.ADDR)

    def listen(self):
        print('Server has started.')
        print(f'Your IP Address is: { self.IP }')
        self.DIRECTORY = input('Please enter the directory to receive files.\n')
        print('Listening for connections.')
        self.socket.listen(5)
        while True:
            conn, address = self.socket.accept()
            print('New connection established.')
            threading.Thread(target=self.client_connection, args=(conn, address)).start()
    
    def client_connection(self, conn, address):
        size = 1024
        conn.send(b'Message from server: Connection accepted')
        while True: 
            try:
                data = conn.recv(size)
                print('Receiving file data...')
                file = open(f'{self.DIRECTORY}/newfile', 'w')
                file.write(data)
            except Exception as e:
                conn.send(b'Something went wrong. Try again.')
                print(f'Error: {e}')
                conn.close()
                return False                     
