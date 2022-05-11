from socket import *


def run(serverName: str, serverPort: int, N: int):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    for i in range(N):
        message = str(i + 1)
        clientSocket.sendto(message.encode(), (serverName, serverPort))
    clientSocket.close()


def main():
    serverName = '127.0.0.1'
    serverPort = 12000
    N = 10**5
    run(serverName, serverPort, N)


main()
