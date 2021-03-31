"""
2.Escrever um programa em Python que encontre a palavra mais longa em um arquivo.
"""

arquivo = open('exemplo.txt')
linhas = arquivo.readlines()

maior_palavra = ''
for linha in linhas:
    palavras = linha.split()
    for palavra in palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra

print(maior_palavra)
