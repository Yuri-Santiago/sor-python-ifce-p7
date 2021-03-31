"""
5.Qual o tamanho ocupado na memória por um inteiro? Uma String vazia? Uma string de um único
caractere? E por um Byte de um caractere?

    inteiro = 28, string vazia = 49, string com um caractere = 50, byte = 34
"""

import sys

inteiro = 11
vazio = ''
string = 'a'
byte = b'b'

print(sys.getsizeof(inteiro))
print(sys.getsizeof(vazio))
print(sys.getsizeof(string))
print(sys.getsizeof(byte))
