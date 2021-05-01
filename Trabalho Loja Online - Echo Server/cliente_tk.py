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

# Criando Objetos
# Carregando as Imagens para a Lista
imagens = [ImageTk.PhotoImage(Image.open('imagens/logo.png'))]

# Cores
cor_fundo = '#0061bc'
cor_laranja = '#ff9900'
cor_azul = '#005e80'

# Primeira Tela
# Labels
nome_loja = Label(inicio, text='Gamer Store', bg=cor_laranja, font='Impact 20 bold', bd=10, relief='raised', width=20,
                  padx=4)
email_label = Label(inicio, text='Email: ', bg=cor_azul, font='Montserrat 15', bd=2, relief='solid', width=7)
senha_label = Label(inicio, text='Senha: ', bg=cor_azul, font='Montserrat 15', bd=2, relief='solid', width=7)
resposta_label = Label(inicio, bg=cor_fundo, font='Verdana 11 italic', width=33, height=2, padx=2)
logo_imagem = Label(inicio, image=imagens[0], width=400, height=451, bg='white', bd=5, relief='solid')
nome_label = Label(inicio, text='Nome: ', bg=cor_azul, font='Montserrat 15', bd=2, relief='solid', width=7)

# Entrys
email_entry = Entry(inicio, bg='white', font='Montserrat 15', bd=2, relief='solid')
senha_entry = Entry(inicio, bg='white', font='Montserrat 15', bd=2, relief='solid')
nome_entry = Entry(inicio, bg='white', font='Montserrat 15', bd=2, relief='solid')
# Buttons
entrar = Button(inicio, text='Entrar', bg=cor_azul, font='Montserrat 15 bold', width=24, padx=5,
                command=lambda: enviar_login('1'))
cadastrar = Button(inicio, text='Cadastrar', bg=cor_azul, font='Montserrat 11 bold', command=lambda: tela_cadastro())


# Funções do Programa
def enviar_dado(dado):
    if bool(dado.get()):
        socket_cliente.enviar(dado.get().strip())
    else:
        socket_cliente.enviar(' ')


def enviar_login(opcao):  # Função de Enviar o Login
    socket_cliente.enviar(opcao)
    enviar_dado(email_entry)
    enviar_dado(senha_entry)
    resposta = socket_cliente.receber_decodificado()
    resposta_label['text'] = resposta
    resposta_label.place(x=45, y=275)


def enviar_cadastro(opcao):
    socket_cliente.enviar(opcao)
    enviar_dado(nome_entry)
    enviar_dado(email_entry)
    enviar_dado(senha_entry)
    resposta = socket_cliente.receber_decodificado()
    resposta_label['text'] = resposta
    resposta_label.place(x=450, y=275)


def tela_inicial():  # Tela Inicial
    nome_entry.place(x=1000, y=1000)
    nome_label.place(x=1000, y=1000)
    resposta_label.place(x=1000, y=1000)
    nome_loja.place(x=45, y=100)
    email_label.place(x=45, y=170)
    senha_label.place(x=45, y=198)
    email_entry.delete(0, END)
    email_entry.place(x=125, y=170)
    senha_entry.delete(0, END)
    senha_entry.place(x=125, y=198)
    entrar['text'] = 'Entrar'
    entrar['command'] = lambda: enviar_login('1')
    entrar.place(x=45, y=230)
    logo_imagem.place(x=400, y=-5)
    cadastrar['text'] = 'Cadastrar'
    cadastrar['command'] = lambda: tela_cadastro()
    cadastrar.place(x=155, y=330)


def tela_cadastro():  # Função da Tela de Cadastro
    resposta_label.place(x=1000, y=1000)
    logo_imagem.place(x=-4, y=-5)
    nome_loja.place(x=450, y=72)
    nome_label.place(x=450, y=142)
    email_label.place(x=450, y=170)
    senha_label.place(x=450, y=198)
    nome_entry.delete(0, END)
    nome_entry.place(x=530, y=142)
    email_entry.delete(0, END)
    email_entry.place(x=530, y=170)
    senha_entry.delete(0, END)
    senha_entry.place(x=530, y=198)
    entrar['text'] = 'Cadastrar'
    entrar['command'] = lambda: enviar_cadastro('2')
    entrar.place(x=450, y=230)
    cadastrar['text'] = 'Voltar'
    cadastrar.place(x=580, y=330)
    cadastrar['command'] = lambda: tela_inicial()


# Começo do Programa
tela_inicial()
tela.mainloop()
