"""
O que acontece se for utiliza a codificação errada? Explique o erro mostrado.
    Aqui em baixo temos um código com erro pois deveria estar sendo decodificado com o UTF-16
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
"""

palavra = b'\xff\xfeA\x00p\x00r\x00e\x00n\x00d\x00e\x00n\x00d\x00o\x00 \x00p\x00r\x00o\x00g\x00r\x00a\x00m\x00a\x00' \
          b'\xe7\x00\xe3\x00o\x00 \x00e\x00m\x00 \x00P\x00y\x00t\x00h\x00o\x00n\x00'.encode()

print(palavra)
