from socket import * 
serverPort = 12000 
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(('127.0.0.1', serverPort)) 
print('The server is ready to receive') 
while True:
    print('waiting for message')
    message, clientAddress = serverSocket.recvfrom(2048)
    print('received message: {0} from {1}'.format(message.decode(), clientAddress))
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)