import socket
import threading
from os import path 
"""
this will handle the endpoint listening to receive files. 
"""

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
        # make sure the user input actually exists 
        while True: 
            self.DIRECTORY = input('Please enter the directory to receive files.\n')
            if not path.exists(self.DIRECTORY):
                continue 
            else:
                break 
        print('Listening for connections. To stop listening press CNTRL-C to quit.')
        self.socket.listen(5)
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
                print("Listening for connections...")
            except ConnectionResetError:
                print(f"Connection to {address} closed.")
            except Exception as e:
                print(f'Error: {e}')
                conn.close()                   
