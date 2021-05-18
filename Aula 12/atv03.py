"""
3. Criar um script em que threads cooperam para determinar se um conjunto de
cinco números (estáticos) disponibilizados em uma lista são primos ou não. Cada
thread deve ser responsável por um número e exibir uma mensagem informando
o resultado
"""

import concurrent.futures


def checa_primo(i, numeros):
    if i != -1:
        for x in range(2, numeros[1] + 1):
            if x == numeros[i]:
                return i + 1
            elif numeros[i] % x == 0:
                return -1
    return -1


lista = [2, 13, 5, 7, 11]

trabalhador = concurrent.futures.ThreadPoolExecutor()
future1 = trabalhador.submit(checa_primo, 0, lista)
result1 = future1.result()
future2 = trabalhador.submit(checa_primo, result1, lista)
result2 = future2.result()
future3 = trabalhador.submit(checa_primo, result2, lista)
result3 = future3.result()
future4 = trabalhador.submit(checa_primo, result3, lista)
result4 = future4.result()
future5 = trabalhador.submit(checa_primo, result4, lista)
if future5.result() != -1:
    print('Todos os valores são Primos')
else:
    print('Nem todos os valores são primos')
