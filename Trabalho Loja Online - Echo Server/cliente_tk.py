from echo_socket import EchoSocket
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pickle

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
loja = Frame(tela).pack()
user = Frame(tela).pack()
compra = Frame(tela).pack()

carrinho = Frame(tela).pack()
# Criando Objetos
# Carregando as Imagens para a Lista
imagens_textos = ['imagens/mouse.png', 'imagens/teclado.png', 'imagens/headset.png', 'imagens/monitor.png',
                  'imagens/playstation.png', 'imagens/notebook.png', 'imagens/cadeira.png', 'imagens/celular.png',
                  'imagens/controle.png', 'imagens/xbox.png', 'imagens/logo.png', 'imagens/loginho.png',
                  'imagens/usuario.png', 'imagens/carrinho.png', 'imagens/casa.png', 'imagens/logoff.png',
                  'imagens/mouse_grande.png', 'imagens/teclado_grande.png', 'imagens/headset_grande.png',
                  'imagens/monitor_grande.png', 'imagens/playstation_grande.png', 'imagens/notebook_grande.png',
                  'imagens/cadeira_grande.png', 'imagens/celular_grande.png', 'imagens/controle_grande.png',
                  'imagens/xbox_grande.png']
imagem = [ImageTk.PhotoImage(Image.open(texto)) for texto in imagens_textos]

# Cores
cor_fundo = '#0061bc'
cor_laranja = '#ff6600'
cor_azul = '#005e80'

# Primeira Tela
# Labels
nome_loja = Label(inicio, text='Gamer Store', bg=cor_laranja, font='Impact 20 bold', bd=10, relief='raised', width=20,
                  padx=4)
email_label = Label(inicio, text='Email: ', bg=cor_azul, font='Montserrat 15', bd=2, relief='solid', width=7)
senha_label = Label(inicio, text='Senha: ', bg=cor_azul, font='Montserrat 15', bd=2, relief='solid', width=7)
resposta_label = Label(inicio, bg=cor_fundo, font='Verdana 11 italic', width=33, height=2, padx=2)
logo_imagem = Label(inicio, image=imagem[10], width=400, height=451, bg='white', bd=5, relief='solid')
nome_label = Label(inicio, text='Nome: ', bg=cor_azul, font='Montserrat 15', bd=2, relief='solid', width=7)

# Entrys
email_entry = Entry(inicio, bg='white', font='Montserrat 15', bd=2, relief='solid')
senha_entry = Entry(inicio, bg='white', font='Montserrat 15', bd=2, relief='solid', show='*')
nome_entry = Entry(inicio, bg='white', font='Montserrat 15', bd=2, relief='solid')
# Buttons
entrar = Button(inicio, text='Entrar', bg=cor_azul, font='Montserrat 15 bold', width=24, padx=5,
                command=lambda: enviar_login())
cadastrar = Button(inicio, text='Cadastrar', bg=cor_azul, font='Montserrat 11 bold', command=lambda: tela_cadastro())


# Segunda Tela


def definir_numero(button, numero):
    button['command'] = lambda: tela_comprar(numero)


# Buttons
botao = [Button(loja, image=imagem[x], bg='white', bd=4, relief='solid') for x in range(10)]
for b in range(10):
    definir_numero(botao[b], b)

# Labels
logo_loja = Label(loja, image=imagem[11], bg=cor_fundo)
gamer_loja = Label(loja, text='Gamer Store', bg=cor_laranja, font='Impact 16 bold', bd=10, relief='raised', width=15)
usuario_butao = Button(loja, image=imagem[12], bg='white', bd=4, relief='solid', )
usuario_label = Label(loja, bg=cor_azul, font='Montserrat 16 bold', width=12, bd=2, relief='solid')
carteira_label = Label(loja, bg=cor_azul, font='Montserrat 16 bold', width=12, bd=2, relief='solid')
carrinho_butao = Button(loja, image=imagem[13], bg='white', bd=4, relief='solid', command=lambda: tela_carrinho())
carrinho_label = Label(loja, bg=cor_fundo, font='Montserrat 14 bold', width=10, anchor=W)
carinho_finalizar = Label(loja, text='Carrinho', bg=cor_fundo, font='Montserrat 14 bold', width=10, anchor=W)
# Recebendo todos os Produtos pelo Servidor
produtos_byte = socket_cliente.receber_bytes()
produtos = pickle.loads(produtos_byte)

