#import socket module 
from socket import * 
import sys 	#In order to terminate the program 
serverSocket = socket(AF_INET, SOCK_STREAM) 
#serverHost = '10.0.2.5' #virtual machine's IP, it has network access
serverHost = 'localhost' 
recvBuffer = 1024 
serverPort = 22222
#ipaddress = '10.0.2.5' 

#Prepare a server socket 
serverSocket.bind(('', serverPort)) 
#serverSocket.bind((serverHost, serverPort)) 
print("The server is ready to receive")
serverSocket.listen(1)

while True: 
    #Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept() 

    try: 
        message = connectionSocket.recv(recvBuffer)#.decode()
        print('Message is: ', message)
        filename = message.split()[1] 
        print('File name is: ', filename)
        f = open(filename[1:]) 
        outputdata = f.read()

        #Send one HTTP header line into socket 
        connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n','UTF-8'))

        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)): 
            connectionSocket.send(bytes(outputdata[i], 'UTF-8')) 
            #connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send(bytes('\r\n', 'UTF-8'))
        #connectionSocket.send("\r\n".encode()) 
        connectionSocket.close() 

    except IOError: 
        #Send response message for 404 file not found 
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n","UTF-8"))
        connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n","UTF-8"))
        #Close client socket 
        connectionSocket.close()
serverSocket.close() 
sys.exit()#Terminate the program after sending the corresponding data 
