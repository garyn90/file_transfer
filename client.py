import socket

"""
this will serve as the code that handles the client (the sender). 
"""

def client(IP, PORT, ADDR, FORMAT, SIZE):
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endpoint = input('Please enter the server\'s IP address.')

    """ attempt to connect to the server. """ 
    try:
        client.connect(endpoint)
    except:
        print("Error connecting to server. Please try again")

    """ Opening and reading the file data. """
    file = open("data/yt.txt", "r")
    data = file.read()
 
    """ Sending the filename to the server. """
    client.send("yt.txt".encode(FORMAT))
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
 
