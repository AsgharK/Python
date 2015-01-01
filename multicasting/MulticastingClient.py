__author__ = 'Asghar'
from datetime import *
import socket
import struct
import sys
from math import *

#multicast group ip address
multicast_group = '224.3.29.71'
#default ip address and port
server_address = ('', 10000)

# create a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to the server address
clientSocket.bind(server_address)

#indetifiying the multicast_group and setting the client socket to connect with the multicast address
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
clientSocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

#while loop continues and waits to recv form server.
while True:
    #receive the packet from server
    data, address = clientSocket.recvfrom(1024)

    #prints the address of server that sent the message
    print('Client 1: Data Received from: ', address)
    #prints the data received from server
    print('and the Received Data is: ', data)

#close client socket
clientSocket.close()