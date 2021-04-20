"""
1 - Criar uma classe que modele retângulos.
    1. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    2. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    3. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um cômodo.
    Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""


class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_valor_lados(self, a, b):
        self.lado_a = a
        self.lado_b = b

    def retornar_valor_lados(self):
        return self.lado_a, self.lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return self.lado_a * 2 + self.lado_b * 2


print("Nesse programa você deverá informar as medidas de um cômodo em metros.")
comprimento = float(input("Digite o valor do comprimento do Cômodo: "))
largura = float(input("Digite o valor do largura do Cômodo: "))

comodo = Retangulo(comprimento, largura)
print(f'Você usará {comodo.calcular_area()} m quadrados de piso.')
print(f'Você usará {comodo.calcular_perimetro()} m quadrados de rodapé.')
