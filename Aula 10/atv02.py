"""
2 - Classe Pessoa: Crie uma classe que modele uma pessoa:
    1. Atributos: nome, idade, peso e altura
    2. Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
    sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        self.crescer()

    def engordar(self, ganho):
        if ganho >= 0:
            self.peso += ganho
        else:
            print('Você deve usar o método emagrecer.')

    def emagrecer(self, perda):
        if perda >= 0:
            self.peso -= perda
        else:
            print('Você deve usar o método engordar.')

    def crescer(self):
        if self.idade < 22:
            self.altura += 0.5
        else:
            self.altura += 0


eu = Pessoa('Yuri', 18, 65.3, 176)

for _ in range(5):
    eu.envelhecer()
    print(eu.idade)
    print(eu.altura)

eu.engordar(0.7)
print(eu.peso)
eu.emagrecer(1)
print(eu.peso)

eu.engordar(-1)
print(eu.peso)
eu.emagrecer(-2.3)
print(eu.peso)
