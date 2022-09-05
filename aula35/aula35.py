# def funcao(var1='rocombole', var2='melancia'):
#     print(var1, var2)
#
# funcao(var2='pera', var1='uva')

# def funcao(var):
#     return var
#
# variavel = funcao('coisa')
# print(variavel)

# def divisao(n1, n2):
#     if n2 == 0:
#         return
#
#     return n1 / n2
#
# divide = divisao(10, 2)
#
# if divide:
#     print(divide)
# else:
#     print('Conta inválida.')

# def casa():
#     return 3
#
# numero = casa()
# print(numero)


def funcao1():
    print('carneiro')

def funcao2():
    return funcao1

var = funcao2()
var()