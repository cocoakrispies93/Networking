from socket import *
serverName = '10.0.2.5' #or '10.0.2.4' for vm copy
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input ping message: ')
clientSocket.sendto(message.encode(),(serverName, serverPort))
message, address = clientSocket.recvfrom(1024)
print(message.decode())
clientSocket.close()
