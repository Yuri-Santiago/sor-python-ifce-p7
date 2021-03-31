"""
4.Defina uma variável inteira, um float e um decimal atribuindo valores a cada um deles. Qual a
quantidade de memória utilizada por cada um deles?
"""

var_inteira = 5
var_real = 3.2
var_decimal = 0.1

print(var_inteira.__sizeof__())
print(var_real.__sizeof__())
print(var_decimal.__sizeof__())
