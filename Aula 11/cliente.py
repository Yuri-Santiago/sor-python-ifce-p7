"""
Implementar uma aplicação utilizando a arquitetura do Echo Server
Clássico utilizando a classe Carros, proposta na aula de 19/04. A
aplicação Cliente deve passar os dados para o servidor e executar
os métodos da classe. A aplicação deve ser um simulador de
consumo. Por exemplo, deve ser informado o consumo do veículo,
a quantidade de combustível abastecida, a distância que se
pretende percorrer e quanto restará no tanque após percorrer a
distância.
"""
import socket
# Criando o Socket do Cliente
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Definindo o endereço do Servidor para o Cliente conectar
host = '127.0.0.1'
port = 8080
# Conectando o Cliente ao Servidor
socket_cliente.connect((host, port))
# Programa Funcionando
print('Nesse programa você poderá simular uma viagem')

km = input('Primeiro digite quantos quilômetros por litro seu carro faz: ')
socket_cliente.send(km.encode('utf-8'))

litro = input('Agora digite quantos litros seu carro possui atualmente: ')
socket_cliente.send(litro.encode('utf-8'))

opc = 0
while int(opc) != 4:
    print("\nDigite o número da opção que você deseja: \nOpção 1 - Dirigir com o Carro \nOpção 2 - Verificar "
          "Combustível no Tanque \nOpção 3 - Abastecer o Tanque \nOpção 4 - Fechar o Programa")
    opc = input('Opção Escolhida: ')
    socket_cliente.send(opc.encode('utf-8'))
    if int(opc) == 1:
        km_andado = input('Digite quantos quilômetros você quer andar: ')
        socket_cliente.send(km_andado.encode('utf-8'))
        resposta = socket_cliente.recv(1024)
        print(resposta.decode('utf-8'))
    elif int(opc) == 2:
        resposta = socket_cliente.recv(1024)
        print(resposta.decode('utf-8'))
    elif int(opc) == 3:
        litros = input('Digite quantos litros você quer abastecer: ')
        socket_cliente.send(litros.encode('utf-8'))
        resposta = socket_cliente.recv(1024)
        print(resposta.decode('utf-8'))
    elif int(opc) == 4:
        print("Obrigado por usar o Programa, até a próxima!")
    else:
        print('Digite uma Opção Válida')

socket_cliente.close()
