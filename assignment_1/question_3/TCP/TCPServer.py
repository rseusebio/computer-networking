from socket import *
from threading import Thread
from typing import List


def start_server(N: int):
    serverPort = 8085
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('127.0.0.1', serverPort))
    serverSocket.listen(N)
    print('The server is ready to receive')
    return serverSocket


def run(serverSocket: socket, id: int):
    print('thread {0} has started.'.format(id))
    while True:
        connectionSocket, addr = serverSocket.accept()
        print('[t_id={1}] Connection established with {0}'.format(addr, id))
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
        connectionSocket.close()
        print('[t_id={0}] connection closed.'.format(id))


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
