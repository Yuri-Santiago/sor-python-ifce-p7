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
                resultado += '%4d:%30s|%16.2f R$|%8d|%24.2f R$\n' % (contador, item.get_produto_nome(),
                                                                     item.get_produto_preco(), item.get_quantidade(),
                                                                     item.get_valor_item())
                contador += 1
        else:
            resultado += 'Sem items na Compra\n'

        return resultado

    def listar_itens_separados(self, dado):
        resultado = ""
        contador = 1
        if len(self.itens) > 0:
            for item in self.itens:
                if dado == 'id':
                    resultado += '%d\n' % contador
                elif dado == 'nome':
                    resultado += '%s\n' % item.get_produto_nome()
                elif dado == 'preco':
                    resultado += '%.2f R$\n' % item.get_produto_preco()
                elif dado == 'quantidade':
                    resultado += '%d\n' % item.get_quantidade()
                elif dado == 'total':
                    resultado += '%.2f R$\n' % item.get_valor_item()
                contador += 1
        return resultado

    def remover_item(self, id_item):
        self.itens.pop(id_item)

    def set_item(self, lista):
        self.itens = lista

    def tamanho_lista(self):
        return len(self.itens)
