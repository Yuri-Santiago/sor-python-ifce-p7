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
        # Entrar em uma Conta
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
                            break
                        else:  # Senha Errada
                            resposta = 'Senha Incorreta.\nTente Novamente.'
                            socket_cliente.enviar(resposta)
                if validacao == 0:  # Email não Cadastrado
                    resposta = 'Email Não Cadastrado.\nCadastre ou Tente Novamente.'
                    socket_cliente.enviar(resposta)
                else:
                    break
        # Criar uma Conta
        if menu == 2:
            nome = socket_cliente.receber_decodificado()
            email = socket_cliente.receber_decodificado()
            senha = socket_cliente.receber_decodificado()
            if nome == ' ' or email == ' ' or senha == ' ':
                resposta = 'Digite Nome, Email\ne Senha.'
                socket_cliente.enviar(resposta)
            else:
                emails = [u.get_email() for u in usuarios]  # Lista com os emails cadastrados
                if email in emails:
                    resposta = 'Email já Cadastrado. Por Favor, Tente Novamente.'
                    socket_cliente.enviar(resposta)
                else:
                    resposta = f'Conta Criada com Sucesso! \nBem vindo(a) {nome.split()[0]}!'
                    socket_cliente.enviar(resposta)

                    usuario = Usuario(nome, email, senha)
                    usuarios.append(usuario)
                    with open('usuarios.pickle', 'wb') as arquivo_usuarios:
                        pickle.dump(usuarios, arquivo_usuarios)
                    break

    # Finaliza a Conexão
    socket_cliente.fechar()
    socket_servidor.fechar()
