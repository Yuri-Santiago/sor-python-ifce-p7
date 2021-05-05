"""
3 - Classe Bomba de Combustível: Faça um programa completo utilizando classses e métodos que:
    1. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
    2. tipoCombustivel.
    3. valorLitro
    4. quantidadeCombustivel
    5. Possua no mínimo esses métodos:
    6. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi
    colocada no veículo
    7. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago
    pelo cliente.
    8. alterarValor( ) – altera o valor do litro do combustível.
    9. alterarCombustivel( ) – altera o tipo do combustível.
    10.alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
    11.OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba
"""


class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        if valor > 0:
            litro = valor / self.valor_litro
            self.quantidade_combustivel -= litro
            return litro
        return 0

    def abastecer_por_litro(self, litro):
        if litro > 0:
            valor = litro * self.valor_litro
            self.quantidade_combustivel -= litro
            return valor
        return 0

    def alterar_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor_litro = novo_valor
        else:
            print('Alteração inválida')

    def alterar_combustivel(self, novo_tipo):
        self.tipo_combustivel = novo_tipo

    def alterar_quantidade_combustivel(self, quantidade):
        if quantidade >= 0:
            self.quantidade_combustivel = quantidade
        else:
            print('Alteração inválida')


bomba = BombaCombustivel('Gasolina', 4, 100)
print(bomba.tipo_combustivel)
print(bomba.valor_litro)
print(bomba.quantidade_combustivel)

print(f'A quantidade de litros abstecidas com 8 reais é: {bomba.abastecer_por_valor(8)}')
print(bomba.quantidade_combustivel)
print(f'A quantidade reais precisos para abastecer 10 litros é: {bomba.abastecer_por_litro(10)}')
print(bomba.quantidade_combustivel)

bomba.alterar_combustivel('Etanol')
bomba.alterar_valor(4.20)
bomba.alterar_quantidade_combustivel(200)

print(bomba.tipo_combustivel)
print(bomba.valor_litro)
print(bomba.quantidade_combustivel)
