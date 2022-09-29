from dados import produtos, pessoas, lista

# nova_lista = [x * 2 for x in lista]
# print(nova_lista)
# nova_lista = map(lambda x: x * 2, lista)
# print(list(nova_lista))

# so_precos = map(lambda x: {x['preco'] + x['preco'] * 0.05}, produtos)

# def aumenta_precos(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p
# alterar_precos = map(aumenta_precos, produtos)
#
# print(list(alterar_precos))

novas_pessoas = map(lambda x: x['nome'], pessoas)


print(list(novas_pessoas))