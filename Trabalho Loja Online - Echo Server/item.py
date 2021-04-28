class Item:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def get_produto(self):
        return self.produto

    def get_produto_nome(self):
        return self.produto.get_nome()

    def get_produto_preco(self):

        return self.produto.get_preco()

    def get_quantidade(self):
        return self.quantidade

    def get_valor_item(self):
        return self.quantidade * self.produto.get_preco()
