from socket import * 
serverName = '127.0.0.1'
serverPort = 8085 

clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName,serverPort)) 

while True:
    sentence = input('Input lowercase sentence (0 - to close):\n')

    if sentence == '0':
        break

    clientSocket.send(sentence.encode()) 

    modifiedSentence = clientSocket.recv(1024) 

    print('From Server: ', modifiedSentence.decode())

clientSocket.close()