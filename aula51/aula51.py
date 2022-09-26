from itertools import zip_longest, count
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Fortaleza']
estados = ['SP', 'MG', 'BA']
cidades_estados = zip(indice, cidades, estados)

for x, y, z in cidades_estados:
    print(x, y, z)