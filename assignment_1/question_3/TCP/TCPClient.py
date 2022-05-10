from socket import *
import time
serverName = '127.0.0.1'
serverPort = 8085 
while True:
    # We need to open and close a connect every time 
    # we want to send a message
    clientSocket = socket(AF_INET, SOCK_STREAM) 
    clientSocket.connect((serverName,serverPort))

    sentence = input('Input lowercase sentence (0 - to close):\n')

    if sentence == '0':
        break

    clientSocket.send(sentence.encode()) 

    modifiedSentence = clientSocket.recv(1024) 

    print('From Server: ', modifiedSentence.decode())

    clientSocket.close()