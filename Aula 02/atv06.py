# Escrever um programa que coleta a senha do Usuário(previamente ajustada), armazena a senha digitada em uma lista e
# retorna a quantidade de vezes que o usuário precisou para digitar a senha correta

senha = ''
vezes = 0

while senha != 'fofinho':
    senha = input('Digite a sua senha de usuário: ')
    vezes += 1
print(f'Você precisou de {vezes} tentativas para acertar a senha')
