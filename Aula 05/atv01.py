"""
1.Escrever um programa em Python para informar ao usuário a quantidade de linhas e caracteres
de um arquivo texto.
"""

arquivo = open('exemplo.txt')
linhas = arquivo.readlines()

print(f'O número de linhas desse arquivo é {len(linhas)}')

arquivo.seek(0)
passe = 0
caracteres = 0

while passe < 1:
    caractere = arquivo.read(1)
    caracteres += 1
    if caractere == '':
        passe = 1

print(f'O número de caracteres desse arquivo é {caracteres}')
