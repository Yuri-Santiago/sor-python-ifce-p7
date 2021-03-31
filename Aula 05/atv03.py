"""
3.Escrever uma função chamada sed que recebe 4 argumentos: uma string padrão, uma string de
substituição e dois arquivos. O primeiro arquivo deve ser lido e caso a string padrão seja
encontrada, deve ser substituída pela string de substituição e o conteúdo escrito no segundo
arquivo.
"""


def sed(padrao, substituicao, arquivo1, arquivo2):
    arquivo = open(arquivo1)
    linhas = arquivo.readlines()

    for indice, linha in enumerate(linhas):
        palavras = linha.split()
        for palavra in palavras:
            if palavra == padrao:
                linhas[indice] = linhas[indice].replace(padrao, substituicao)
                arquivo_novo = open(arquivo2, 'w')
                novo = ''.join(linhas)
                arquivo_novo.write(novo)


sed('BANANA', 'MELANCIA', 'arquivo_um.txt', 'arquivo_dois.txt')
