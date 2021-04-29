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

        # Criando Conta do Usuário
        if menu == 1:
            nome = socket_cliente.receber_decodificado()
            # Verificar se o Email já é existente
            while True:
                email = socket_cliente.receber_decodificado()
                emails = [u.get_email() for u in usuarios]  # Lista com os emails listados
                if email in emails:
                    resposta = 'Email já Cadastrado. Por Favor, Tente Novamente.'
                    socket_cliente.enviar(resposta)
                else:
                    resposta = 'Email Válido!'
                    socket_cliente.enviar(resposta)
                    break
            senha = socket_cliente.receber_decodificado()
            usuario = Usuario(nome, email, senha)
            resposta = f'Conta Criada com Sucesso! \nBem vindo(a) {nome.split()[0]}!'
            socket_cliente.enviar(resposta)

            usuarios.append(usuario)
            with open('usuarios.pickle', 'wb') as arquivo_usuarios:
                pickle.dump(usuarios, arquivo_usuarios)
            break

        # Fazer Login
        elif menu == 2:
            validacao = 0
            while True:
                email = socket_cliente.receber_decodificado()
                for u in usuarios:
                    if email == u.get_email():  # Verificar se o Email está Cadastrado
                        resposta = 'Email Válido!'
                        socket_cliente.enviar(resposta)

                        while True:
                            senha = socket_cliente.receber_decodificado()
                            if senha == u.get_senha():  # Verificar se a Senha está Correta
                                resposta = f'Bem vindo(a) {u.get_nome().split()[0]}!'
                                socket_cliente.enviar(resposta)
                                usuario = u
                                validacao = 1
                                break
                            else:  # Senha Errada
                                resposta = 'Senha Incorreta, Tente Novamente.'
                                socket_cliente.enviar(resposta)
                        break
                if validacao == 1:
                    break
                else:  # Email não Cadastrado
                    resposta = 'Email Não Cadastrado, se Cadastre ou Tente Novamente.'
                    socket_cliente.enviar(resposta)
            break

        # Sair
        elif menu == 0:
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
            if resposta == 'Pagamento Aprovado.\nCompra Bem Sucedida!':
                usuario.fechar_compra()

        # Adicionar dinheiro na Carteira
        elif opc == 5:
            valor = socket_cliente.receber_inteiro()
            resposta = usuario.get_carteira().adicionar(valor)
            socket_cliente.enviar(resposta)

        # Dinheiro total na Carteira
        elif opc == 6:
            resposta = 'Você possui na Carteira: %.2fR$' % usuario.get_carteira().get_total()
            socket_cliente.enviar(resposta)

        # Sair do Programa e Armazenar os Dados atuais do Usuário no Sistema
        elif opc == 0:
            with open('usuarios.pickle', 'rb') as arquivo_usuarios:
                usuarios_final = pickle.load(arquivo_usuarios)

            for u in usuarios_final:
                if usuario.get_email() == u.get_email():
                    usuarios_final[usuarios_final.index(u)] = usuario

            with open('usuarios.pickle', 'wb') as arquivo_usuarios:
                pickle.dump(usuarios_final, arquivo_usuarios)

            resposta = "Obrigado por Comprar na nossa Loja, Compre Conosco Sempre que Puder!"
            socket_cliente.enviar(resposta)
            break

    # Finaliza a Conexão
    socket_cliente.fechar()
    socket_servidor.fechar()
