from produto import Produto
from item import Item
from usuario import Usuario
import socket

# Criando o Socket do Servidor
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definindo o endereço do Servidor
host = '127.0.0.1'
port = 8080

# Conectando o socket com a porta
socket_servidor.bind((host, port))

# Socket começa a escutar solicitações
socket_servidor.listen()

# Funções do Servidor
# Salvando os Produtos da Loja e os Usuários
with open('produtos.txt', 'r') as arquivo_produtos:
    linhas = arquivo_produtos.readlines()
produtos = [Produto(p.split('-')[0], float(p.split('-')[1])) for p in linhas]

with open('usuarios.txt', 'r') as arquivo_usuarios:
    usuarios_cadastrados = arquivo_usuarios.readlines()
logins = {u.split('-')[1]: u.split('-')[2] for u in usuarios_cadastrados}

# Começo das conexão
while True:
    # Estabelece uma Conexão
    socket_cliente, endereco = socket_servidor.accept()
    print("Conexão Estabelecida com: %s" % str(endereco))

    # Programa Funcionando

    # Criando o Usuário
    while True:
        menu = int(socket_cliente.recv(1024))

        # Criando Conta do Usuário
        if menu == 1:
            nome = socket_cliente.recv(1024).decode('utf-8')
            email = socket_cliente.recv(1024).decode('utf-8')
            senha = socket_cliente.recv(1024).decode('utf-8')
            usuario = Usuario(nome, email, senha)
            resposta = 'Conta Criada com Sucesso!'
            socket_cliente.send(resposta.encode('utf-8'))

            with open('usuarios.txt', 'a') as arquivo_usuarios:
                arquivo_usuarios.write(f'\n{nome}-{email}-{senha}-')
            break

        # Fazer Login
        elif menu == 2:
            while True:
                # TODO
                email = socket_cliente.recv(1024).decode('utf-8')
                senha = socket_cliente.recv(1024).decode('utf-8')
                if email in logins.keys():
                    if senha == logins[email]:
                        resposta = 'Bem vindo!'
                        socket_cliente.send(resposta.encode('utf-8'))
                else:
                    resposta = 'Email Não Cadastrado'
                    socket_cliente.send(resposta.encode('utf-8'))
            break
        # Sair
        elif menu == 3:
            socket_cliente.close()
            socket_servidor.close()
            break

    # Dentro da Loja
    while True:
        opc = int(socket_cliente.recv(1024))

        # Mostrar os Produtos da Loja
        if opc == 1:
            resposta = '\nProdutos da Loja: \n'
            for i, produto in enumerate(produtos):
                resposta += 'ID: %d - Produto: %s - Preço: %.2fR$\n' % \
                           (i, produto.get_nome(), produto.get_preco())
            socket_cliente.send(resposta.encode('utf-8'))

        # Adicionar Produto no Carrinho
        elif opc == 2:
            id_produto = int(socket_cliente.recv(1024))
            quantidade = int(socket_cliente.recv(1024))
            item = Item(produtos[id_produto], quantidade)
            usuario.get_compra().add_item(item)
            resposta = 'Item Adicionado ao Carrinho com Sucesso!'
            socket_cliente.send(resposta.encode('utf-8'))

        # Listar os Itens do Carrinho
        elif opc == 3:
            resposta = '\nLista de Itens do Carrinho:\n'
            resposta += usuario.get_compra().listar_itens()
            resposta += 'O Valor Total o Carrinho é: %.2fR$' % (usuario.get_compra().get_valor_compra())
            socket_cliente.send(resposta.encode('utf-8'))

        # Finalizar a Compra
        elif opc == 4:
            resposta = usuario.get_carteira().pagar(usuario.get_compra().get_valor_compra())
            socket_cliente.send(resposta.encode('utf-8'))

        # Adicionar dinheiro na Carteira
        elif opc == 5:
            valor = int(socket_cliente.recv(1024))
            resposta = usuario.get_carteira().adicionar(valor)
            socket_cliente.send(resposta.encode('utf-8'))

        # Dinheiro total na Carteira
        elif opc == 6:
            resposta = 'Você possui na Carteira: %.2fR$' % usuario.get_carteira().get_total()
            socket_cliente.send(resposta.encode('utf-8'))

        # Sair
        elif opc == 7:
            with open('usuarios.txt', 'a') as arquivo_usuarios:
                arquivo_usuarios.write(str(usuario.get_carteira().get_total()))
            break

    # Finaliza a Conexão
    socket_cliente.close()
    socket_servidor.close()
