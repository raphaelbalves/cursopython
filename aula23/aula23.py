# lista = ['A', 'B', 'C', 'D', 'E']
#
# for x in lista:
#     print(x)
#
# lista.append('casa')
# print(lista)
# lista.pop()
# print(lista)
#
# numeros = [3, 5, 7, 8]
# print(min(numeros))
# numeros.insert(1, 2)
# print(numeros)
#
# l1 = [10, 11, 12]
# l2 = [20, 21, 22]
# l1.extend(l2)
# print(l1)
#
#
# n_numeros = list(range(10,21))
# print(n_numeros)
#
# soma = 0
# mais_lista = list(range(1, 11))
#
# for x in mais_lista:
#     soma += x
# print(soma)

# secreto = 'perfume'
# acerto = []
# dica = []
#
# for x in secreto:
#     dica.append('_')
#     acerto.append(x)
# while True:
#     letra = input('Digite uma letra: ')
#     for i, x in enumerate(secreto):
#         if x == letra:
#             dica.insert(i, x)
#             dica.pop(i+1)
#     print(dica)
#     if dica == acerto:
#         print('Você acertou!')
#         break

secreto = 'perfume'
digitadas = []
chances = 3

while chances > 0:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Só digite uma letra por vez.')
        chances -= 1
        print(f'Você tem mais {chances} chance(s).')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra {letra} está na palavra.')
    else:
        print(f'A letra {letra} não está na palavra.')
        digitadas.pop()

    if letra not in secreto:
        chances -= 1
        print(f'Você tem mais {chances} chance(s).')
        continue

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Você ganhou. A palavra era "{secreto}".')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

