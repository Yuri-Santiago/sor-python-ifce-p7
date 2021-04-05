"""
3. Aplique a função math.fmod a todos os elementos da lista nums, de forma que os ítens
sejam copiados para uma nova lista, porém com 3 casas decimais. nums = [1.1765,
1.98387, 5.9364976, 7.845289, 3.9998871]
"""

import math
nums = [1.1765, 1.98387, 5.9364976, 7.845289, 3.9998871]
um = [1, 1, 1, 1, 1]
nova_lista = list(map(lambda x, y: math.fmod(x, y), nums, um))
print(nova_lista)

lista_formatada = list(map(lambda x: int(x * 10**3)/10**3, nova_lista))
print(lista_formatada)
