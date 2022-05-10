from socket import *
from threading import Thread
from typing import List


def start_server(N: int):
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('127.0.0.1', serverPort))
    print('The server is ready to receive')
    return serverSocket


def run(serverSocket: socket, id: int):
    print('thread {0} has started.'.format(id))
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print('[t_id={1}] received message from {0}'.format(clientAddress, id))
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        print('[t_id={0} returned message.'.format(clientAddress))


def main():
    N = 10

    print('start server')
    server = start_server(N)

    threads: List[Thread] = []

    for i in range(N):
        t = Thread(
            target=run,
            args=(server, i + 1)
        )

        t.start()

        threads.append(t)

    for i in range(N):
        threads[i].join()


main()
