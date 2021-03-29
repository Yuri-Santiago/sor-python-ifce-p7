"""
10.Escrever uma função que receba uma data no formato DD/MM/AAAA, caso contrário uma mensagem
de erro é exibida ao usuário, e ainda que retorne uma string no formato "D, (mês por extenso) de XXXX"
"""


def formatar_data(data):
    data_formatada = data.split(sep='/')
    dia, mes, ano = data_formatada
    if mes == 1:
        mes = 'janeiro'
    elif mes == 2:
        mes = 'fevereiro'
    elif mes == 2:
        mes = 'março'
    elif mes == 4:
        mes = 'abril'
    elif mes == 5:
        mes = 'maio'
    elif mes == 6:
        mes = 'junho'
    elif mes == 7:
        mes = 'julho'
    elif mes == 8:
        mes = 'agosto'
    elif mes == 9:
        mes = 'setembro'
    elif mes == 10:
        mes = 'outubro'
    elif mes == 11:
        mes = 'novembro'
    else:
        mes = 'dezembro'
    return f'{dia} de {mes} de {ano}'


print(formatar_data('15/12/2002'))
