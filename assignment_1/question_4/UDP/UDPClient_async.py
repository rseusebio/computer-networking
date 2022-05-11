from socket import *
from typing import Tuple
import asyncio

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)


async def async_send(message: str):
    clientSocket.sendall(message.encode(), (serverName, serverPort))


async def run(serverName: str, serverPort: int, N: int):

    tasks = []

    for i in range(N):
        t = asyncio.create_task(
            async_send(
                str(i+1)
            )
        )
        tasks.append(t)

    await asyncio.wait(tasks)

    clientSocket.close()


def main():
    serverName = '127.0.0.1'
    serverPort = 12000
    N = 100
    asyncio.run(run(serverName, serverPort, N))


main()
