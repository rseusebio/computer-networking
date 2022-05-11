from socket import *

serverName = '127.0.0.1'
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print('The server is ready to receive')

count = 0
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    count += 1
    flag = 'OUT' if count != int(message.decode()) else ''
    print('received: ' + message.decode() + ' ' + str(count) + ' ' + flag)
    # serverSocket.sendto('done'.encode(), clientAddress)
