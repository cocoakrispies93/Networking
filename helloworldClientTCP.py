from socket import *
serverName = '10.0.2.5'
serverPort = 22222
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input https://10.0.2.5:22222/helloworld.html')
clientSocket.send(clientSocket.recv(1024))
clientSocket.send(sentence.encode())
#modifiedSentence = clientSocket.recv(1024)
#print('From Server: ', modifiedSentence.decode())
clientSocket.close()
