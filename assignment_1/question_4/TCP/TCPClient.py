from socket import * 
N = 100
serverName = '127.0.0.1'
serverPort = 8085 

clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName,serverPort)) 

for i in range(N):
    clientSocket.send(str(N + 1).encode())

clientSocket.close()