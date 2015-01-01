from socket import *
import base64
import ssl


sendTo = "<email>"
sendFrom = "<email>"
username = "youremailusername"
#password not included
password = "*********"
# Setup messages

msg = "\r\nI love computer networks!" 	# email body

endMsg = "\r\n.\r\n"					# end of body

# Choose a mail server (e.g. Google mail server) and call it mailserver

mailServer =("smtp.gmail.com",587)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailServer)


recv = clientSocket.recv(1024)
print(recv.decode('utf-8'))
if recv.decode('utf-8')[:3] != '220':
     print('220 reply not received from server.')
     

# Send EHLO command and print server response.
ehloCommand = 'EHLO Alice\r\n'
clientSocket.send(bytes(ehloCommand,'utf-8'))
ehlo_recv = clientSocket.recv(1024)
print(ehlo_recv.decode('utf-8'))
if ehlo_recv.decode('utf-8')[:3] != '250':
    print('250 reply not received from server.')


# Start tls connection for encryption
startTlsCommand = "STARTTLS \r\n"
clientSocket.send(startTlsCommand.encode('utf-8'))
recv_tls = clientSocket.recv(1024)
print(recv_tls.decode('utf-8'))

# Encrypt the socket using ssl wrap
ssl_clientSocket = ssl.wrap_socket(clientSocket, ssl_version = ssl.PROTOCOL_SSLv23)


# Second EHLO command just to check Starttls
ehloCommand2 = 'EHLO Alice\r\n'
ssl_clientSocket.send(bytes(ehloCommand2,'utf-8'))
ehlo_recv2 = ssl_clientSocket.recv(1024)
print(ehlo_recv2.decode('utf-8'))
if ehlo_recv2.decode('utf-8')[:3] != '250':
    print('250 reply not received from server.')

# Send the AUTH LOGIN command and print server response.
authCommand = 'AUTH LOGIN\r\n'
ssl_clientSocket.send(authCommand.encode('utf-8'))
auth_recv = ssl_clientSocket.recv(1024)
print(auth_recv.decode('utf-8'))
if auth_recv.decode('utf-8')[:3] != '334':
    print('334 reply not received from server')

# Send username and print server response.
uname = base64.b64encode(username.encode('utf-8')).decode('utf-8') + '\r\n'
ssl_clientSocket.send(uname.encode('utf-8'))
u_recv = ssl_clientSocket.recv(1024)
print(u_recv.decode('utf-8'))
if u_recv.decode('utf-8')[:3] != '334':
    print('334 reply not received from server')

# Send password and print server response.
pword = base64.b64encode(password.encode('utf-8')).decode('utf-8') + '\r\n'
ssl_clientSocket.send(pword.encode('utf-8'))
p_recv = ssl_clientSocket.recv(1024)
print(p_recv.decode('utf-8'))
if p_recv.decode('utf-8')[:3] != '235':
    print('235 reply not received from server')


# Send MAIL FROM command and print server response.
mailFrom = 'MAIL FROM: ' + sendFrom + '\r\n'
ssl_clientSocket.send(mailFrom.encode('utf-8'))
from_recv = ssl_clientSocket.recv(1024)
print(from_recv.decode('utf-8'))
if from_recv.decode('utf-8')[:3] != '250':
    print('250 reply not received from server.')


# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: ' + sendTo + '\r\n'
ssl_clientSocket.send(rcptToCommand.encode('utf-8'))
to_recv = ssl_clientSocket.recv(1024)
print(to_recv.decode('utf-8'))
if to_recv.decode('utf-8')[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
ssl_clientSocket.send(dataCommand.encode('utf-8'))
data_recv = ssl_clientSocket.recv(1024)
print(data_recv.decode('utf-8'))
if data_recv.decode('utf-8')[:3] != '354':
    print('354 reply not received from server.')


# Send message subject, body and data
ssl_clientSocket.send(msg.encode('utf-8'))

# Message ends with a single period.
ssl_clientSocket.send(endMsg.encode('utf-8'))
end_recv = ssl_clientSocket.recv(1024)
print(end_recv.decode('utf-8'))
if end_recv.decode('utf-8')[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
ssl_clientSocket.send(quitCommand.encode('utf-8'))
quit_recv = ssl_clientSocket.recv(1024)
print(quit_recv.decode('utf-8'))
if quit_recv.decode('utf-8')[:3] != '221':
    print('221 reply not received from server.')

clientSocket.close()
