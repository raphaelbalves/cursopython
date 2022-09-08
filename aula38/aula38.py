# Escopo

variavel = 'valor'

def func(arg=None):
    arg = arg.replace('v', 'c')
    return arg

outra_variavel = func(variavel)
print(outra_variavel)
print(variavel)