"""
6. Repita os ítens anteriores utilizado um módulo diferente do utilizado (json ou pickle).
"""

import pickle

frase = "Hello, world"
arquivo = open('teste.pickle', 'wb')
pickle.dump(frase, arquivo)
print('Processo finalizado com Sucesso.')


arquivo = open('teste.pickle', 'rb')
frase = pickle.load(arquivo)
print(frase)


arquivo = open('teste.pickle', 'wb')

lista = [1, 2, 3, 4, 5]
dicionario = {'a': 1, 'b': 2, 'c': 3}
numero = 10

pickle.dump(lista, arquivo)
pickle.dump(dicionario, arquivo)
pickle.dump(numero, arquivo)


lista = []
while True:
    frase = input('Digite uma frase para ser acrescentada a lista, digite "sair" para finalizar: ')
    if frase == 'sair':
        break
    lista.append(frase)

with open('teste.pickle', 'wb') as arquivo:
    pickle.dump(lista, arquivo)

with open('teste.pickle', 'rb') as arquivo:
    frase = pickle.load(arquivo)
    print(frase)


print('Você deverá escrever o seu Nome, Telefone e Email respectivamente, para serem gravados')

dados = {}
dados['nome'] = input('Digite seu Nome: ')
dados['telefone'] = input('Digite seu número de Telefone: ')
dados['email'] = input('Digite seu Email: ')

with open('teste.pickle', 'wb') as arquivo:
    pickle.dump(dados, arquivo)

with open('teste.pickle', 'rb') as arquivo:
    frase = pickle.load(arquivo)
    print(frase)
