from socket import *

serverName = '127.0.0.1'
serverPort = 12000 
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message = input('Input lowercase sentence (0 - to close):\n') 
    if message == '0':
        break
    clientSocket.sendto(message.encode(),(serverName, serverPort)) 
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
    print(modifiedMessage.decode()) 
clientSocket.close()