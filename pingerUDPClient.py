# UDPPingerClient.py
from socket import *
#import socket
import sys 	#In order to terminate the program 
import time

serverName = '10.0.2.5' #or '10.0.2.4' for vm copy
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('localhost', serverPort))
server_addr = ('localhost', 12000)
clientSocket.settimeout(1)

try:
    for i in range(1, 11):
        start = time.time()
        message = 'Ping #' + str(i) + " " + time.ctime(start)
        try:
            sent = clientSocket.sendto(bytes(message, 'UTF-8'), server_addr) 
            #sent = clientSocket.sendto(bytes(message, 'UTF-8'), (serverName, serverPort)) #message.encode()
            print("Sent " + message)
            data, server = clientSocket.recvfrom(1024)
            print("Received: " + str(data))
            end = time.time();
            elapsed = end - start
            print("RTT: " + str(elapsed) + " seconds\n")
        except timeout:
            print("#" + str(i) + " Requested Time out\n")

finally:
    print("closing socket")
    clientSocket.close()

#while True: 
#    message = input('Input ping message: ')
#    clientSocket.sendto(message.encode(),(serverName, serverPort))
#    message, address = clientSocket.recvfrom(1024)
#    print(message.decode(), address)

clientSocket.close()
sys.exit()
