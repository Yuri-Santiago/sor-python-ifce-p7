"""
1. Crie um script para abrir um arquivo, utilizando modo escrita, e salvar a string “Hello,
world” no mesmo.
"""

import json

frase = "Hello, world"
arquivo = open('teste.json', 'w', encoding='utf-8')
json.dump(frase, arquivo)
print('Processo finalizado com Sucesso.')
