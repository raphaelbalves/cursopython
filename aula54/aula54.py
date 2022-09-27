from itertools import combinations, permutations, product
pessoas = ['luiz', 'andré', 'eduardo',
          'letícia', 'fabrício', 'rose']

teste1 = combinations(pessoas, 2)
print(list(teste1))

teste2 = permutations(pessoas, 2)
print(list(teste2))

teste3 = product(pessoas, repeat=2)
print(list(teste3))
