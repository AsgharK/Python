__author__ = 'Asghar'
import time
import socket
import struct

#specifi mutlicast group and port
multicast_group=('224.3.29.71', 10000)
#create server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#this is for the initial TTL of multicast datagram
ttl = struct.pack('b', 127)
#set the socket with multicast and ttl
serverSocket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

#keep trying to send messages until server is killed
while True:
    try:
        #message to be send
        message = "Multi-casting Assignment ECE 4436 from Server 1"
        #send message
        sent = serverSocket.sendto(message.encode('utf-8'), multicast_group)
        print('Server 1: multicast packet is sent now')

    #telling program to sleep for 3 seconds so a packet is send every three seconds
    finally:
        time.sleep(3)

#lastly close the server socket
serverSocket.close()
