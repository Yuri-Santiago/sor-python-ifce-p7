import pickle
from usuario import Usuario

usuario0 = Usuario('Admin', 'admin@infra', 'senhasecreta', 999999)
usuario1 = Usuario('Yuri', 'yuri@gmail.com', 'senha', 150)
usuario2 = Usuario('Raquel', 'raquel@gmail.com', '12345', 1000)
usuario3 = Usuario('Kelvin', 'kelvin@gmail.com', 'oier', 189.90)
lista = [usuario0, usuario1, usuario2, usuario3]

with open('usuarios.pickle', 'wb') as usuarios:
    pickle.dump(lista, usuarios)
print('Finalizado!')
