from socket import * 
serverPort = 8085 
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('127.0.0.1',serverPort)) 
serverSocket.listen(1) 
print('The server is ready to receive')
connectionSocket, addr = serverSocket.accept()
while True:
    sentence = connectionSocket.recv(1024).decode()
    print('received: {0}'.format())

connectionSocket.close()