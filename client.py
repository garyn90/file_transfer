import socket
from os import path 
import tqdm

"""
this will serve as the code that handles the client (the sender). 
"""
class Client():
    def __init__(self, IP, PORT, ADDR, SIZE, FORMAT):
        self.BUFFER_SIZE = 4096
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
            # catch user input mistake, and keep asking for a proper file input from the user, continues when it finds a file 
            while True:
                file_input = input('Please enter the absolute path to the desired file to send, or \'CTRL-C\' to quit.\n')
                if not path.isfile(file_input):
                    continue
                else:
                    break
            print('Valid file.')
            # grab the filename to send to server        
            file_name = path.basename(file_input)
            # this is just for the progress bar 
            file_size = path.getsize(file_input)
            # then send it, remembering to encode 
            conn.send(file_name.encode())
            progress = tqdm.tqdm(range(file_size), f'Sending {file_name}', unit='B', unit_scale=True)
            with open(file_input, 'rb') as file_:
                while True: 
                    bytes = file_.read(self.BUFFER_SIZE)
                    if not bytes:
                        break
                    conn.sendall(bytes)
                    progress.update(len(bytes))
            print('Finished sending file. Closing.')
            conn.close()
                    
                    
        except Exception as e:
            print(f"Error connecting to server. Status code: {e}. Please try again.")
    
    # try to take the above while loop and contain the entire file sending process into a method 

    # def send_file(self, conn, file):
    #     while True:
    #         conn.send(file)

