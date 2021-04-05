"""
2. Criar uma lista (angulos) com os ângulos do círculo trigonométrico (0-359) para, a partir
dela criar 3 novas listas (sen, cos, tan) contendo o valor das funções trigonométricas de
cada ângulo como um elemento das listas. Exemplo sen = [0, 0,017, 0,034, ...], cos = [1,
0,9998, 0,9993], tan = [0, 0,01745, 0,3492]
"""

import math

angulos = list(range(359))
print(angulos)
angulos_radianos = list(map(math.radians, angulos))
seno = list(map(math.sin, angulos_radianos))
cosseno = list(map(math.cos, angulos_radianos))
tangente = list(map(math.tan, angulos_radianos))
print(seno)
print(cosseno)
print(tangente)
