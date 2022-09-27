from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Renato', 'nota': 'B'},
    {'nome': 'Carlos', 'nota': 'C'},
    {'nome': 'Jorge', 'nota': 'A'},
    {'nome': 'Alberto', 'nota': 'C'},
    {'nome': 'Messias', 'nota': 'C'},
    {'nome': 'Cleber', 'nota': 'A'},
    {'nome': 'Júlio', 'nota': 'B'},
    {'nome': 'Augusto', 'nota': 'B'},
    {'nome': 'Rogério', 'nota': 'A'}
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for grupo, dados in alunos_agrupados:
    va1, va2 = tee(dados)
    print(grupo)
    for x in va1:
        print(x)

    print(len(list(va2)))
    print()


