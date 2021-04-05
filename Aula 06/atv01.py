"""
1. Dada a lista [‘abc’, ‘def’, ‘ghi’] aplique uma função para converter cada ítem da
lista em letras maiúsculas, criando uma nova lista. Depois repita a operação convertendo
o primeiro caractere de cada ítem em caractere maiúsculo. Exemplo: 'Abc'.
"""

lista = ['abc', 'def', 'ghi']
nova_lista = list(map(lambda x: x.upper(), lista))
print(nova_lista)
nova_lista2 = list(map(lambda x: x.capitalize(), lista))
print(nova_lista2)
