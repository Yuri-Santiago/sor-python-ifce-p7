"""
Como evitar o erro (UnicodeDecodeError:) do ítem anterior utilizando o parâmetro ‘replace' ou ‘ignore' do
método decode? Diferencie-os.

    ignore: ignora o caractere que nao pode ser decodificado
    replace: substitui o caractere errado por uma interrogação
"""

palavra_ignore = b'\xff\xfeA\x00p\x00r\x00e\x00n\x00d\x00e\x00n\x00d\x00o\x00 \x00p\x00r\x00o\x00g\x00r\x00a\x00m' \
                 b'\x00a\x00\xe7\x00\xe3\x00o\x00 \x00e\x00m\x00 ' \
                 b'\x00P\x00y\x00t\x00h\x00o\x00n\x00'.decode(errors='ignore')

palavra_replace = b'\xff\xfeA\x00p\x00r\x00e\x00n\x00d\x00e\x00n\x00d\x00o\x00 \x00p\x00r\x00o\x00g\x00r\x00a\x00m' \
                 b'\x00a\x00\xe7\x00\xe3\x00o\x00 \x00e\x00m\x00 ' \
                  b'\x00P\x00y\x00t\x00h\x00o\x00n\x00'.decode(errors='replace')

print(palavra_ignore)
print(palavra_replace)
