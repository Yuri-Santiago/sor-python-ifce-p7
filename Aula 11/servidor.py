import socket
from carro import Carro
# Criando o Socket do Servidor
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Definindo o endereço do Servidor
host = '127.0.0.1'
port = 8080
# Conectando o socket com a porta
socket_servidor.bind((host, port))
# Socket começa a escutar solicitações
socket_servidor.listen()
while True:
    # Estabelece uma Conexão
    socket_cliente, endereco = socket_servidor.accept()
    print("Conexão Estabelecida com: %s" % str(endereco))

    km = float(socket_cliente.recv(1024))
    carro = Carro(km)

    litro = float(socket_cliente.recv(1024))
    carro.adicionar_gasolina(litro)

    while True:
        opc = int(socket_cliente.recv(1024))
        if opc == 1:
            km_andado = float(socket_cliente.recv(1024))
            resposta = carro.andar(km_andado)
            socket_cliente.send(resposta.encode('utf-8'))
        if opc == 2:
            resposta = f'Você possui %.2f litros de combustível no seu Tanque.' % carro.obter_gasolina()
            socket_cliente.send(resposta.encode('utf-8'))
        if opc == 3:
            litros = float(socket_cliente.recv(1024))
            resposta = carro.adicionar_gasolina(litros)
            socket_cliente.send(resposta.encode('utf-8'))
        if opc == 4:
            break

    socket_cliente.close()
    socket_servidor.close()