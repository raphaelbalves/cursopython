lista = ['A', 'B', 'C', 'D', 'E']

for x in lista:
    print(x)

lista.append('casa')
print(lista)
lista.pop()
print(lista)

numeros = [3, 5, 7, 8]
print(min(numeros))
numeros.insert(1, 2)
print(numeros)

l1 = [10,11,12]
l2 = [20,21,22]
l1.extend(l2)
print(l1)


n_numeros = list(range(10,21))
print(n_numeros)