produto = [Label(loja, text=t.get_nome(), bg=cor_fundo, font='Montserrat 12 bold') for t in produtos]
textos_loja = [str(p.descricao) for p in produtos]
# Terceira Tela
# Labels
dados = Label(user, text='Dados', bg=cor_laranja, font='Montserrat 16 bold', anchor=N, width=25, height=13, bd=4,
              relief='solid')
nome_dado = Label(user, bg=cor_azul, font='Montserrat 12 bold', bd=2, relief='solid')
email_dado = Label(user, bg=cor_azul, font='Montserrat 12 bold', bd=2, relief='solid')
cpf_dado = Label(user, text='CPF: 123-456-789-10', bg=cor_azul, font='Montserrat 12 bold', bd=2, relief='solid')
data_dado = Label(user, text='Nascimento: 01/01/1901', bg=cor_azul, font='Montserrat 12 bold', bd=2, relief='solid')
endereco_dado = Label(user, text='Enderaço: Rua X, 00', bg=cor_azul, font='Montserrat 12 bold', bd=2, relief='solid')
cidade_dado = Label(user, text='Cidade: Fortaleza, Ceará', bg=cor_azul, font='Montserrat 12 bold', bd=2, relief='solid')
cartao_dado = Label(user, text='Cartão 1: XXXX-XXXX-XXXX-XXXX', bg=cor_azul, font='Montserrat 12 bold', bd=2,
                    relief='solid')
cartao2_dado = Label(user, text='Cartão 2: XXXX-XXXX-XXXX-XXXX', bg=cor_azul, font='Montserrat 12 bold', bd=2,
                     relief='solid')
carteira_dados = Label(user, text='Carteira', bg=cor_laranja, font='Montserrat 16 bold', anchor=N, width=25, height=8,
                       bd=4, relief='solid')
valor_dados = Label(user, bg=cor_azul, font='Montserrat 12 bold', bd=2, relief='solid')
valor_label = Label(user, text='Inserir na Carteira: ', bg=cor_azul, font='Montserrat 12 bold', bd=2, relief='solid')
resposta_valor = Label(user, font='Verdana 12 italic', bg=cor_laranja, width=31, height=2)
casa_label = Label(user, text='Voltar pra \nTela Inicial', bg=cor_fundo, font='Montserrat 16 bold', height=2)
logoff_label = Label(user, text='Sair da\nConta', bg=cor_fundo, font='Montserrat 16 bold', height=2)
# Buttons
senha_dado = Button(user, text='Alterar Senha', bg=cor_azul, font='Montserrat 12 bold', bd=4, relief='solid')
casa_botao = Button(user, image=imagem[14], bg='white', bd=4, relief='solid', command=lambda: tela_loja())
valor_botao = Button(user, text='Adicionar Valor', bg=cor_azul, font='Montserrat 12 bold', bd=4, relief='solid')
logoff_botao = Button(user, image=imagem[15], bg='white', bd=4, relief='solid', command=lambda: deslogar())
# Entrys
valor_entry = Entry(user, bg='white', font='Montserrat 12', bd=2, relief='solid', width=12)

# Quarta Tela
imagens_produtos = [Label(compra, image=imagem[x], bg='white', width=300, height=300, bd=4, relief='solid') for x in
                    range(16, 26)]

descricao_labels = [Label(compra, text=t, bg=cor_fundo, font='Montserrat 11 bold', width=46, height=4)
                    for t in textos_loja]
compra_box = Label(compra, text='Produto', bg=cor_azul, font='Montserrat 16 bold', anchor=N, width=33, height=1,
                   bd=4, relief='solid')
descricao_box = Label(compra, text='Descrição', bg=cor_azul, font='Montserrat 16 bold', anchor=N, width=33, height=1,
                      bd=4, relief='solid')
