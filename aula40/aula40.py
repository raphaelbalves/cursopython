# def funcao(arg1, arg2):
#     return arg1 * arg2
#
# var = funcao(2, 2)
# print(var)
#
# # A função abaixo é igual a acima.
#
# a = lambda x, y: x * y
# print(a(2, 3))

lista = [
    ['p4', 13],
    ['p3', 6],
    ['p2', 17],
    ['p1', 18],
    ['p5', 8]
]


# lista.sort(key=lambda item: item[1], reverse=True)
# print(lista)

print(sorted(lista, key=lambda i: i[1], reverse=True))
