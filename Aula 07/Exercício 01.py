"""
Reproduza o conteúdo da tabela mostrada usando comandos a saída formatada do Python para exibir os dados em formato
texto. Ver exemplo.
+--------------------+-------+
|Produtos            |Entrada|
+--------------------+-------+
|Azeite              |     10|
+--------------------+-------+
|Castanha            |    190|
+--------------------+-------+
|Flocos              |      9|
+--------------------+-------+
"""

from collections import namedtuple

# Aqui declaro todos os produtos
produto = namedtuple('produto', ['nome', 'entrada', 'saida', 'saldo', 'preco', 'subtotal'])
produtos = [
    produto(nome='Azeite de Oliva - Extra Virgem LAT 500ml',
            entrada=100, saida=40, saldo=60, preco=21.90, subtotal=1314.00),
    produto(nome='Castanha do Pará - Granel (Gr)',
            entrada=100, saida=5, saldo=95, preco=6.00, subtotal=300.00),
    produto(nome='Flocos de Aveia CXA 500g',
            entrada=1000, saida=200, saldo=800, preco=10.90, subtotal=872.00),
    produto(nome='Paçoca de Amendoim - CXA 30 Und',
            entrada=100, saida=8, saldo=92, preco=1.50, subtotal=30.00),
    produto(nome='Panetone sem Gluten - CXA 1 Und',
            entrada=100, saida=60, saldo=40, preco=17.30, subtotal=692.00),
    produto(nome='Pão Sirio Integral - Saco 500g',
            entrada=100, saida=70, saldo=30, preco=5.90, subtotal=177.00),
    produto(nome='Polpa de Açaí Natural PCT 5L',
            entrada=100, saida=1, saldo=99, preco=7.10, subtotal=639.00),
    produto(nome='Queijo Vegano PCT 450g',
            entrada=100, saida=30, saldo=70, preco=25.00, subtotal=1750.00),
]
# Aqui declaro meu cabeçalho
cabecalho = ['Lista de Produtos', 'QTD Entradas', 'QTD Saídas', 'Saldo Estoque', 'Preço Unitário', 'Subtotal']
# Aqui declaro meu final
fim = ['TOTAL', 5774.00]
# Aqui declaro as linhas para printar e os espaços de tudo
linha = '+'+'-'*40+('+'+'-'*15)*5+'+'
espacos_cabecalho = '|%40s|%15s|%15s|%15s|%15s|%15s|'
espacos_produtos = '|%40s|%15d|%15d|%15d|%15.2f|%15.2f|'
espacos_fim = '|%40s|%15s|%15s|%15s|%15s|%15.2f|'

# Printando o Cabeçalho
print(linha)
print(espacos_cabecalho % (cabecalho[0], cabecalho[1], cabecalho[2], cabecalho[3], cabecalho[4], cabecalho[5]))
# Printando os Produtos
for x in range(len(produtos)):
    print(linha)
    print(espacos_produtos % (produtos[x].nome, produtos[x].entrada, produtos[x].saida, produtos[x].saldo, produtos[x].preco,
                     produtos[x].subtotal))
print(linha)
# Printando o Fim
print(espacos_fim % (' ', ' ', ' ', ' ', fim[0], fim[1]))
print(linha)
