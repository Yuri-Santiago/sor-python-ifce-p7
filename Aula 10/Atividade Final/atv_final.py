"""
1. Controle de cotas de disco. A ACME Inc., uma organização com mais de 1500 funcionários, está tendo problemas de
espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber
qual o espaço em disco ocupado pelas contas dos usuários, e identificar os usuários com maior espaço ocupado. Através
de um aplicativo baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado usuarios.txt:

alexandre   456123789
anderson    1245698456
antonio     123456456
carlos      91257581
cesar       987458
rosemary    789456125

Neste arquivo, o primeiro campo corresponde ao login do usuário e o segundo ao espaço em disco ocupado pelo seu
diretório home. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado relatório.txt, no
seguinte formato:

ACME Inc.           Uso do espaço em disco pelos usuários
---------------------------------------------------------
Nr.     Usuário     Espaço utilizado    % do uso
1       alexandre   434,99 MB           16,85%
2       anderson    1187,99 MB          46,02%
3       antonio     117,73 MB           4,56%
4       carlos      87,03 MB            3,37%
5       cesar       0,94 MB             0,04%
6       rosemary    752,88 MB           29,16%
Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a
agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá
ser feito através de uma função, que será chamada pelo programa principal.
"""


def converter(numero):
    return numero / 1024 ** 2


def percentual(numeros):
    soma = sum(numeros)
    porcentagens = [numero * 100 / soma for numero in numeros]
    return porcentagens


arquivo = open('usuarios.txt', 'r')
linhas = arquivo.readlines()

pessoas = [pessoa.split()[0] for pessoa in linhas]
lista = [int(pessoa.split()[1]) for pessoa in linhas]

convertido = list(map(converter, lista))
porcentagem = percentual(lista)

total = sum(convertido)
media = total / len(convertido)
arquivo.close()

string = 'ACME Inc.         Uso do espaco em disco pelos usuarios\n' + '-'*55 + \
         '\nNr.        Usuario       Espaco utilizado      % do uso\n'
for x in range(len(linhas)):
    string += '%d %16s %19.2f MB %11.2f %s\n' % (x+1, pessoas[x], convertido[x], porcentagem[x], '%')
string += 'Espaco total ocupado: %.2f MB \nEspaco medio ocupado: %.2f MB' % (total, media)

with open('relatório.txt', 'w') as a:
    a.write(string)
a.close()
