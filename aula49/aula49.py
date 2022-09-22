import sys
# lista = list(range(1000))
# print(sys.getsizeof(lista))

# Geradores
import time


# def gera():
#     r = []
#     for n in range(100):
#         r.append(n)
#         time.sleep(0.1)
#     return r
#
# g = gera()
# for v in g:
#     print(v)

# def gera():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#
# g = gera()
# print(g)
#
# for x in g:
#     print(x)
# # for v in g:
# #     print(v)

# lista = [x for x in range(100)]
# print(type(lista))
# print(lista)
# lista = (x for x in range(100))
# print(type(lista))
# print(next(lista))

# nome = (x for x in 'Luiz Otávio')
# print(next(nome))
# print(next(nome))
#
# nome2 = 'raphael'
# print(type(nome2))
# iterador = iter(nome)
# print(type(iterador))

nome = 'raphael'
iterador = iter(nome)
gerador = (x for x in nome)
print(type(nome))
print(type(iterador))
print(type(gerador))