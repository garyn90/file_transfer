import socket

"""
this will serve as the code that handles the client (the sender). 
"""

def client(IP, PORT, ADDR, FORMAT, SIZE):
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
    file = open(file_input, "r")
    data = file.read()
 
    """ Sending the filename to the server. """
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
 
    """ Sending the file data to the server. """
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
 
    """ Closing the file. """
    file.close()
 
    """ Closing the connection from the server. """
    client.close()
