"""
5. Escrever um script que solicite ao usuário 3 dados: nome, telefone e email. Os
dados devem ser armazenados em um arquivo (binário ou texto). Cada vez que o
script for executado o arquivo deve ser atualizado com os novos dados.
"""

import json

print('Você deverá escrever o seu Nome, Telefone e Email respectivamente, para serem gravados')

dados = {}
dados['nome'] = input('Digite seu Nome: ')
dados['telefone'] = input('Digite seu número de Telefone: ')
dados['email'] = input('Digite seu Email: ')

with open('teste.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo)