nome_preco = Label(compra, bg='white', font='Montserrat 16 bold', width=33, padx=3, height=1, bd=2, relief='solid')
quantidade_label = Label(compra, text='Quantidade de Produtos Desejados:', bg='white', font='Montserrat 16 bold', bd=2,
                         relief='solid')
quantidade_entry = Spinbox(compra, bg='white', font='Montserrat 16 bold', width=4, bd=2, relief='solid', from_=1,
                           to=20)
compra_botao = Button(compra, text='Adicionar ao Carrinho', bg=cor_laranja, font='Montserrat 12 bold', bd=4,
                      relief='solid')
especificacoes = Button(compra, text='Especificações', bg=cor_azul, font='Montserrat 14 bold', bd=4, relief='solid')

# Quinta Tela
itens_carrinho = Label(carrinho, text='Itens do Carrinho', bg=cor_laranja, font='Montserrat 16 bold', anchor=N,
                       width=39, padx=3, height=14, bd=4, relief='solid')
itens_label = Label(carrinho, text='%5s%22s%30s%16s%16s' % ('Id', 'Produto', 'Preço', 'Quant.', 'Preço Total'),
                    bg='white', font='Montserrat 12', width=55, anchor=W, bd=2, relief='solid')
itens_id = Label(carrinho, bg='white', font='Montserrat 12', anchor=NE, justify=RIGHT, width=4, height=12, bd=2,
                 relief='solid')
itens_nomes = Label(carrinho, bg='white', font='Montserrat 12', anchor=NE, justify=RIGHT, width=17, height=12, bd=2,
                    relief='solid')
itens_preco = Label(carrinho, bg='white', font='Montserrat 12', anchor=NE, justify=RIGHT, width=14, height=12, bd=2,
                    relief='solid', padx=4)
itens_quantidade = Label(carrinho, bg='white', font='Montserrat 12', anchor=NE, justify=RIGHT, width=3, height=12, bd=2,
                         relief='solid')
itens_total = Label(carrinho, bg='white', font='Montserrat 12', anchor=NE, justify=RIGHT, width=15, height=12, bd=2,
                    relief='solid')
total_label = Label(carrinho, bg='white', font='Montserrat 12', width=55, anchor=E, bd=2, relief='solid')

botao_comprar = Button(compra, text='Finalizar Compra', bg=cor_azul, font='Montserrat 14 bold', bd=4, relief='solid',
                       command=lambda: finalizar_compra())
remover_item = Label(carrinho, text='Remover Item\ndo Carrinho', bg=cor_laranja, font='Montserrat 16 bold', anchor=N,
                     width=14, padx=3, height=7, bd=4, relief='solid')
botao_remover = Button(compra, text='Remover', bg=cor_azul, font='Montserrat 12 bold', bd=4, relief='solid',
                       command=lambda: remover())
id_label = Label(user, text='Id do Item: ', bg=cor_azul, font='Montserrat 12 bold', bd=2, relief='solid')
id_entry = Entry(user, bg='white', font='Montserrat 12', bd=2, relief='solid', width=4)
id_resposta = Label(user, font='Verdana 12 italic', bg=cor_laranja, width=13,)


# Funções do Programa


