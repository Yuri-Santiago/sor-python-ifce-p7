"""
1. Utilizar exercícios das aulas anteriores e criar interfaces gráficas
para eles.
"""
# Programa Feito por Yuri Mateus Santiago, no dia 13-04-2021

from tkinter import *

# Variáveis Globais
joga = 1
vez = 1
marcacao = 'X'
posicao = [None, None, None, None, None, None, None, None, None]
a = 1
p = 0
# Funções


def troca_vez():  # Função de Trocar a Vez
    global vez
    global marcacao
    global joga
    if vez % 2 != 0:
        marcacao = 'O'
        joga = 2
    else:
        marcacao = 'X'
        joga = 1
    vez += 1


def marcar():  # Função de Marcar no Grid
    global p
    global marcacao
    if posicao[p]['fg'] != 'grey':
        mensagem.configure(text='Jogada Inválida\nSelecione uma posição válida')
        finalizar()
    else:
        mensagem.configure(text='Continue o Jogo')
        posicao[p].configure(text=marcacao, fg='black')
        troca_vez()
        finalizar()
        jogador.configure(text=f'Jogador {joga}')


def trocar():  # Função que troca as posições do Grid
    global p
    global marcacao
    if p == 8:
        p = -1
    p += 1
    fila = ['Esquerda Superior', 'Meio Superior', 'Direita Superior', 'Esquerda Central', 'Centro', 'Direita Central',
            'Esquerda Inferior', 'Meio Inferior', 'Direita Inferior']
    local.configure(text=f"{fila[p]}")

    if posicao[p]['fg'] == 'black' and posicao[p]['text'] == '':
        posicao[p].configure(text=marcacao, fg='grey')

    if posicao[p-1]['fg'] != 'black':
        posicao[p-1].configure(text='', fg='black')


def finalizar():  # Fução que Verifica se o Jogo Acabou
    ret = ganhar()
    if not ret:
        condicao = 0
        for i in range(len(posicao)):
            if posicao[i]['text'] != '':
                condicao += 1
            else:
                condicao = 0
        if condicao == 9:
            mensagem.configure(text='Fim de Jogo!\nDeu Velha!')
            marca.configure(text='Reiniciar', command=lambda: reiniciar())
            troca.configure(text='Fechar', command=lambda: principal.quit())
    else:
        marca.configure(text='Reiniciar', command=lambda: reiniciar())
        troca.configure(text='Fechar', command=lambda: principal.quit())


def ganhar():  # Função que Checa se Algum Jogador Ganhou
    global joga
    if joga == 1:
        v = 2
    else:
        v = 1
    vit = 0
    # Verificação Horizontal
    for m in range(0, 7, 3):
        if posicao[m]['text'] == posicao[m+1]['text'] and posicao[m+1]['text'] == posicao[m+2]['text'] \
                and posicao[m]['text'] != '':
            mensagem.configure(text=f'Fim de Jogo!\nVitória do Jogador {v}')
            vit += 1
    # Verificação Vertical
    for m in range(0, 3):
        if posicao[m]['text'] == posicao[m+3]['text'] and posicao[m+3]['text'] == posicao[m+6]['text'] \
                and posicao[m]['text'] != '':
            mensagem.configure(text=f'Fim de Jogo!\nVitória do Jogador {v}')
            vit += 1
    # Verificação Diagonal Descendente
    if posicao[0]['text'] == posicao[4]['text'] and posicao[4]['text'] == posicao[8]['text'] and \
            posicao[0]['text'] != '':
        mensagem.configure(text=f'Fim de Jogo!\nVitória do Jogador {v}')
        vit += 1
    # Verificação Diagonal Ascendente
    if posicao[2]['text'] == posicao[4]['text'] and posicao[4]['text'] == posicao[6]['text'] and \
            posicao[2]['text'] != '':
        mensagem.configure(text=f'Fim de Jogo!\nVitória do Jogador {v}')
        vit += 1

    if vit > 0:
        return True
    return False


def reiniciar():  # Função para Reiniciar o Grid
    global a
    a = 1
    marca.configure(text="Marcar", command=lambda: marcar())
    troca.configure(text="Trocar Posição", command=lambda: trocar())
    mensagem.configure(text='Bom Jogo!')
    d = 0
    for w in range(3):
        for z in range(3):
            posicao[d] = Label(cima, text='', fg='black', width=4, height=2, font=('Impact', '20'))
            posicao[d].grid(row=w, column=z, padx=2, pady=2)
            d += 1
    posicao[p].configure(text=marcacao, fg='grey')


# Criando a Tela Principal
principal = Tk()
principal.title("Jogo da Velha")
principal.geometry('310x350')

# Criando Janelas
cima = Frame(principal, bg='black')
baixo = Frame(principal)
fundo = Frame(principal)
cima.pack()
baixo.pack()
fundo.pack()

# Criando o Grid
c = 0
for x in range(3):
    for y in range(3):
        posicao[c] = Label(cima, text='', fg='black', width=4, height=2, font=('Impact', '20'))
        posicao[c].grid(row=x, column=y, padx=2, pady=2)
        c += 1

# Criando os botões do Jogo e alguns Labels
marca = Button(baixo, text="Marcar", command=lambda: marcar())
marca.grid(row=0, column=0, padx=1, pady=1)
troca = Button(baixo, text="Trocar Posição", command=lambda: trocar())
troca.grid(row=0, column=1, padx=1, pady=1)
jogador = Label(baixo, text="Jogador 1", font=('Impact', '13'))
jogador.grid(row=1, column=0, padx=1, pady=1)
local = Label(baixo, text="Esquerda Superior", font=('Impact', '13'))
local.grid(row=1, column=1, padx=1, pady=1)
mensagem = Label(fundo, text="Bom Jogo!", font=('Impact', '13'))
mensagem.grid(row=0, column=0, padx=1, pady=1)
posicao[0].configure(text=marcacao, fg='grey')
principal.mainloop()
