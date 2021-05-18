"""
1. Escrever um script “hello, world” multi-threaded. Cada thread deve exibir a
mensagem padrão com uma personalização (id da thread, parâmetro passado
na criação, data/hora, etc).
"""

import threading
import time


def hello_world(nome, mensagem):
    print(f'Thread {nome} iniciando\n')
    time.sleep(3)
    print(f'Thread {nome}: "Hello, World. {mensagem}" Time: {time.time()}\n')
    time.sleep(3)
    print(f'Thread {nome} finalizando\n')


if __name__ == "__main__":
    threads = list()
    for index in range(5):
        print(f"Main : cria e inicializa thread {index}.\n")
        time.sleep(2)
        x = threading.Thread(target=hello_world, args=(index, 'Yuri.'))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        print(f"Main : antes de sincronizar thread {index}.\n")
        thread.join()
        print(f"Main : thread {index} pronta.\n")
