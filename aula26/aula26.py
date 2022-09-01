lista = [
    ['edu', 'joao', 'luiz'],
    ['maria', 'aline', 'joana'],
    ['helena', 'ed', 'lu']
]

for x, y in enumerate(lista):
    print(x, y)

print()
print('O enumerate enumera.')
print()

for x, y in enumerate(lista, 86):
    print(x, y)


