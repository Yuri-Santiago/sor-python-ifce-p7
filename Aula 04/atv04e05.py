"""
4. Criar um script que utilize as funções do ítem anterior retornar ao usuário a área e o perímetro de um
triângulo retângulo.
5. Criar um módulo que incorpore as funções de área e perímetro do triângulo retângulo feitas em ítens
anteriores.
"""

import triangulo_retangulo

print('Digite os valores dos lados de um triângulo retângulo')
cateto1 = int(input('Digite o cateto a'))
cateto2 = int(input('Digite o cateto b'))
hipotenusa = int(input('Digite a hipotenusa'))

print(triangulo_retangulo.area_triangulo_retangulo(cateto1, cateto2))
print(triangulo_retangulo.perimetro_triangulo_retangulo(cateto1, cateto2, hipotenusa))