def mover_tudo():
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
    dados.place(x=1000, y=1000)
    logo_loja.place(x=1000, y=1000)
    gamer_loja.place(x=1000, y=1000)
    usuario_butao.place(x=1000, y=1000)
    usuario_label.place(x=1000, y=1000)
    carteira_label.place(x=1000, y=1000)
    nome_dado.place(x=1000, y=1000)
    carrinho_butao.place(x=1000, y=1000)
    carrinho_label.place(x=1000, y=1000)
    carinho_finalizar.place(x=1000, y=1000)
    email_dado.place(x=1000, y=1000)
    cpf_dado.place(x=1000, y=1000)
    data_dado.place(x=1000, y=1000)
    endereco_dado.place(x=1000, y=1000)
    cidade_dado.place(x=1000, y=1000)
    cartao_dado.place(x=1000, y=1000)
    cartao2_dado.place(x=1000, y=1000)
    senha_dado.place(x=1000, y=1000)
    carteira_dados.place(x=1000, y=1000)
    valor_dados.place(x=1000, y=1000)
    valor_label.place(x=1000, y=1000)
    valor_entry.place(x=1000, y=1000)
    valor_entry.delete(0, 1)
    valor_botao.place(x=1000, y=1000)
    resposta_valor.place(x=1000, y=1000)
    casa_botao.place(x=1000, y=1000)
    casa_label.place(x=1000, y=1000)
    logoff_botao.place(x=1000, y=1000)
    logoff_label.place(x=1000, y=1000)
    compra_box.place(x=1000, y=1000)
    descricao_box.place(x=1000, y=1000)
    nome_preco.place(x=1000, y=1000)
    quantidade_entry.place(x=1000, y=1000)
    quantidade_entry.delete(0, END)
    quantidade_label.place(x=1000, y=1000)
    compra_botao.place(x=1000, y=1000)
    especificacoes.place(x=1000, y=1000)
    itens_carrinho.place(x=1000, y=1000)
    itens_id.place(x=1000, y=1000)
    itens_nomes.place(x=1000, y=1000)
    itens_label.place(x=1000, y=1000)
    itens_preco.place(x=1000, y=1000)
    itens_quantidade.place(x=1000, y=1000)
    itens_total.place(x=1000, y=1000)
    total_label.place(x=1000, y=1000)
    botao_comprar.place(x=1000, y=1000)
    remover_item.place(x=1000, y=1000)
    botao_remover.place(x=1000, y=1000)
    id_entry.place(x=1000, y=1000)
    id_label.place(x=1000, y=1000)
    id_resposta.place(x=1000, y=1000)
    resposta_label['text'] = ''
    resposta_valor['text'] = ''
    for w in descricao_labels:
        w.place(x=1000, y=1000)
    for x in botao:
        x.place(x=1000, y=1000)
    for y in produto:
        y.place(x=1000, y=1000)
    for z in imagens_produtos:
        z.place(x=1000, y=1000)


def enviar_dado(dado):  # Enviar dado do Usuario
    if bool(dado.get()):
        socket_cliente.enviar(dado.get().strip())
    else:
        socket_cliente.enviar(' ')


def enviar_login():  # Função de Enviar o Login
    socket_cliente.enviar('1')
    enviar_dado(email_entry)
    enviar_dado(senha_entry)
    resposta = socket_cliente.receber_decodificado()
    resposta_label['text'] = resposta
    if resposta == 'Bem vindo':
        atualizar_usuario()
        tela_loja()
        messagebox.showinfo(title='Login Bem Sucedido', message=f'Bem Vindo {usuario.get_nome()}!')


def enviar_cadastro():  # Enviar conta para criação do usuario
    socket_cliente.enviar('2')
    enviar_dado(nome_entry)
    enviar_dado(email_entry)
    enviar_dado(senha_entry)
    resposta = socket_cliente.receber_decodificado()
    resposta_label['text'] = resposta
    if resposta == 'Conta criada':
        atualizar_usuario()
        tela_loja()
        messagebox.showinfo(title='Login Bem Sucedido', message=f'Bem Vindo {usuario.get_nome()}!')


def enviar_valor():  # Envia valor da Carteira
    socket_cliente.enviar('3')
    try:
        float(valor_entry.get())
        socket_cliente.enviar(valor_entry.get())
    except ValueError:
        socket_cliente.enviar('-1')
    valor_entry.delete(0, 1)
    valor_entry.delete(0, END)
    resposta = socket_cliente.receber_decodificado()
    resposta_valor['text'] = resposta
    atualizar_usuario()
    atualizar_valores()


def enviar_produto(id_p):
    socket_cliente.enviar('4')
    socket_cliente.enviar(str(id_p))
    try:
        int(quantidade_entry.get())
        if 0 < int(quantidade_entry.get()) <= 20:
            socket_cliente.enviar(quantidade_entry.get())
            atualizar_usuario()
            atualizar_valores()
        else:
            socket_cliente.enviar('-1')
    except ValueError:
        socket_cliente.enviar('-1')
    quantidade_entry.delete(0, END)
    resposta = socket_cliente.receber_decodificado()
    tela_loja()
    if resposta == 'Item Adicionado ao Carrinho com Sucesso!':
        messagebox.showinfo(title='Adicionar no Carrinho', message=resposta)
    else:
        messagebox.showerror(title='Adicionar no Carrinho', message=resposta)


