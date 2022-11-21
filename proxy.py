from socket import * 
import sys 
if len(sys.argv) <= 1: 
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server') 
    sys.exit(2) 

# Create a server socket, bind it to a port and start listening 
tcpSerSock = socket(AF_INET, SOCK_STREAM) 
# Fill in start. 
tcpSerPort = 8888
tcpSerSock.bind(('127.0.0.1',tcpSerPort))
tcpSerSock.listen(1)
# Fill in end.

while 1: 
    # Strat receiving data from the client 
    print('Ready to serve...') 
    tcpCliSock, addr = tcpSerSock.accept() 
    print('Received a connection from:', addr) 
    message = tcpCliSock.recv(1024).decode( ) 
    # Fill in start.
    if message.split()[1]==None:
        continue
    if message.split()[1]!='/www.google.com':
        continue
    if message.split()[1]=='/favicon.ico':
        continue
    # Fill in end.
    print(message) 

    # Extract the filename from the given message 
    print(message.split()[1]) 
    filename = message.split()[1].partition("/")[2] 
    print(filename) 
    fileExist = "false" 
    filetouse = "/" + filename 
    print(filetouse) 
    try: 
        # Check wether the file exist in the cache 
        f = open(filetouse[1:], "rb")
        outputdata = f.readlines() 
        fileExist = "true" 
        # ProxyServer finds a cache hit and generates a response message 
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode()) 
        tcpCliSock.send("Content-Type:text/html\r\n".encode()) 
        # Fill in start.
        # for i in range(0,len(outputdata)):
        tcpCliSock.send(outputdata[i].encode())
        tcpCliSock.send("\r\n".encode())
        tcpCliSock.close()
        f.close() 
        # Fill in end. 
        print('Read from cache') 

    # Error handling for file not found in cache 
    except IOError: 
        if fileExist == "false": 
        # Create a socket on the proxyserver 
            c = socket(AF_INET, SOCK_STREAM
            # Fill in start.
            hostn = filename.replace("www.","",1)
            print(hostn)

            try:
                # Connect to the socket to port 80
                c.connect((hostn,80))
                print ('Socket connected to port 80')
                # # Fill in end. 

                # Create a temporary file on this socket and ask port 80 
                #for the file requested by the client 
                fileobj = c.makefile('rmb', 0) 
                fileobj.write("GET ".encode() + "http://".encode() + filename.encode() + "HTTP/1.0\n\n".encode()) 
                # Read the response into buffer

                # Fill in start. 
                buff="GET"+' /'+" HTTP/1.1\r\n\r\n"
                c.send(buff.encode())
                recv = c.recv(15000000)
                # Fill in end. 

                # Create a new file in the cache for the requested file. 
                # Also send the response in the buffer to client socket 
                #and the corresponding file in the cache 
                tmpFile = open("./" + filename,"wb")

                # Fill in start. 
                tmpFile.write(recv)
                print('successfully save')
                tcpCliSock.send(recv)
                # Fill in end. 
            except: 
                print("Illegal request") 
        else: 
        # HTTP response message for file not found 
        # Fill in start. 
            status_line='HTTP/1.1 404 Not Found'
            connectionSocket.send(status_line.encode())
            connectionSocket.close()
        # Fill in end. 
# Close the client and the server sockets 
    tcpCliSock.close() 
tcpSerSock.close()

