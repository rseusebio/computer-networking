from socket import *


def run(serverName: str, serverPort: int, N: int):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    arr = ','.join(map(lambda x: str(x + 1), range(N)))
    clientSocket.sendto(arr.encode(), (serverName, serverPort))
    # for i in range(N):
    #     message = str(i + 1)
    #     clientSocket.sendto(rand.encode(), (serverName, serverPort))
    # response, serverAddress = clientSocket.recvfrom(2048)
    # print('response: {0} from {1}.'.format(response, serverAddress))
    clientSocket.close()


def main():
    serverName = '127.0.0.1'
    serverPort = 12000
    N = 10**5
    run(serverName, serverPort, N)


main()
