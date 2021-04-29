class Compra:
    def __init__(self):
        self.itens = []

    def add_item(self, item):
        self.itens.append(item)

    def get_valor_compra(self):
        return sum(list(map(lambda item: item.get_valor_item(), self.itens)))

    def listar_itens(self):
        resultado = ""
        contador = 1

        if len(self.itens) > 0:
            for item in self.itens:
                if item.get_quantidade() > 1:
                    resultado += '%d: O produto %s tem o valor de %.2f R$ e a quantidade é de %d produtos.\n' % \
                             (contador, item.get_produto_nome(), item.get_produto_preco(), item.get_quantidade())
                else:
                    resultado += '%d: O produto %s tem o valor de %.2f R$.\n' % \
                             (contador, item.get_produto_nome(), item.get_produto_preco())
                contador += 1
        else:
            resultado += 'Sem items na Compra\n'

        return resultado
