"""
6. Reescreva os exemplos anteriores utilizando o módulo criado no ítem anterior.
7. Inserir as funções criadas em módulos para que possam ser utilizadas em outros programas.
8. Escreva um script que importe o módulo criado e utlize-as durante a execução.
"""

import triangulo_retangulo

print(f'O valor de a área de um triangulo retangulo de base 2 e altura 4 é '
      f'{triangulo_retangulo.area_triangulo_retangulo(2, 4)}')

print(f'O valor do perímetro de um triangulo retangulo de lados 2, 4 e 6 é '
      f'{triangulo_retangulo.perimetro_triangulo_retangulo(2, 4, 6)}')
