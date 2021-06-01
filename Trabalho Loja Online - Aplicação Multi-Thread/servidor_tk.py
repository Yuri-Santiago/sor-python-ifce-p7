import pickle
import threading

from echo_socket import EchoSocket
from item import Item
from produto import Produto
from usuario import Usuario

# Criando o Socket do Servidor
socket_servidor = EchoSocket()

# Socket começa a escutar solicitações
socket_servidor.escutar_atomico()

# Salvando os Produtos da Loja e os Usuários
with open('produtos.pickle', 'rb') as arquivo_produtos:
    produtos_bytes = pickle.load(arquivo_produtos)
produtos = [Produto(p.nome, p.preco, p.descricao) for p in produtos_bytes]

with open('usuarios.pickle', 'rb') as arquivo_usuarios:
    usuarios_cadastrados = pickle.load(arquivo_usuarios)

usuario_inicial = usuarios_cadastrados[0]
usuarios_ativos = []


def salvar_usuario(usuario_final):
    with open('usuarios.pickle', 'rb') as arquivo_final:
        usuarios_finais = pickle.load(arquivo_final)

    for usuario_lista in usuarios_finais:
        if usuario_final.get_email() == usuario_lista.get_email():
            usuarios_finais[usuarios_finais.index(usuario_lista)] = usuario_final

    with open('usuarios.pickle', 'wb') as arquivo_final:
        pickle.dump(usuarios_finais, arquivo_final)

    usuarios_ativos.remove(usuario_final)


def enviar_usuario(cliente, usuario_atualizado):
    usuario_byte = pickle.dumps(usuario_atualizado)
    cliente.enviar_bytes(usuario_byte)


# Função Principal
def guardar_usuario(usuario):
    usuarios_ativos.append(usuario)


def aplicacao(socket_cliente, endereco, usuario):
    print("Conexão Estabelecida com: %s" % str(endereco))
    # Envio Produtos para o Cliente
    produtos_byte = pickle.dumps(produtos)
    socket_cliente.enviar_bytes(produtos_byte)
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
                for u in usuarios_cadastrados:
                    if email == u.get_email():  # Verificar se o Email está Cadastrado
                        validacao = 1
                        if senha == u.get_senha():  # Verificar se a Senha está Correta
                            if u not in usuarios_ativos:  # Verifica se o usuario não está conectado
                                resposta = 'Bem vindo'
                                socket_cliente.enviar(resposta)
                                usuario = u
                                enviar_usuario(socket_cliente, usuario)
                                guardar_usuario(usuario)
                                break
                            else:  # Usuário já conectado
                                resposta = 'Este usuário já está Conectado\nDesconecte ou Tente Outro Usuário'
                                socket_cliente.enviar(resposta)
                        else:  # Senha Errada
                            resposta = 'Senha Incorreta.\nTente Novamente.'
                            socket_cliente.enviar(resposta)
                if validacao == 0:  # Email não Cadastrado
                    resposta = 'Email Não Cadastrado.\nCadastre ou Tente Novamente.'
                    socket_cliente.enviar(resposta)
        # Criar uma Conta
        elif menu == 2:
            nome = socket_cliente.receber_decodificado()
            email = socket_cliente.receber_decodificado()
            senha = socket_cliente.receber_decodificado()
            if nome == ' ' or email == ' ' or senha == ' ':
                resposta = 'Digite Nome, Email\ne Senha.'
                socket_cliente.enviar(resposta)
            else:
                emails = [u.get_email() for u in usuarios_cadastrados]  # Lista com os emails cadastrados
                if email in emails:
                    resposta = 'Email já Cadastrado. \nPor Favor, Tente Novamente.'
                    socket_cliente.enviar(resposta)
                else:
                    resposta = 'Conta criada'
                    socket_cliente.enviar(resposta)
                    nome_correto = nome.title().strip()
                    usuario = Usuario(nome_correto, email, senha)
                    usuarios_cadastrados.append(usuario)
                    with open('usuarios.pickle', 'wb') as a_usuarios:
                        pickle.dump(usuarios_cadastrados, a_usuarios)
                    enviar_usuario(socket_cliente, usuario)
                    guardar_usuario(usuario)
        # Adicionar Valor na Careira
        elif menu == 3:
            valor = socket_cliente.receber_float()
            resposta = usuario.get_carteira().adicionar(valor)
            socket_cliente.enviar(resposta)
            enviar_usuario(socket_cliente, usuario)
        # Adicionar Item no Carrinho
        elif menu == 4:
            id_produto = socket_cliente.receber_inteiro()
            quantidade = socket_cliente.receber_inteiro()
            if quantidade > 0:
                item = Item(produtos[id_produto], quantidade)
                usuario.get_compra().add_item(item)
                enviar_usuario(socket_cliente, usuario)
                resposta = 'Item Adicionado ao Carrinho com Sucesso!'
                socket_cliente.enviar(resposta)
            else:
                resposta = 'Quantidade Inválida!'
                socket_cliente.enviar(resposta)
        # Finalizar Compra
        elif menu == 5:
            if usuario.get_compra().get_valor_compra() > 0:
                resposta = usuario.get_carteira().pagar(usuario.get_compra().get_valor_compra())
                socket_cliente.enviar(resposta)
                if resposta == 'Pagamento Aprovado.\nCompra Bem Sucedida!':
                    usuario.fechar_compra()
                    enviar_usuario(socket_cliente, usuario)
            else:
                resposta = 'Compra Vazia!'
                socket_cliente.enviar(resposta)
        # Remover Item do Carrinho
        elif menu == 6:
            id_lista = socket_cliente.receber_inteiro()
            if id_lista == -1 or id_lista > usuario.get_compra().tamanho_lista():
                resposta = 'Id Inválido!'
                socket_cliente.enviar(resposta)
            else:
                usuario.get_compra().remover_item(id_lista - 1)
                enviar_usuario(socket_cliente, usuario)
                resposta = 'Item Removido.'
                socket_cliente.enviar(resposta)
        # Sair
        elif menu == 9:
            salvar_usuario(usuario)
            resposta = "Obrigado por Comprar na nossa Loja\n Compre Conosco Sempre que Puder!"
            socket_cliente.enviar(resposta)
        # Fechar Tela
        elif menu == 0:
            salvar_usuario(usuario)
            break
    # Finaliza a Conexão
    socket_cliente.fechar()


while True:
    # Estabelece uma Conexão
    socket_c, end = socket_servidor.aceitar_cliente()
    t = threading.Thread(target=aplicacao, args=(socket_c, end, usuario_inicial))
    t.start()
