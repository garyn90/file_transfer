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
        self.BUFFER_SIZE = 4096
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
        print('Listening for connections. To stop listening, press Q to quit.')
        self.socket.listen(5)
        # offer input to cleanly close the program
        if input() == 'q':
            quit()
        while True:
            conn, address = self.socket.accept()
            print(f'New connection established: {address}')
            threading.Thread(target=self.client_connection, args=(conn, address)).start()
    
    def client_connection(self, conn, address):
        received_filename = conn.recv(self.BUFFER_SIZE).decode()
        with open(self.DIRECTORY + '/' + received_filename, 'wb') as file_: 
            try:
                print('Receiving file data...')
                while True:
                    incoming_bytes = conn.recv(self.BUFFER_SIZE)
                    if not incoming_bytes: 
                        break 
                    file_.write(incoming_bytes)
                print("File has been received.")
                conn.close()

            except ConnectionResetError:
                print(f"Connection to {address} closed.")
                print("Listening for connections. To stop listening, press Q to quit.")
            except Exception as e:
                print(f'Error: {e}')
                conn.close()                   
