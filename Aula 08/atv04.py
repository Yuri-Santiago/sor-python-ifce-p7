"""
4. Crie um script para criar uma lista de frases digitadas pelo usuário. Em seguida a lista
deve ser salva em um arquivo.
"""

import json

lista = []
while True:
    frase = input('Digite uma frase para ser acrescentada a lista, digite "sair" para finalizar: ')
    if frase == 'sair':
        break
    lista.append(frase)

with open('teste.json', 'w', encoding='utf-8') as arquivo:
    json.dump(lista, arquivo)
