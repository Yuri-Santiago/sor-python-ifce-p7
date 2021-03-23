"""
Dada a string “A persistência é o caminho do êxito” codifique-a utilizando UTF-8 e UTF-16.

1.1.O que acontece em cada caso? Justifique.
    As saídas são diferentes e a segunda é bem maior
1.2.Qual a diferença de tamanho entre as saídas em UTF-8 e UTF-16?
    A saída UTF-16 é muito maior que a UTF-8 quase que o dobro
1.3.Tente realizar a codificação/decodificação cruzada. O que acontece?
    Dá errado
"""

palavra = 'A persistência é o caminho do êxito'
palavra_utf8 = palavra.encode()
palavra_utf16 = palavra.encode('utf - 16')

print(palavra_utf8)
print(palavra_utf16)
