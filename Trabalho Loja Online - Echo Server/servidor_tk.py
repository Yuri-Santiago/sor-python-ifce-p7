from produto import Produto
from item import Item
from usuario import Usuario
from echo_socket import EchoSocket
import pickle

# Criando o Socket do Servidor
socket_servidor = EchoSocket()

# Socket começa a escutar solicitações
socket_servidor.escutar_atomico()

# Salvando os Produtos da Loja e os Usuários
with open('produtos.txt', 'r') as arquivo_produtos:
    linhas = arquivo_produtos.readlines()
produtos = [Produto(p.split('-')[0], float(p.split('-')[1])) for p in linhas]

with open('usuarios.pickle', 'rb') as arquivo_usuarios:
    usuarios = pickle.load(arquivo_usuarios)
usuario = usuarios[0]

# Começo das conexão
while True:
    # Estabelece uma Conexão
    socket_cliente, endereco = socket_servidor.aceitar_cliente()
    print("Conexão Estabelecida com: %s" % str(endereco))

    # Parte do Usuário
    while True:
        menu = socket_cliente.receber_inteiro()

        if menu == 1:
            email = socket_cliente.receber_decodificado()
            senha = socket_cliente.receber_decodificado()
            if email == ' ' or senha == ' ':
                resposta = 'Digite Email e Senha.'
                socket_cliente.enviar(resposta)
            else:
                validacao = 0
                for u in usuarios:
                    if email == u.get_email():  # Verificar se o Email está Cadastrado
                        validacao = 1
                        if senha == u.get_senha():  # Verificar se a Senha está Correta
                            resposta = f'Bem vindo(a) {u.get_nome().split()[0]}!'
                            socket_cliente.enviar(resposta)
                            usuario = u
                        else:  # Senha Errada
                            resposta = 'Senha Incorreta.\nTente Novamente.'
                            socket_cliente.enviar(resposta)
                if validacao == 0:  # Email não Cadastrado
                    resposta = 'Email Não Cadastrado.\nCadastre ou Tente Novamente.'
                    socket_cliente.enviar(resposta)

    # Finaliza a Conexão
    socket_cliente.fechar()
    socket_servidor.fechar()
