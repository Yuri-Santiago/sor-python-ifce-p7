from carteira import Carteira
from compra import Compra


class Usuario:
    def __init__(self, nome, email, senha, carteira=0):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.carteira = Carteira(carteira)
        self.compra = Compra()

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = str(email)

    def get_senha(self):
        return self.senha

    def set_senha(self, senha):
        self.senha = str(senha)

    def get_carteira(self):
        return self.carteira

    def get_compra(self):
        return self.compra

    def fechar_compra(self):
        self.compra = Compra()
