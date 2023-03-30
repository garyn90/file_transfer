import socket
from server import Server
from client import client

# automatically nab the IP address
IP = socket.gethostbyname(socket.gethostname())
print(type(IP))
print(IP)
PORT = 8000 
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = 'utf-8'

""" 
this is a simple CLI program for personal use. the goal is to have a quick method to send files between the laptop and pc, along with the option to introduce threads
to handle file transfers concurrently. system agnoticism is ideal, since you are using a unix laptop and a windows pc. 
"""

user_inp= input('File transfer program initiated.\nPress 1 for CLIENT, or 2 for SERVER. Or Q to quit: \n')

if user_inp == '1':
    print('You have chosen CLIENT...')
    """ put client code here. remember that client will be able to send files only, hence the option to switch """
    client(IP, PORT, ADDR, SIZE, FORMAT)

if user_inp == '2':
    print('You have chosen SERVER...')
    """ put server code here. server option will receive files. """
    Server(IP, PORT, ADDR, SIZE, FORMAT).listen()

if user_inp =='q' or 'Q':
    quit()