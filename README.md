# file_transfer
A simple CLI program to send files between computers on a local network.

Probably an on-going project I will sporadically work on to add new features and capability. The most important thing is to allow any device running the script to choose either of the two available conifgurations. 

A server will provide its local address, and the client device can connect to it over LAN. Currently the server can handle up to 5 connections, with each connection spun off into its own thread. Future improvements will include:

a)sending entire directories
b)maintaining a connection to send files separately
