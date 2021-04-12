"""
2. Crie um script para abrir o arquivo criado no item anterior (em modo leitura) e leia
o seu conteúdo e em seguida guarde este conteúdo em uma variável e a exiba
na tela.
"""

import json

arquivo = open('teste.json', 'r')
frase = json.load(arquivo)
print(frase)
