from echo_socket import EchoSocket
from tkinter import *
from PIL import ImageTk, Image
import pickle
from tkinter import messagebox
import time
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
inicio = Frame(tela).pack(side=TOP)
loja = Frame(tela).pack(side=BOTTOM)

# Criando Objetos
# Carregando as Imagens para a Lista
imagem = [ImageTk.PhotoImage(Image.open('imagens/logo.png')), ImageTk.PhotoImage(Image.open('imagens/mouse.png')),
          ImageTk.PhotoImage(Image.open('imagens/teclado.png')), ImageTk.PhotoImage(Image.open('imagens/headset.png')),
          ImageTk.PhotoImage(Image.open('imagens/monitor.png')), ImageTk.PhotoImage(Image.open('imagens/playstation.png')),
          ImageTk.PhotoImage(Image.open('imagens/notebook.png')), ImageTk.PhotoImage(Image.open('imagens/cadeira.png')),
          ImageTk.PhotoImage(Image.open('imagens/celular.png')), ImageTk.PhotoImage(Image.open('imagens/controle.png')),
          ImageTk.PhotoImage(Image.open('imagens/xbox.png')), ImageTk.PhotoImage(Image.open('imagens/loginho.png')),
          ImageTk.PhotoImage(Image.open('imagens/usuario.png')), ImageTk.PhotoImage(Image.open('imagens/carrinho.png'))]

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
logo_imagem = Label(inicio, image=imagem[0], width=400, height=451, bg='white', bd=5, relief='solid')
nome_label = Label(inicio, text='Nome: ', bg=cor_azul, font='Montserrat 15', bd=2, relief='solid', width=7)

# Entrys
email_entry = Entry(inicio, bg='white', font='Montserrat 15', bd=2, relief='solid')
senha_entry = Entry(inicio, bg='white', font='Montserrat 15', bd=2, relief='solid')
nome_entry = Entry(inicio, bg='white', font='Montserrat 15', bd=2, relief='solid')
# Buttons
entrar = Button(inicio, text='Entrar', bg=cor_azul, font='Montserrat 15 bold', width=24, padx=5,
                command=lambda: enviar_login('1'))
cadastrar = Button(inicio, text='Cadastrar', bg=cor_azul, font='Montserrat 11 bold', command=lambda: tela_cadastro())

# Segunda Tela
# Buttons
botao = [Button(loja, image = imagem[x], bg='white', bd=4, relief='solid') for x in range(1,11)]

# Labels
logo_loja = Label(loja, image=imagem[11], bg=cor_fundo)
gamer_loja = Label(loja, text='Gamer Store', bg=cor_laranja, font='Impact 16 bold', bd=10, relief='raised', width=15)
usuario_butao = Button(loja, image=imagem[12], bg='white', bd=4, relief='solid')
usuario_label = Label(loja, bg=cor_azul, font='Montserrat 16 bold', width=12)
carteira_label = Label(loja, bg=cor_azul, font='Montserrat 16 bold', width=12)
carrinho_butao = Button(loja, image=imagem[13], bg='white', bd=4, relief='solid')
carrinho_label = Label(loja, bg=cor_fundo, font='Montserrat 16 bold')
carinho_finalizar = Label(loja, text='Finalizar', bg=cor_fundo, font='Montserrat 16 bold')
# Recebendo todos os Nomes Pelo Servidor
textos_recebidos = socket_cliente.receber_bytes()
textos_produtos = pickle.loads(textos_recebidos)
produto = [Label(loja, text=t, bg=cor_fundo, font='Montserrat 12 bold') for t in textos_produtos]

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
    if resposta == 'Bem vindo':
        tela_loja()



def enviar_cadastro(opcao):
    socket_cliente.enviar(opcao)
    enviar_dado(nome_entry)
    enviar_dado(email_entry)
    enviar_dado(senha_entry)
    resposta = socket_cliente.receber_decodificado()
    resposta_label['text'] = resposta
    resposta_label.place(x=450, y=275)
    if resposta == 'Conta criada':
        tela_loja()


def tela_inicial():  # Tela Inicial
    # Movendo coisas pra longe
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
    # Movendo coisas pra longe
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


def tela_loja():
    # Recebendo o Usuario
    usuario_byte = socket_cliente.receber_bytes()
    usuario = pickle.loads(usuario_byte)
    # Movendo coisas pra longe
    nome_entry.place(x=1000, y=1000)
    nome_label.place(x=1000, y=1000)
    resposta_label.place(x=1000, y=1000)
    nome_loja.place(x=1000, y=1000)
    email_label.place(x=1000, y=1000)
    senha_label.place(x=1000, y=1000)
    email_entry.place(x=1000, y=1000)
    senha_entry.place(x=1000, y=1000)
    entrar.place(x=1000, y=1000)
    logo_imagem.place(x=1000, y=1000)
    cadastrar.place(x=1000, y=1000)

    # Tela
    botao[0].place(x=26, y=100)
    botao[1].place(x=180, y=100)
    botao[2].place(x=336, y=100)
    botao[3].place(x=490, y=100)
    botao[4].place(x=644, y=100)
    botao[5].place(x=26, y=275)
    botao[6].place(x=180, y=275)
    botao[7].place(x=336, y=275)
    botao[8].place(x=490, y=275)
    botao[9].place(x=644, y=275)
    produto[0].place(x=40, y=240)
    produto[1].place(x=190, y=240)
    produto[2].place(x=344, y=240)
    produto[3].place(x=502, y=240)
    produto[4].place(x=660, y=240)
    produto[5].place(x=28, y=415)
    produto[6].place(x=191, y=415)
    produto[7].place(x=349, y=415)
    produto[8].place(x=497, y=415)
    produto[9].place(x=658, y=415)

    logo_loja.place(x=26, y=3)
    gamer_loja.place(x=110, y=17)
    usuario_butao.place(x=700, y=3)
    usuario_label['text'] = usuario.get_nome().split()[0]
    usuario_label.place(x=530, y=17)
    carteira_label['text'] = '%.2f R$' % usuario.get_carteira().get_total()
    carteira_label.place(x=530, y=47)
    carrinho_butao.place(x=315, y=3)
    carrinho_label['text'] = '%.2f R$' % usuario.get_compra().get_valor_compra()
    carrinho_label.place(x=400, y=47)
    carinho_finalizar.place(x=400, y=17)
# Começo do Programa
tela_inicial()
tela.mainloop()
"""def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        tela.destroy()

tela.protocol("WM_DELETE_WINDOW", on_closing)"""
