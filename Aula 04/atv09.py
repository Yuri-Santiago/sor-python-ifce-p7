"""
9. Escreva um script que exibe a lista das funções dos módulo re (regular expression) em ordem alfabética.
"""

import re

lista_ordenada = dir(re)
print(lista_ordenada.sort())
