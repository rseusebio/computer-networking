from socket import *
N = 100
serverName = '127.0.0.1'
serverPort = 8085

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

user = input('user:\n')
pwd = input('pwd:\n')

clientSocket.send('{0}:{1}'.format(user, pwd).encode())
msg = clientSocket.recv(2048)
print(msg.decode())
clientSocket.close()
