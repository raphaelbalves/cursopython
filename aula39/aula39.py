# # Exercício 01
#
# def func1(arg):
#     return arg()
#
# def func2():
#     return 'Olá'
#
# print(func1(func2))


# Exercício 02

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome=''):
    return f'Oi, {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, saudacao='ola', nome='luiz')
print(executando)
print(executando2)