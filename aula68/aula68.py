# def lista_de_clientes(clientes_iteravel, lista=[]):
#     lista.extend(clientes_iteravel)
#     return lista

# solução

def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista





clientes1 = lista_de_clientes(['joão', 'maria', 'eduardo'])
clientes2 = lista_de_clientes(['marcos', 'jonas', 'zico'])
print(clientes1)
print(clientes2)
