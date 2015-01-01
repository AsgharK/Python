# We will need the following module to generate randomized lost packets 
import random
from datetime import datetime
from socket import * 
 
# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets 
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('127.0.0.1', 12000))
 
while True: 
# Generate random number in the range of 0 to 10 
    rand = random.randint(0, 10)
# Receive the client packet along with the address it is coming from 
    message, address = serverSocket.recvfrom(1024)
# Capitalize the message from the client
    message = message.upper() 
# If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
        # Otherwise, the server responds
    #just formating the message for printing and sending return message
    printMessage = message.split()[2] + (" ").encode('utf-8') +  message.split()[3]
    print(printMessage)
    returnMessage = message.split()[0] + message.split()[1]
    serverSocket.sendto(returnMessage, address)

