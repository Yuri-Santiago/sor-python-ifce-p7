"""
2. Escrever uma função que calcule a raiz quadrada de um número positivo.
"""

import math


def raiz_quadrada(num):
    return f'O resultado da raiz quadrada desse número é {math.sqrt(num)}'


valor = int(input('Digite um valor para vermos sua raiz quadrada'))
print(raiz_quadrada(valor))
