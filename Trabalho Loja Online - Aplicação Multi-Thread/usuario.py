from passlib.hash import pbkdf2_sha256 as cryp

from carteira import Carteira
from compra import Compra


class Usuario:
    def __init__(self, nome='', email='', senha='', carteira=0):
        self.nome = nome
        self.email = email
        self.senha = cryp.hash(senha, rounds=200000, salt_size=10)
        self.carteira = Carteira(carteira)
        self.compra = Compra()

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = str(email)

    def get_senha(self):
        return str(self.senha)

    def set_senha(self, senha):
        self.senha = str(senha)

    def get_carteira(self):
        return self.carteira

    def get_compra(self):
        return self.compra

    def fechar_compra(self):
        self.compra = Compra()

    def checa_senha(self, senha):
        if cryp.verify(senha, self.senha):
            return True
        return False
