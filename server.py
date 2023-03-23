import socket

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
