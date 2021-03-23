# A partir de uma faixa de números, fazer uma varredura a partir do enésimo número até o final e imprima a soma do
# número atual e os anteriores


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0
n = int(input('Digite o número que vc que começar'))

for x in range(n, len(lista)+1):
    soma += x
print(f'O valor da soma é {soma}')
