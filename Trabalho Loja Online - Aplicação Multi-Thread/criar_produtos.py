import pickle

from produto import Produto

p1 = Produto('Mouse Gamer', 86.90, 'Mouse Gamer excepcional para seus games de FPS,\nquem gosta de jogar no PC, '
                                   'precisa de um mouse gamer\nrápido e que corresponde ao jogador. Ele é \ndiferente '
                                   'do mouse comum e faz toda diferença na hora H.')
p2 = Produto('Teclado Gamer', 376.35, 'Ter um Teclado Gamer vai deixar seus jogos\nmuito mais divertidos, quem não '
                                      'precisa de luzinhas RGB\npara se exibir pros amigos não é mesmo. E o \nbarulho '
                                      'das teclas mecânicas com certeza é mais gostoso.')
p3 = Produto('Headset Gamer', 289.29, 'Para deixar a qualidade de som do seu jogo ainda\nmais real e potente. Vale a '
                                      'pena adquirir o Headset\nGamer! O melhor é que ele vem com um microfone\ntambém '
                                      'pra você poder conversar com outros jogadores.')
p4 = Produto('Monitor Gamer', 4111.00, 'Um bom monitor é importante pra conseguir aproveitar\no melhor do seu '
                                       'computador. Afinal, assim fica\nmais fácil trabalhar, estudar, jogar e etc. '
                                       'Mas\nter um Monitor Gamer é outro nível, por favor né.')
p5 = Produto('Playstation 5', 4899.00, 'É um Playstation 5 amigo, não tem nem o que discutir\nesse console é o mais '
                                       'novo da geração com uma\n potência gigante e diversos jogos incríveis nele.\n'
                                       'Compra Obrigatória para os verdadeiros gamers.')
p6 = Produto('Notebook Gamer', 4842.00, 'Pra quem quer comodidade e desempenho nós trazemos\no sensacional Notebook '
                                        'Gamer! Afinal, quem ai não\nquer viajar e continuar jogando seu Valorant com '
                                        'os\namigos né. Peça já o seu e experimente essa.')
p7 = Produto('Cadeira Gamer', 1169.90, 'Especial para quem gosta de jogar no computador ou\nno videogame, pois você não'
                                       ' quer virar o corcunda\n de Notre Dame. A Cadeira Gamer é ergonômica e super\n '
                                       'confotável, para acabar com a sua dor na coluna.')
p8 = Produto('Celular Gamer', 3875.40, 'Um verdadeiro gamer também precisa jogar no tempo\nlivre, por isso ter um '
                                       'Celular Gamer é a melhor\nopção para você. Quando quiser jogar Free Fire ou\n'
                                       'Clash of Clans é preciso ter desempeho e boa tela.')
p9 = Produto('Controle Gamer', 149.90, 'O Controle Gamer é ideal pra usar no console ou PC.\nPois ele vem com botões, '
                                       'joysticks, gatilhos que\nacompanham o ritmo dos movimentos dos personagens,\n'
                                       'pra que sejam do jeitinho que você precisa e quer.')
p10 = Produto('Xbox Series X', 2799.90, 'Se você gosta de facilidade, de jogos bons, de uma\ncomunidade divertida e '
                                        'custo benefício, comprar\no Xbox Series X é a escolha certa para você. O\n '
                                        'Gamer que está dentro de você precisa desse console.')

lista = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
with open('produtos.pickle', 'wb') as arquivo_produtos:
    pickle.dump(lista, arquivo_produtos)
    print('Deu certo!')
