import socket

# Criando o Socket do Cliente
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definindo o endereço do Servidor para o Cliente conectar
host = '127.0.0.1'
port = 8080

# Conectando o Cliente ao Servidor
socket_cliente.connect((host, port))

# Programa Funcionando
print('### Bem Vindo a Loja Online Gamer ###\nCompre seus produtos no preço mais acessível aqui!')

# Parte da Verificação do Usuário
menu = 0
while True:
    print('Você deve criar uma Conta ou Fazer Login na sua conta primeiro.\nOpção 1 - Criar a Conta.\nOpção 2 - Fazer '
          'Login.\nOpção 3 - Sair da Loja.')
    menu = input('Opção Escolhida: ')
    socket_cliente.send(menu.encode('utf-8'))

    # Criando Conta do Usuário
    if int(menu) == 1:
        nome = input('Digite seu Nome Completo: ')
        socket_cliente.send(nome.encode('utf-8'))
        email = input('Digite seu Email para Login: ')
        socket_cliente.send(email.encode('utf-8'))
        senha = input('Digite sua Senha para Login: ')
        socket_cliente.send(senha.encode('utf-8'))
        resposta = socket_cliente.recv(1024)
        print(resposta.decode('utf-8'))
        break
    # Fazendo Login em uma Conta Existente
    elif int(menu) == 2:
        email = input('Digite seu Email para Login: ')
        socket_cliente.send(email.encode('utf-8'))
        senha = input('Digite sua Senha para Login: ')
        socket_cliente.send(senha.encode('utf-8'))
        break

    # Saindo do Menu
    elif int(menu) == 3:
        print("Obrigado por entrar na Loja, Compre quando Quiser!")
    else:
        print('Digite uma Opção Válida, Por Favor.')

# Dentro da Loja
opc = 0
while int(opc) != 7:

    print("\nDigite o número da opção que você desejar: \nOpção 1 - Mostrar os Produtos da loja \nOpção 2 - Adicionar "
          "Produto no Carrinho \nOpção 3 - Listar os Itens do Carrinho \nOpção 4 - Finalizar a Compra \nOpção 5 - "
          "Adicionar dinheiro na Carteira \nOpção 6 - Dinheiro total na Carteira \nOpção 7 - Deslogar")
    opc = input('Opção Escolhida: ')
    socket_cliente.send(opc.encode('utf-8'))

    # Mostrar os Produtos da loja
    if int(opc) == 1:
        resposta = socket_cliente.recv(1024)
        print(resposta.decode('utf-8'))
        input('Aperte Enter para Continuar.')

    # Adicionar Produto no Carrinho
    elif int(opc) == 2:
        id_produto = input('Digite o Número de Identificação (ID) do Produto: ')
        socket_cliente.send(id_produto.encode('utf-8'))
        quantidade = input('Digite a Quantidade do Produtos que Deseja Comprar: ')
        socket_cliente.send(quantidade.encode('utf-8'))
        resposta = socket_cliente.recv(1024)
        print(resposta.decode('utf-8'))

    # Listar os Itens do Carrinho
    elif int(opc) == 3:
        resposta = socket_cliente.recv(1024)
        print(resposta.decode('utf-8'))

    # Finalizar a Compra
    elif int(opc) == 4:
        resposta = socket_cliente.recv(1024)
        print(resposta.decode('utf-8'))

    # Adicionar dinheiro na Carteira
    elif int(opc) == 5:
        valor = input('Digite qual Valor você quer Adicionar na Carteira: ')
        socket_cliente.send(valor.encode('utf-8'))
        resposta = socket_cliente.recv(1024)
        print(resposta.decode('utf-8'))

    # Dinheiro total na Carteira
    elif int(opc) == 6:
        resposta = socket_cliente.recv(1024)
        print(resposta.decode('utf-8'))

    # Deslogar
    elif int(opc) == 7:
        print("Obrigado por Comprar na nossa Loja, Compre Conosco Sempre que Puder!")
    else:
        print('Digite uma Opção Válida, Por Favor.')

socket_cliente.close()
