from echo_socket import EchoSocket
from tkinter import *
from PIL import ImageTk, Image

# Criando o Socket do Cliente
socket_cliente = EchoSocket()

# Conectando o Cliente ao Servidor
socket_cliente.conectar_cliente_local()

# Tkinter
# Criando a Tela
tela = Tk()
tela.title('Gamer Store')
tela.geometry('800x450+283+154')
tela.resizable(False, False)
tela.iconbitmap('imagens/logo.ico')
tela['bg'] = '#0061bc'

# Criando Frames
inicio = Frame(tela).pack()
cadastro = Frame(tela)

"""for frame in (inicio, cadastro):
    frame.grid(row=0,column=0,sticky="nsew")"""

# Criando alguns objetos
cor_fundo = '#0061bc'
cor_laranja = '#ff9900'
cor_azul = '#005e80'
usuario = Entry(inicio, bg='white', font='Montserrat 15', bd=2, relief='solid')
senha = Entry(inicio, bg='white', font='Montserrat 15', bd=2, relief='solid')

# Carregando as Imagens para a Lista
imagens = [ImageTk.PhotoImage(Image.open('imagens/logo.png'))]

# Funções do Programa


def troca_frame(frame):
    frame.tkraise()


def enviar_login(opcao):  # Função de Enviar o Login
    socket_cliente.enviar(opcao)
    if bool(usuario.get()):
        socket_cliente.enviar(usuario.get().strip())
    else:
        socket_cliente.enviar(' ')
    if bool(senha.get()):
        socket_cliente.enviar(senha.get().strip())
    else:
        socket_cliente.enviar(' ')
    resposta = socket_cliente.receber_decodificado()
    Label(inicio, text=resposta, bg=cor_fundo, font='Verdana 11 italic', width=33, height=2, padx=2).place(x=45, y=275)


def tela_inicial(): # Tela Inicial
    Label(inicio, text='Gamer Store', bg=cor_laranja, font='Impact 20 bold', bd=10, relief='raised', width=20, padx=4)\
        .place(x=45, y=100)
    Label(inicio, text='Email: ', bg=cor_azul, font='Montserrat 15', bd=2, relief='solid', width=7).place(x=45, y=170)
    Label(inicio, text='Senha: ', bg=cor_azul, font='Montserrat 15', bd=2, relief='solid', width=7).place(x=45, y=198)
    usuario.place(x=125, y=170)
    senha.place(x=125, y=198)
    Button(inicio, text='Entrar', bg=cor_azul, font='Montserrat 15 bold', width=24, padx=5, command=lambda:
    enviar_login('1')).place(x=45, y=230)
    Label(inicio, image=imagens[0], width=400, height=451, bg='white', bd=5, relief='solid').place(x=400, y=-5)
    Button(inicio, text='Cadastrar', bg=cor_azul, font='Montserrat 11 bold', command=lambda: troca_frame(cadastro))\
        .place(x=155, y=330)

def tela_cadastro():# Função da Tela de Cadastro
    Label(cadastro, text='OIIIIEee', bg=cor_laranja, font='Impact 20 bold', bd=10, relief='raised', width=20, padx=4)\
        .place(x=45, y=100)
# Começo do Programa

tela_inicial()
tela.mainloop()
