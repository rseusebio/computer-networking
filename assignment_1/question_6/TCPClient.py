from pydoc import cli
from socket import *
from string import digits
N = 100
serverName = '127.0.0.1'
serverPort = 8085

msg = 'oi'

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    clientSocket.send(msg.encode())
    res = clientSocket.recv(2048).decode()
    print(res)
    if res.find('Até logo!') >= 0:
        break
    if msg in digits:
        print(clientSocket.recv(2048).decode())
        break
    msg = input('')

clientSocket.close()
