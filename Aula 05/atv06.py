"""
6.Qual o tamanho ocupado na memória por uma lista vazia? O que acontece com o tamanho ao
adicionar elementos a lista?

    A medida que acrescentamos determinado número de elementos a lista aumenta de tamanho para se adequar ao dados.
"""

import sys

lista = []
print(sys.getsizeof(lista))

lista.append(1)
print(sys.getsizeof(lista))
lista.append(2)
print(sys.getsizeof(lista))
lista.append(3)
print(sys.getsizeof(lista))
lista.append(4)
print(sys.getsizeof(lista))
lista.append(5)
print(sys.getsizeof(lista))
lista.append(6)
print(sys.getsizeof(lista))
lista.append(7)
print(sys.getsizeof(lista))
