import socket


class EchoSocket:
    def __init__(self, socket_inicio=socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
        self.socket = socket_inicio

    def conectar_servidor_local(self):
        self.socket.bind(('127.0.0.1', 8080))

    def conectar_cliente_local(self):
        self.socket.connect(('127.0.0.1', 8080))

    def escutar_atomico(self):
        self.conectar_servidor_local()
        self.socket.listen()

    def aceitar_cliente(self):
        socket_cliente, endereco = self.socket.accept()
        return EchoSocket(socket_cliente), endereco

    def receber_inteiro(self):
        return int(self.socket.recv(1024))

    def receber_decodificado(self):
        return self.socket.recv(1024).decode('utf-8')

    def receber_bytes(self):
        return self.socket.recv(1024)

    def enviar(self, pacote):
        self.socket.send(pacote.encode('utf-8'))

    def enviar_bytes(self, pacote):
        self.socket.send(pacote)
    def fechar(self):
        self.socket.close()
