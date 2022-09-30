from aula56.dados import produtos, pessoas, lista

# nova_lista = filter(lambda x: x > 5, lista)
# print(list(nova_lista))
#
# teste_lista = [x for x in lista if x > 5]
# print(teste_lista)

# nova_lista_produtos = filter(lambda x: x['preco'] > 50, produtos)
# print(list(nova_lista_produtos))

def procura_luiz(p):
    if p['nome'] == 'Luiz':
        p['idade'] = 66
    return True

nova_idade = filter(procura_luiz, pessoas)
print(list(nova_idade))