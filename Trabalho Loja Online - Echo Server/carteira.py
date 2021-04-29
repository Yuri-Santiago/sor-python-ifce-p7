class Carteira:
    def __init__(self, total):
        self.total = total

    def get_total(self):
        return self.total

    def pagar(self, valor):
        if self.total >= valor:
            self.total -= valor
            return 'Pagamento Aprovado.\nCompra Bem Sucedida!'
        return 'Pagamento Não Aprovado.\nCompra Cancelada.'

    def adicionar(self, valor):
        if valor > 0:
            self.total += valor
            return 'Valor Adicionado na Carteira.\nO Valor Atual é: %.2f' % (self.total)
        return 'Valor Inválido'
