

from socket import * 
import ssl
import base64

msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n" 

#----------------------------------------------------------------------
# Choose a mail server (e.g. Google mail server) and call it mailserver 
#----------------------------------------------------------------------
mailserver = 'external-relay.indiana.edu' 
#mailServer = 'localhost'
mailPort = 25 #25 is standard smtp, 465 is for SSL and 587 for TLS

#---------------------------------------------------------------------------------
# Create socket called clientSocket and establish a TCP connection with mailserver 
#---------------------------------------------------------------------------------
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((mailserver, mailPort))
recv1 = clientSocket.recv(1024).decode() 
print('Recv1 print: ' + recv1) 
if recv1[:3] != '220': #250, 530
    print('220 reply not received from server.')
    
#---------------------------------------------
# Send HELO command and print server response. 
#---------------------------------------------
heloCommand = 'HELO Shane\r\n' 
clientSocket.sendall(heloCommand.encode()) 
recv3 = clientSocket.recv(1024).decode() 
print('Recv3 print: ' + recv3) 
if recv3[:3] != '530':  #250
    print('530 reply not received from server.')

#--------------------------------
# Request an encrypted connection
#--------------------------------
command = 'STARTTLS\r\n'.encode()
clientSocket.send(command)
recv2 = clientSocket.recv(1024).decode()
print('Recv2 print: ' + recv2)
if recv2[:3] != '220':
    print('recv2:220 reply not received from server')

#-------------------
# Encrypt the socket
#-------------------
ssl_clientSocket = ssl.wrap_socket(clientSocket)

#---------------------------------------------
# Send HELO command and print server response. 
#---------------------------------------------
heloCommand = 'HELO Shane\r\n' 
ssl_clientSocket.sendall(heloCommand.encode()) 
recv3 = ssl_clientSocket.recv(1024).decode() 
print('Recv3 print: ' + recv3) 
if recv3[:3] != '530':  #250
    print('530 reply not received from server.')

#---------------------------------------------
# Send the AUTH LOGIN command and print server response.
#---------------------------------------------
authCommand = 'AUTH LOGIN\r\n'
ssl_clientSocket.write(authCommand.encode())
auth_recv = ssl_clientSocket.read(1024)
if auth_recv[:3] != '334':
    print ('334 reply not received from server')

#---------------------------------------------
# Send username and print server response.
#---------------------------------------------
username = input("Type your username and press enter:")
uname = base64.b64encode(username.encode())
print('\r\n')
ssl_clientSocket.write(uname)
uname_recv = ssl_clientSocket.read(1024)
if uname_recv[:3] != '334':
    print ('334 reply not received from server')

#---------------------------------------------
# Send password and print server response.
#---------------------------------------------
password = input("Type your password and press enter:")
pword = base64.b64encode(password.encode())
#print('\r\n')
ssl_clientSocket.write(pword)
pword_recv = ssl_clientSocket.read(1024)
if pword_recv[:3] != '235':
    print ('235 reply not received from server')

#--------------------------------------------------
# Send MAIL FROM command and print server response. 
#--------------------------------------------------
mailfromCommand = 'MAIL FROM: <toddhoward@bethesda.org>\r\n'
ssl_clientSocket.sendall(mailfromCommand.encode())
recv4 = ssl_clientSocket.recv(1024)
print('Recv4 print: ' + recv4)
if recv4[:3] != '530': #250, 530
    print('530 reply not received from server.')


#-------------------------------------------------
# Send RCPT TO command and print server response. 
#-------------------------------------------------
rcpttoCommand = 'RCPT TO: <whimay@iu.edu>\r\n'
ssl_clientSocket.sendall(rcpttoCommand.encode())
recv5 = ssl_clientSocket.recv(1024)
print('Recv5 print: ' + recv5)
if recv5[:3] != '530': #250
    print('rcpt to 530 reply not received from server.')
 
#---------------------------------------------
# Send DATA command and print server response.
#--------------------------------------------- 
dataCommand = 'Data\r\n'
print(dataCommand)
ssl_clientSocket.sendall(dataCommand.encode())
recv6 = ssl_clientSocket.recv(1024)
print('Recv6 print: ' + recv6)
if recv6[:3] != '530':  #250? 354, 530
    print('data 530 reply not received from server.')

#---------------------------------------------
# Send message data. 
#---------------------------------------------
message = 'SUBJECT: Obsidian made my best Fallout game'
fallout76 = 'SUBJECT: I’m sorry about Fallout 76\r\n'
ssl_clientSocket.send(fallout76.encode())
ssl_clientSocket.send(message.encode())
ssl_clientSocket.send(msg.encode())

#---------------------------------------------
# Message ends with a single period.
#--------------------------------------------- 
ssl_clientSocket.sendall(message.encode() + endmsg.encode())
recv7 = ssl_clientSocket.recv(1024)
print('Recv7 print: ' + recv7)
if recv7[:3] != '530': #250, 530
    print('end msg 530 reply not received from server.')

#---------------------------------------------
# Send QUIT command and get server response. 
#---------------------------------------------
quitCommand = 'Quit\r\n'
print(quitCommand)
ssl_clientSocket.sendall(quitCommand.encode())
recv8 = ssl_clientSocket.recv(1024)
print('Recv8 print: ' + recv8)
if recv8[:3] != '221': #250. 221, 530
    print('quit 221 reply not received from server.')


