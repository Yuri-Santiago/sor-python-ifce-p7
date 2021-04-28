from produto import Produto
from item import Item
from usuario import Usuario
from echo_socket import EchoSocket

# Criando o Socket do Servidor
socket_servidor = EchoSocket()

# Socket começa a escutar solicitações
socket_servidor.escutar_atomico()

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
    socket_cliente, endereco = socket_servidor.aceitar_cliente()
    print("Conexão Estabelecida com: %s" % str(endereco))

    # Criando o Usuário
    while True:
        menu = socket_cliente.receber_inteiro()

        # Criando Conta do Usuário
        if menu == 1:
            nome = socket_cliente.receber_decodificado()
            email = socket_cliente.receber_decodificado()
            senha = socket_cliente.receber_decodificado()
            usuario = Usuario(nome, email, senha)
            resposta = 'Conta Criada com Sucesso!'
            socket_cliente.enviar(resposta)

            with open('usuarios.txt', 'a') as arquivo_usuarios:
                arquivo_usuarios.write(f'\n{nome}-{email}-{senha}-')
            break

        # Fazer Login
        elif menu == 2:
            while True:
                # TODO
                email = socket_cliente.receber_decodificado()
                senha = socket_cliente.receber_decodificado()
                if email in logins.keys():
                    if senha == logins[email]:
                        resposta = 'Bem vindo!'
                        socket_cliente.enviar(resposta)
                else:
                    resposta = 'Email Não Cadastrado'
                    socket_cliente.enviar(resposta)
            break
        # Sair
        elif menu == 3:
            socket_cliente.fechar()
            socket_servidor.fechar()
            break

    # Dentro da Loja
    while True:
        opc = socket_cliente.receber_inteiro()

        # Mostrar os Produtos da Loja
        if opc == 1:
            resposta = '\nProdutos da Loja: \n'
            for i, produto in enumerate(produtos):
                resposta += 'ID: %d - Produto: %s - Preço: %.2fR$\n' % \
                           (i, produto.get_nome(), produto.get_preco())
            socket_cliente.enviar(resposta)

        # Adicionar Produto no Carrinho
        elif opc == 2:
            id_produto = socket_cliente.receber_inteiro()
            quantidade = socket_cliente.receber_inteiro()

            item = Item(produtos[id_produto], quantidade)
            usuario.get_compra().add_item(item)

            resposta = 'Item Adicionado ao Carrinho com Sucesso!'
            socket_cliente.enviar(resposta)

        # Listar os Itens do Carrinho
        elif opc == 3:
            resposta = '\nLista de Itens do Carrinho:\n'
            resposta += usuario.get_compra().listar_itens()
            resposta += 'O Valor Total o Carrinho é: %.2fR$' % (usuario.get_compra().get_valor_compra())
            socket_cliente.enviar(resposta)

        # Finalizar a Compra
        elif opc == 4:
            resposta = usuario.get_carteira().pagar(usuario.get_compra().get_valor_compra())
            socket_cliente.enviar(resposta)

        # Adicionar dinheiro na Carteira
        elif opc == 5:
            valor = socket_cliente.receber_inteiro()
            resposta = usuario.get_carteira().adicionar(valor)
            socket_cliente.enviar(resposta)

        # Dinheiro total na Carteira
        elif opc == 6:
            resposta = 'Você possui na Carteira: %.2fR$' % usuario.get_carteira().get_total()
            socket_cliente.enviar(resposta)

        # Sair
        elif opc == 7:
            with open('usuarios.txt', 'a') as arquivo_usuarios:
                arquivo_usuarios.write(str(usuario.get_carteira().get_total()))
            break

    # Finaliza a Conexão
    socket_cliente.fechar()
    socket_servidor.fechar()
