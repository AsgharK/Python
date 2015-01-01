from datetime import *
from socket import *
from math import *

IP =  '127.0.0.1'

serverPort = 12000

#format the date and time for print
fmt = '[%Y/%m/%d %H:%M:%S]'

#create client socket using SOCK_DGRAM sinc this is a UDP connection
clientSocket = socket(AF_INET, SOCK_DGRAM)

#varaiables for for loop, max, min and average calculations
counter = 10
i = 0
count = 0
min = 0.0
max = 1000.0
total = 0.0
#while loop so ping is sent 10 times
while i<counter:
    sentTime=datetime.now()
    message = "ping"+ ": " + str(i) + " " + str(sentTime)
    clientSocket.sendto(message.encode('utf-8'), (IP, serverPort))
    clientSocket.settimeout(1)
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        #count of total packets actually sent
        count += 1
        #find receivedTime
        receivedTime = datetime.now()
        #calculate rtt
        rtt = receivedTime-sentTime
        #calculate total to use for average
        total += rtt.microseconds
        #find the min and max
        if count == 1:
           min = rtt
           max = rtt
        elif rtt > max:
            max = rtt
        elif rtt < min:
            min = rtt
        print(modifiedMessage.decode("utf-8"), str(sentTime.strftime(fmt)))
    except timeout:
        print("***     timeout     ***")
    i += 1
#convert min and max to milliseconds
mi=min.microseconds*(10**(-3))
ma=max.microseconds*(10**(-3))
#convert total rtt into milliseconds
to=total*(10**(-3))
#print out the min, max, average, and the loss of packet percentage
print("RTT: Min:" + str(mi) + "ms Max:" + str(ma)+ "ms Average:" +  str(to/count) + "ms Packet Loss:" + str(ceil(((10-count)/10.0)*(100.0))) + "%")
clientSocket.close()