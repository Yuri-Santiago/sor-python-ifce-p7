# Escrever um programa em Python em que dada uma lista ccom números inteiros, retorna uma nova lista com os números
# ímpares (ou pares) contidos nesta lista

lista = [1, 5, 2, 8, 6, 4, 7, 3, 9, 10]
lista_sort = sorted(lista)
lista_par = []
lista_impar = []

for valor in lista_sort:
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)

print(f'Os números pares são {lista_par}\nOs números ímpares são {lista_impar}')