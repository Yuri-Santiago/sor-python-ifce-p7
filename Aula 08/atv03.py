"""
3. Altere o conteúdo do arquivo criado no item 1. Utilize listas, dicionários e números.
Quais os tipos de dados que são criados em cada caso?
"""

import json

arquivo = open('teste.json', 'w', encoding='utf-8')

lista = [1, 2, 3, 4, 5]
dicionario = {'a': 1, 'b': 2, 'c': 3}
numero = 10

json.dump(lista, arquivo)
json.dump(dicionario, arquivo)
json.dump(numero, arquivo)

print('Processo finalizado com Sucesso.')
