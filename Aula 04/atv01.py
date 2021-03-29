"""
1. Escrever uma função que calcule o fatorial de um número inteiro. Uma mensagem de erro deve ser
exibida, caso um número inteiro não positivo seja passado.
"""


def fatorial(num):
    if num >= 0:
        total = 1
        for x in range(1, num+1):
            total *= x
        return f'O fatorial do número {num} é {total}'
    else:
        print('Por favor digite um número positivo')


valor = int(input('Digite um valor para vermos seu fatorial'))
print(fatorial(valor))
