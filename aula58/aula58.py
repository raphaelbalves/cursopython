from aula56.dados import produtos, pessoas, lista
from functools import reduce

# soma_lista = sum(lista)
# print(soma_lista)
#
# acumula = 0
# for x in lista:
#     acumula += x
#
# print(acumula)

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_precos_produtos = reduce(lambda ac, i: i['preco'] + ac, produtos, 0)
print(f'A média dos valores dos produtos: {soma_precos_produtos / len(produtos)}')
