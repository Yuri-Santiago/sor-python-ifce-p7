import pickle
from usuario import Usuario
usuario = Usuario('Admin', 'a', 'a', 99999)
eu = Usuario('Yuri', 'yuri@gmail.com', 'senha', 150)
lista = [usuario, eu]
with open('usuarios.pickle', 'wb') as arquivo_usuarios:
                pickle.dump(lista, arquivo_usuarios)