class Carro:
    def __init__(self, consumo_combustivel):
        self.consumo_combustivel = consumo_combustivel
        self.combustivel_tanque = 0

    def andar(self, km):
        litro_total = km / self.consumo_combustivel
        if litro_total <= self.combustivel_tanque:
            self.combustivel_tanque -= litro_total
            return f'Você andou %.2f quilômetros gastando %.2f litros de combustível' % (km, litro_total)
        else:
            km_dirigido = self.consumo_combustivel * self.combustivel_tanque
            self.combustivel_tanque = 0
            return f'Você andou somente %.2f quilômetros e seu combustível acabou' % km_dirigido

    def obter_gasolina(self):
        return self.combustivel_tanque

    def adicionar_gasolina(self, quantidade):
        if quantidade > 0:
            self.combustivel_tanque += quantidade
            return f'Você abasteceu %.2f litros.' % quantidade
        else:
            return 'Valor de litros inválido'
