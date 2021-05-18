"""
2. Fazer um script em Python que utilize múltiplas threads (5) em que cada thread
exibe a hora atual em sequência num intervalo determinado, porém as threads
são executadas em tempos aleatórios. Por exemplo, T1 5 segundos, T2 7
segundos, T3 13 segundos, T4 23 segundos e T5 26 segundos. A informação
exibida deve identificar também a Thread que está exibindo a informação.
Utilize prints ou logs para exibir as informações.
"""

import threading
import time


def separados(i):
    if i == 0:
        time.sleep(5)
    elif i == 1:
        time.sleep(7)
    elif i == 2:
        time.sleep(13)
    elif i == 4:
        time.sleep(23)
    else:
        time.sleep(26)
    print(f'Thread {i}: Hora Atual: {time.asctime()}\n')
    time.sleep(1)
    print(f'Thread {i} finalizando\n')


if __name__ == "__main__":
    threads = list()
    for index in range(5):
        print(f"Main : cria e inicializa thread {index}.\n")
        x = threading.Thread(target=separados, args=(index, ))
        threads.append(x)
        x.start()
        time.sleep(1)

    for index, thread in enumerate(threads):
        print(f"Main : antes de sincronizar thread {index}.\n")
        time.sleep(1)
        thread.join()
        print(f"Main : thread {index} pronta.\n")
        time.sleep(1)
