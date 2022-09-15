# s1 = {1, 2, 3, 4, 5}
# print(type(s1))
# print(s1)
# for x in s1:
#     print(x)
#
#
# s2 = set()
# s2.add(1)
# s2.add(2)
# s2.add('casa')
# s2.add((44, 22, 66))
# print(s2)
# s2.discard('casa')
# print(s2)
#
# s3 = set()
# s3.update('python')
# print(s3)
#
# l1 = [1, 2, 1, 1, 1, 3, 4, 5, 5, 6, 6, 6, 6, 6, 7, 8, 9, 9, 9, 'L', 'U', 'L', 'A']
# print(set(l1))
#
#
# ex1 = {1, 2, 3, 4, 5, 7}
# ex2 = {1, 2, 3, 4, 5, 6}
# ex3 = ex1 | ex2
# print(ex3)
# ex4 = ex1 & ex2
# print(ex4)
# ex5 = ex1 - ex2
# print(ex5)
# ex6 = ex2 - ex1
# print(ex6)
# ex7 = ex2 ^ ex1
# print(ex7)
# ex8 = ex1 ^ ex2
# print(ex8)

# Exercício nada a ver 1

# while True:
#     resposta = input('Você gosta de Python? ')
#     if resposta.lower() == 'sim':
#         print('Resposta correta.')
#         break
#     else:
#         print('Opa, esta não é a resposta correta, tente novamente.')

# Exercício nada a ver 2

# multiplicador = 0
# numero = int(input('Digite o número para tabuada: '))
#
# while multiplicador <= 10:
#     print(f'{numero} x {multiplicador} = {numero * multiplicador}')
#     multiplicador += 1

# Exercício nada a ver 3

# multiplicador = 1
# acertos = 0
# erros = 0
# numero = int(input('Digite o número que para tabuada: '))
#
# while multiplicador <= 10:
#     tentativa = int(input(f'{numero} x {multiplicador} = '))
#     if tentativa == numero * multiplicador:
#         print(f'Correto.')
#         acertos += 1
#     else:
#         print(f'Que pena, você errou. O valor correto é {numero * multiplicador}.')
#         erros += 1
#     multiplicador += 1
#
# print(f'Você acertou: {acertos}')
# print(f'Você errou: {erros}')

# Exercício nada a ver 4

# contagem = 1
# quantidade_numero = int(input('Informe a quantidade de números de 1 a 9: '))
# numero = 0
# soma = 0
#
# if quantidade_numero < 1 or quantidade_numero > 9:
#     print('Quantidade de número inválida.')
# else:
#     while contagem <= quantidade_numero:
#         numero = int(input(f'Informe o {contagem}o número: '))
#         soma += numero * contagem
#         contagem += 1
# print(f'O resultado final é: {soma}')

# Exercício nada a ver 5

# palavra = input('Digite uma palavra: ')
# inverso = ''
#
# for x in range(len(palavra) - 1, -1, -1):
#     inverso += palavra[x]
#
# print(inverso)
#
# print(f'A palavra invertida é: {palavra[::-1]}')

# Exercício nada a ver 6

# for x in range(1, 10):
#     print(f'{str(x) * x}')

# Exercício nada a ver 7

# vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
# palavra = input('Digite uma palavra: ')
# for letra in palavra.lower():
#     if letra in vogais:
#         vogais[letra] += 1
# print()
# print('-=-Quantidade de vogais-=-')
# for k, v in vogais.items()  :
#     print(f'Quantidade de "{k}": {v}')

# Exercício nada a ver 8

while True:
    entrada = input('Digite um número ou escreva SAIR para encerrar o programa: ')
    if entrada.lower() == 'sair':
        print('Encerrando programa.')
        break
    else:
        if int(entrada) % 2 == 0:
            print(f'{entrada} é um número par.')
        else:
            print(f'{entrada} é um número ímpar.')




