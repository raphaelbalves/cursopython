# Dicionário

# # Outra forma de criar dicionário
# d2 = dict(chachave1='vavalor1', chachave2='vavalor2')
# print(d2)
#
# d1 = {'chave1':'valor1'}
# d1['chave2'] = 'valor2'
# print(d1)
# print(d1.get('chave2'))

# d1 = {
#     'str': 'valor',
#     123: 'outro valor',
#     (1, 2, 3, 4): 'Tupla'
# }
#
# print(d1)
#
# if 'str' in d1:
#     print(d1['str'])
# else:
#     print('Chave não existe.')
#
# print(d1.get('naoexiste'))
#
# d1.update({'novachave': 'novovalor'})
# # del d1['str']
# d1.pop('str')
# print(d1)
#
# for k, v in d1.items():
#     print(k, v)

clientes = {
    'cliente1': {
        'nome': 'raphael',
        'sobrenome': 'barros'
    },

    'cliente2': {
        'nome': 'iana',
        'sobrenome': 'soares'
    }
}

for k in clientes.items():
    for k2, v2 in k[1].items():
        print(k2, v2)