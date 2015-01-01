from socket import *
import struct
import sys
import time
#this is a ntp server i found
NTP_SERVER = "pool.ntp.org"
#this is the unix time for January  1 1970
TIME1970 = 2208988800
#create a client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
#connect to ntp port
portNumber = 123
#my sntp_client function
def sntp_client():
    #data to be encrypted and sent to ntp server
    data = '\x1b' + 47 * '\0'
    #send data to ntp server through port
    clientSocket.sendto( data.encode('utf-8'), ( NTP_SERVER, portNumber ))
    #recieve the data and address
    data, address = clientSocket.recvfrom(1024)
    #if there is data return do the following
    if data:
        print ('Response received from:', address)
        #unpack the data and get time at index 10 because that is going to be used to calculate current time
        t_time = struct.unpack( '!12I', data )[10]
        #subtract January 1 1970 to get current date and time
        t_time -= TIME1970
        #princt time and date
        print ('Time= ',time.ctime(t_time))
    #close socket
    clientSocket.close()
#main
if __name__ == '__main__':
    #call function
    sntp_client()