def atualizar_usuario():  # atualizar o Usuario
    global usuario
    usuario_byte = socket_cliente.receber_bytes()
    usuario = pickle.loads(usuario_byte)


def deslogar():
    if messagebox.askokcancel(title='Sair?', message=f'{usuario.get_nome()} quer Sair da Conta?'):
        socket_cliente.enviar('9')
        resposta = socket_cliente.receber_decodificado()
        tela_inicial()
        messagebox.showinfo(title='Volte Sempre!', message=resposta)


def atualizar_valores():
    valor_dados['text'] = 'Valor Total na Carteira: %.2f R$' % usuario.get_carteira().get_total()
    carteira_label['text'] = '%.2f R$' % usuario.get_carteira().get_total()
    carteira_label['text'] = '%.2f R$' % usuario.get_carteira().get_total()


def finalizar_compra():
    socket_cliente.enviar('5')
    resposta = socket_cliente.receber_decodificado()
    if resposta == 'Pagamento Aprovado.\nCompra Bem Sucedida!':
        atualizar_usuario()
        atualizar_valores()
    tela_loja()
    messagebox.showinfo(title='Compra', message=resposta)


def remover():
    socket_cliente.enviar('6')
    try:
        int(id_entry.get())
        if 0 < int(id_entry.get()) <= usuario.get_compra().tamanho_lista():
            socket_cliente.enviar(id_entry.get())
            atualizar_usuario()
            atualizar_valores()
        else:
            socket_cliente.enviar('-1')
    except ValueError:
        socket_cliente.enviar('-1')
    id_entry.delete(0, END)
    resposta = socket_cliente.receber_decodificado()
    id_resposta['text'] = resposta
    tela_carrinho()


def tela_inicial():  # Tela Inicial
    # Movendo coisas pra longe
    mover_tudo()

    nome_loja.place(x=45, y=100)
    email_label.place(x=45, y=170)
    senha_label.place(x=45, y=198)
    email_entry.delete(0, END)
    email_entry.place(x=125, y=170)
    senha_entry.delete(0, END)
    senha_entry.place(x=125, y=198)
    entrar['text'] = 'Entrar'
    entrar['command'] = lambda: enviar_login()
    entrar.place(x=45, y=230)
    logo_imagem.place(x=400, y=-5)
    cadastrar['text'] = 'Cadastrar'
    cadastrar['command'] = lambda: tela_cadastro()
    cadastrar.place(x=155, y=330)
    resposta_label.place(x=45, y=275)


def tela_cadastro():  # Função da Tela de Cadastro
    # Movendo coisas pra longe
    mover_tudo()

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
    entrar['command'] = lambda: enviar_cadastro()
    entrar.place(x=450, y=230)
    cadastrar['text'] = 'Voltar'
    cadastrar.place(x=580, y=330)
    cadastrar['command'] = lambda: tela_inicial()
    resposta_label.place(x=450, y=275)


def menu_cima():  # Tela de Cima
    logo_loja.place(x=26, y=3)
    gamer_loja.place(x=110, y=17)
    usuario_butao.place(x=700, y=3)
    usuario_butao['command'] = lambda: tela_usuario()
    usuario_label['text'] = usuario.get_nome().split()[0]
    usuario_label.place(x=530, y=17)
    carteira_label['text'] = '%.2f R$' % usuario.get_carteira().get_total()
    carteira_label.place(x=530, y=47)
    carrinho_butao.place(x=315, y=3)
    carrinho_label['text'] = '%.2f R$' % usuario.get_compra().get_valor_compra()
    carrinho_label.place(x=400, y=47)
    carinho_finalizar.place(x=400, y=17)


def tela_loja():  # Tela Inicial dos Produtos
    # Movendo coisas pra longe
    mover_tudo()
    menu_cima()

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


