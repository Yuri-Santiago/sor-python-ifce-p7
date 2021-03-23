# Escrever um programa que informe ao usuário o maior e o menor elemento de uma lista e o valor médio dos elementos da
# lista. Utilize uma lista com 10 elementos.

lista = [2, 4, 7, 3, 1, 0, 6, 9, 5, 8]
lista_ascendente = sorted(lista)
print(f'{lista_ascendente}')
print(f'O menor elemento é {lista_ascendente[0]} e o maior é {lista_ascendente[-1]}')

valor_medio = (lista_ascendente[4] + lista_ascendente[5]) / 2
print(f'O valor médio da lista é {valor_medio}')
