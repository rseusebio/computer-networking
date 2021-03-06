from socket import * 
serverPort = 8085 
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('127.0.0.1',serverPort)) 
serverSocket.listen(1) 
print('The server is ready to receive')

connectionSocket, addr = serverSocket.accept()
print('Connection established with {0}'.format(addr))
while True:
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
connectionSocket.close()
print('connection closed.')