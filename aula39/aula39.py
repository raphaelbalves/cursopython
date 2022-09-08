# Exercício 01

def func1(arg):
    return arg

def func2():
    return 'Olá'

print(func1(func2()))

# Exercício 02

def func1(*arg):
    return arg

def func2(*args):
    return args

print(func1(func2('cabeça', 'de'), func2('dinossauro')))

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(saudacao, nome):
    return f'{saudacao} {nome}'

print(func1(fala_oi('carlos'), saudacao('hey', 'romero')))


