# arquivo = open('abc.txt', 'w+')
# arquivo.write('Linha 1\n')
# arquivo.write('Linha 2\n')
# arquivo.write('Linha 3\n')
# arquivo.seek(0, 0)
# print(arquivo.read())
# print('##############')
# arquivo.seek(0, 0)
# print(arquivo.readline(), end='')
# print(arquivo.readline(), end='')
# print(arquivo.readline(), end='')
# print('##############')
#
# arquivo.seek(0, 0)
# print(arquivo.readlines())
#
# arquivo.seek(0, 0)
# print(list(arquivo))
#
# arquivo.close()


# try:
#     arquivo = open('abc.txt', 'w+')
#     arquivo.write('linha')
#     arquivo.seek(0, 0)
#     print(arquivo.read())
# finally:
#     arquivo.close()

# with open('abc.txt', 'w+') as arquivo:
#     arquivo.write('linha\n')
#     arquivo.write('linhaa\n')
#     arquivo.write('linhaaa\n')
#     arquivo.seek(0)
#     print(arquivo.read())

# import os
# os.remove('abc.txt')

import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25
    },

    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30
    }
}

print(d1)
d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('abc.json', 'w+') as arquivo:
    arquivo.write(d1_json)
