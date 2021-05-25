import socket
import threading


def aplicacao(socket_cliente, endereco):
    print("Conexão recebida de %s" % str(endereco))

    peso = float(socket_cliente.recv(2048).decode())
    altura = float(socket_cliente.recv(2048).decode())
    total = peso / (altura ** 2)
    socket_cliente.send(str(total).encode())
    socket_cliente.close()


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8080
ss.bind((host, port))
ss.listen()
print("Servidor ativo na porta %s.\n\r" % port)

while True:
    socket_c, edrc = ss.accept()
    t = threading.Thread(target=aplicacao, args=(socket_c, edrc))
    t.start()
