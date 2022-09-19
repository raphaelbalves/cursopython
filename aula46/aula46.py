l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [x * 2 for x in l1]
print(l1)
print(l2)


ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)


ex4 = []
for x in l1:
    for y in range(3):
        ex4.append((x, y))
print(ex4)

l3 = ['Luiz', 'Mauro', 'Maria']
ex5 = [x.replace('a', '@') for x in l3]
print(ex5)

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
)

ex6 = [(y, x) for x, y in tupla]
ex6 = dict(ex6)
print(ex6)


nova_lista = list(range(100))
impar = [x for x in nova_lista if x % 2 != 0 if x > 35]
# Maior que 35
print(impar)

teste = [v if v % 3 == 0 else f'{v} - Não é' for v in nova_lista]
print(teste)
