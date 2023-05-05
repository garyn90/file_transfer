import socket
from server import Server
from client import Client

""" 
this is a simple CLI program for personal use. the goal is to have a quick method to send files between the laptop and pc, 
along with the option to introduce threads to handle multiple file transfers concurrently. 
system agnoticism is ideal, since you are using a unix laptop and a windows pc.

files will be sent over TCP stream.
"""

# set of configurations that are hosted here, which are then passed into whichever respective object the user chooses 
IP = socket.gethostbyname(socket.gethostname())
PORT = 8000 
ADDR = (IP, PORT)
SIZE = 5000000
FORMAT = 'utf-8'


user_inp= input('File transfer program initiated.\nPress 1 for CLIENT, or 2 for SERVER. Or Q to quit: \n')

if user_inp == '1':
    print('You have chosen CLIENT...')
    """ put client code here. remember that client will be able to send files only, hence the option to switch """
    Client(IP=IP, PORT=PORT, ADDR=ADDR, SIZE=SIZE, FORMAT=FORMAT).connect()

if user_inp == '2':
    print('You have chosen SERVER...')
    """ put server code here. server option will receive files. """
    Server(IP=IP, PORT=PORT, ADDR=ADDR, SIZE=SIZE, FORMAT=FORMAT).listen()

if user_inp =='q' or 'Q':
    quit()