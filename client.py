import socket
from os import path 

"""
this will serve as the code that handles the client (the sender). 
"""

def client(IP, PORT, ADDR, FORMAT, SIZE):

    # remember to delete this 
    size = 1024

    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input('Please enter the server\'s IP address.\n')

    """ attempt to connect to the server. """ 
    try:
        client.connect((server_ip, PORT))
    except Exception as e:
        print(f"Error connecting to server. Status code: {e}. Please try again.")

    """ Opening and reading the file data. """
    file_input = input("Please enter the absolute path of the file to send.\n")
    with open(file_input, 'rb') as f:
        data = f.read()
        while True: 
            chunks = f.read(size)
            if not chunks:
                break 
            client.sendall(chunks)
    # """ Sending the filename to the server. """
    # client.send(data.encode())
    # msg = client.recv(SIZE).decode()
    # print(f"[SERVER]: {msg}")
 
    """ Sending the file data to the server. """
 
 
    """ Closing the connection from the server. """
    client.close()


class Client():
    def __init__(self, IP, PORT, ADDR, SIZE, FORMAT):
        # attributes to be passed in by computer
        self.IP = IP
        self.PORT = PORT 
        self.ADDR = ADDR 
        self.FORMAT = FORMAT 
        self.DIRECTORY = ''
        self.SIZE = SIZE  
        
        #self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        server_ip = input('Please enter the address of the server to connect to.\n')
        try:
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.connect((server_ip, self.PORT))
            while True:
                file_input = input('Please enter the absolute path to the desired file to send, or \'CTRL-C\' to quit.\n')
                if not path.isfile(file_input):
                    continue
                else:
                    print('Valid file.')
                    break
            with open(file_input, 'rb') as file_:
                #send_file = file_.read()
                conn.sendfile(file_)
                

        except Exception as e:
            print(f"Error connecting to server. Status code: {e}. Please try again.")
    
    # try to take the above while loop and contain the entire file sending process into a method 

    # def send_file(self, conn, file):
    #     while True:
    #         conn.send(file)

