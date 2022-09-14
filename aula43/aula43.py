perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 2?',
        'respostas': {'a': '4', 'b': '10', 'c': '6'},
        'resposta_certa': 'c'
    }
}

# Versão 1

# for k, v in perguntas.items():
#     print(k)
#     print(f"\t{v['pergunta']}")
#     for x, y in v['respostas'].items():
#         print(f"\t\t{x}: {y}")
#
#     resposta_usuario = input('Digite a letra da resposta: ')
#     if resposta_usuario == v['resposta_certa']:
#         print(f'Você acertou. Resposta: {resposta_usuario}')
#         print()
#     else:
#         print(f"Você errou. Resposta: {v['resposta_certa']}")
#         print()

# Versão 2
pontos = 0

for k, v in perguntas.items():
    print(k)
    print(f"\t{v['pergunta']}")
    for x, y in v['respostas'].items():
        print(f"\t\t{x}: {y}")
    print()

for k, v in perguntas.items():

    resposta_usuario = input(f"Responda a {k.lower()}: ")
    if resposta_usuario == v['resposta_certa']:
        pontos += 1
        print(f'Você acertou. Resposta: {resposta_usuario}')
        print()
    else:
        print(f"Você errou. Resposta: {v['resposta_certa']}")
        print()

print(f'Você conseguiu {pontos} pontos.')