def tela_usuario():  # Tela Do Usuario
    mover_tudo()
    menu_cima()
    # Dados
    dados.place(x=26, y=100)
    nome_dado['text'] = f'Nome: {usuario.get_nome()}'
    nome_dado.place(x=35, y=140)
    email_dado['text'] = f'Email: {usuario.get_email()}'
    email_dado.place(x=35, y=170)
    cpf_dado.place(x=35, y=200)
    data_dado.place(x=35, y=230)
    endereco_dado.place(x=35, y=260)
    cidade_dado.place(x=35, y=290)
    cartao_dado.place(x=35, y=320)
    cartao2_dado.place(x=35, y=350)
    senha_dado.place(x=130, y=380)
    # Carteira
    carteira_dados.place(x=426, y=100)
    valor_dados['text'] = 'Valor Total na Carteira: %.2f R$' % usuario.get_carteira().get_total()
    valor_dados.place(x=435, y=140)
    valor_label.place(x=435, y=170)
    valor_entry.place(x=585, y=170)
    valor_botao['command'] = lambda: enviar_valor()
    valor_botao.place(x=530, y=200)
    resposta_valor.place(x=435, y=245)
    # Voltar
    casa_botao.place(x=700, y=350)
    casa_label.place(x=590, y=360)
    # Deslogar
    logoff_botao.place(x=426, y=350)
    logoff_label.place(x=505, y=360)


def tela_comprar(id_p):  # Tela dos Produtos para Compra
    mover_tudo()
    menu_cima()

    # Produto
    imagens_produtos[id_p].place(x=26, y=100)
    # Comprar
    compra_box.place(x=360, y=100)
    nome_preco['text'] = '%s          Preço: %.2f R$' % (produtos[id_p].get_nome(), produtos[id_p].get_preco())
    nome_preco.place(x=360, y=132)
    quantidade_label.place(x=360, y=160)
    quantidade_entry.place(x=729, y=160)
    quantidade_entry.insert(0, 1)
    compra_botao['command'] = lambda: enviar_produto(id_p)
    compra_botao.place(x=486, y=192)
    # Descrição
    descricao_box.place(x=360, y=230)
    descricao_labels[id_p].place(x=375, y=265)
    especificacoes.place(x=360, y=350)
    # Parte de Sair
    casa_botao.place(x=700, y=350)
    casa_label.place(x=590, y=360)


def tela_carrinho():  # Tela de Finalizar compra
    mover_tudo()
    menu_cima()

    # Tela
    itens_carrinho.place(x=20, y=90)
    itens_label.place(x=30, y=120)
    itens_id['text'] = usuario.get_compra().listar_itens_separados('id')
    itens_id.place(x=30, y=142)
    itens_nomes['text'] = usuario.get_compra().listar_itens_separados('nome')
    itens_nomes.place(x=70, y=142)
    itens_preco['text'] = usuario.get_compra().listar_itens_separados('preco')
    itens_preco.place(x=227, y=142)
    itens_quantidade['text'] = usuario.get_compra().listar_itens_separados('quantidade')
    itens_quantidade.place(x=360, y=142)
    itens_total['text'] = usuario.get_compra().listar_itens_separados('total')
    itens_total.place(x=390, y=142)
    total_label['text'] = 'Valor Total da Compra: %8.2f R$' % usuario.get_compra().get_valor_compra()
    total_label.place(x=30, y=360)
    botao_comprar.place(x=351, y=387)
    # Remover Item
    remover_item.place(x=586, y=90)
    id_label.place(x=620, y=150)
    id_entry.place(x=709, y=150)
    id_entry.delete(0, END)
    botao_remover.place(x=642, y=180)
    id_resposta.place(x=619, y=230)
    # Parte de Sair
    casa_botao.place(x=700, y=350)
    casa_label.place(x=590, y=360)


def fechar():
    if messagebox.askokcancel("Sair", "Você deseja Sair?"):
        socket_cliente.enviar('0')
        tela.destroy()
        socket_cliente.fechar()


# Começo do Programa
tela_inicial()
tela.protocol("WM_DELETE_WINDOW", lambda: fechar())
tela.mainloop()
