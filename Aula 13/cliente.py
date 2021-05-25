import socket

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8080

socket_cliente.connect((host, port))

print("Programa que Calcula o seu IMC")
peso = input("Digite o seu Peso em kilos: ")
socket_cliente.send(peso.encode())
altura = input("Digite sua Altura em metros: ")
socket_cliente.send(altura.encode())
total = float(socket_cliente.recv(2048).decode())
print("O seu IMC é: %.2f" % total)
