from multiprocessing import connection
from socket import *
serverPort = 8085
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    usr, pwd = connectionSocket.recv(1024).decode().split(':')

    if usr == 'me' and pwd == '123':
        connectionSocket.send('Allowed'.encode())
    else:
        connectionSocket.send('Forbidden'.encode())
    connectionSocket.close()
