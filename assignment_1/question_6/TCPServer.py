from http.client import SWITCHING_PROTOCOLS
from multiprocessing import connection
from socket import *
serverPort = 8085
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

state = 0

final_message = 'Obrigado por utilizar nossos serviços! Até logo!'

while True:
    conn, addr = serverSocket.accept()

    while True:
        print('esperando {0}'.format(state))

        message = conn.recv(2048).decode()

        print('receive {0}'.format(message))

        if state == 0:
            state += 1
            conn.send('Olá! Boas-vindas! Qual seu nome?'.encode())

        elif state == 1:
            state += 1
            conn.send('''Certo, {0}! 
            Como posso te ajudar? 
            Digite o número que corresponde à opção desejada: 
            1 - Agendar horario de monitoria
            2 - Listar proximas atividades da disciplina
            3 - Email do professor'''.format(message).encode())

        elif state == 2:
            state += 1
            if message == '1':
                conn.send(
                    '''Para agendar uma monitoria, basta enviar um email para cainafigueiredo@poli.ufrj.br
                    '''.encode()
                )
            elif message == '2':
                conn.send(
                    '''Fique atento para as datas das proximas atividades. Confira o que vem por aí!
                    P1: 26 de maio de 2022
                    Lista 3: 29 de maio de 2022
                    '''.encode()
                )
            elif message == '3':
                conn.send(
                    '''Quer falar com o professor? O email dele é sadoc@dcc.ufrj.br
                    '''.encode()
                )
            conn.send(final_message.encode())
            state = 0
            break
        else:
            state = 0
            conn.send(final_message.encode())
            break

    conn.close()
