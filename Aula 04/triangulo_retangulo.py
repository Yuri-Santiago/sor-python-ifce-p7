"""
3. Crie duas funções: uma para calcular a área de um triângulo retângulo e outra para calcular o perímetro.
"""


def area_triangulo_retangulo(cateto_a, cateto_b):
    area = cateto_a * cateto_b / 2
    return f'A área do triângulo é igual a {area}'


def perimetro_triangulo_retangulo(lado_a, lado_b, lado_c):
    perimetro = lado_a + lado_b + lado_c
    return f'O perímetro do triângulo é igual a {perimetro}'
