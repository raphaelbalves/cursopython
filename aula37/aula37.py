# def funcao(a1, a2, a3, a4, a5, nome=None, a6=None):
#     print(a1, a2, a3, a4, a5, nome, a6)

# def funcao(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#
# funcao(1, 2, 3, 4, 5)

# def funcao(*args):
#     args = list(args)
#     args[0] = 20
#     print(args)
#
# funcao(1, 2, 3, 4, 5)

def funcao(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome')
    print(nome)

lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 30, 40, 100]

funcao(*lista1, *lista2, nome='luiz', idade='34')



