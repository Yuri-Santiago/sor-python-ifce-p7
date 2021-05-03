class Produto:
    def __init__(self, nome, preco, descricao=''):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, preco):
        if preco > 0:
            self.preco = preco
        else:
            self.preco = 0

    def get_descricao(self):
        return self.descricao
