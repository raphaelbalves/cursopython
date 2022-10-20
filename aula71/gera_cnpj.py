from random import randint
from aula70.funcoes_cnpj import validar


def formatar_cnpj(cnpj):
    cnpj = list(cnpj)
    cnpj.insert(2, '.')
    cnpj.insert(6, '.')
    cnpj.insert(10, '/')
    cnpj.insert(15, '-')
    return "".join(cnpj)


def gerador_cnpj():

    while True:
        cnpj = ''
        for numero in range(14):
            cnpj += str(randint(0, 9))
        cnpj_formatado = formatar_cnpj(cnpj)

        if validar(cnpj_formatado):
            print(f'CNPJ válido: {cnpj_formatado}')
            break



