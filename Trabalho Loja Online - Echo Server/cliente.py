from echo_socket import EchoSocket

# Criando o Socket do Cliente
socket_cliente = EchoSocket()

# Conectando o Cliente ao Servidor
socket_cliente.conectar_cliente_local()

# Programa Funcionando
print('### Bem Vindo a Loja Online Gamer ###\nCompre seus produtos no preço mais acessível aqui!')

# Parte da Verificação do Usuário
menu = -1
while True:
    print('Você deve criar uma Conta ou Fazer Login na sua conta primeiro.\nOpção 1 - Criar a Conta.\nOpção 2 - Fazer '
          'Login.\nOpção 0 - Sair da Loja.')
    menu = input('Opção Escolhida: ')
    socket_cliente.enviar(menu)

    # Criando Conta do Usuário
    if int(menu) == 1:
        nome = input('Digite seu Nome Completo para Criar sua Conta: ')
        socket_cliente.enviar(nome)
        while True:
            email = input('Digite seu Email para Criar sua Conta: ')
            socket_cliente.enviar(email)
            resposta = socket_cliente.receber_decodificado()
            print(resposta)
            if resposta == 'Email Válido!':
                break
        senha = input('Digite sua Senha para Criar sua Conta: ')
        socket_cliente.enviar(senha)
        resposta = socket_cliente.receber_decodificado()
        print(resposta)
        break

    # Fazendo Login em uma Conta Existente
    elif int(menu) == 2:
        validacao = 0
        while True:
            email = input('Digite seu Email para Login: ')
            socket_cliente.enviar(email)
            resposta = socket_cliente.receber_decodificado()
            print(resposta)

            if resposta == 'Email Válido!':
                while True:
                    senha = input('Digite sua Senha para Login: ')
                    socket_cliente.enviar(senha)
                    resposta = socket_cliente.receber_decodificado()
                    print(resposta)

                    if resposta != 'Senha Incorreta, Tente Novamente.':
                        validacao = 1
                        break
            if validacao == 1:
                break
        break

    # Saindo do Menu
    elif int(menu) == 0:
        print("Obrigado por entrar na Loja, Compre quando Quiser!")
    else:
        print('Digite uma Opção Válida, Por Favor.')

# Dentro da Loja
opc = -1
while int(opc) != 0:

    print("\nDigite o número da opção que você desejar: \nOpção 1 - Mostrar os Produtos da loja \nOpção 2 - Adicionar "
          "Produto no Carrinho \nOpção 3 - Listar os Itens do Carrinho \nOpção 4 - Finalizar a Compra \nOpção 5 - "
          "Adicionar dinheiro na Carteira \nOpção 6 - Dinheiro total na Carteira \nOpção 0 - Deslogar")
    opc = input('Opção Escolhida: ')
    socket_cliente.enviar(opc)

    # Mostrar os Produtos da loja
    if int(opc) == 1:
        resposta = socket_cliente.receber_decodificado()
        print(resposta)
        input('Aperte Enter para Continuar.')

    # Adicionar Produto no Carrinho
    elif int(opc) == 2:
        id_produto = input('Digite o Número de Identificação (ID) do Produto: ')
        socket_cliente.enviar(id_produto)
        quantidade = input('Digite a Quantidade do Produtos que Deseja Comprar: ')
        socket_cliente.enviar(quantidade)
        resposta = socket_cliente.receber_decodificado()
        print(resposta)

    # Listar os Itens do Carrinho
    elif int(opc) == 3:
        resposta = socket_cliente.receber_decodificado()
        print(resposta)

    # Finalizar a Compra
    elif int(opc) == 4:
        resposta = socket_cliente.receber_decodificado()
        print(resposta)

    # Adicionar dinheiro na Carteira
    elif int(opc) == 5:
        valor = input('Digite qual Valor você quer Adicionar na Carteira: ')
        socket_cliente.enviar(valor)
        resposta = socket_cliente.receber_decodificado()
        print(resposta)

    # Dinheiro total na Carteira
    elif int(opc) == 6:
        resposta = socket_cliente.receber_decodificado()
        print(resposta)

    # Sair do Programa e Armazenar os Dados atuais do Usuário no Sistema
    elif int(opc) == 0:
        resposta = socket_cliente.receber_decodificado()
        print(resposta)
    else:
        print('Digite uma Opção Válida, Por Favor.')

socket_cliente.fechar()
