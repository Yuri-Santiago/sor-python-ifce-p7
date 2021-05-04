import pickle
from produto import Produto




lista = [p1, p2, p3, p4, p5, p6, p7, p8, p9, 10]
with open('usuarios.pickle', 'wb') as arquivo_usuarios:
                pickle.dump(lista, arquivo_usuarios)