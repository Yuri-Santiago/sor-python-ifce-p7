"""
Exercício 03 - Classe Carro

Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
    - Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa
    quantidade de combustível no tanque.
    - O consumo é especificado no construtor e o nível de combustível inicial é 0.
    - Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa
    distância, reduzindo o nível de combustível no tanque de gasolina.
    - Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    - Forneça um método adicionarGasolina( ), para abastecer o tanque.
    - Exemplo de uso:
        meuFusca = Carro(15);               # 15 quilômetros por litro de combustível.
        meuFusca.adicionarGasolina(20);     # abastece com 20 litros de combustível.
        meuFusca.andar(100);                # anda 100 quilômetros.
        meuFusca.obterGasolina()            # Imprime o combustível que resta no tanque.
"""


class Carro:
    def __init__(self, consumo_combustivel):
        self.consumo_combustivel = consumo_combustivel
        self.combustivel_tanque = 0

    def andar(self, km):
        litro_total = km / self.consumo_combustivel
        if litro_total <= self.combustivel_tanque:
            self.combustivel_tanque -= litro_total
            return f'Você andou {km} quilômetros gastando {litro_total} litros de combustível'
        else:
            km_dirigido = self.consumo_combustivel * self.combustivel_tanque
            self.combustivel_tanque = 0
            return f'Você andou somente {km_dirigido} quilômetros e seu combustível acabou'

    def obter_gasolina(self):
        return self.combustivel_tanque

    def adicionar_gasolina(self, quantidade):
        if quantidade > 0:
            self.combustivel_tanque += quantidade
            return f'Você abasteceu {quantidade} litros.'
        else:
            return 'Valor de litros inválido'


celta = Carro(10)
print(celta.adicionar_gasolina(15))
print(f'Você possui {celta.obter_gasolina()} litros no tanque')
print(celta.andar(125))
print(f'Você possui {celta.obter_gasolina()} litros no tanque')
print(celta.andar(50))
print(f'Você possui {celta.obter_gasolina()} litros no tanque')
