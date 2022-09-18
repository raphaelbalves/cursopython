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

# while True:
#     entrada = input('Digite um número ou escreva SAIR para encerrar o programa: ')
#     if entrada.lower() == 'sair':
#         print('Encerrando programa.')
#         break
#     else:
#         if int(entrada) % 2 == 0:
#             print(f'{entrada} é um número par.')
#         else:
#             print(f'{entrada} é um número ímpar.')

# Novos exercícios

# Versão 1

# numeros = []
# mult = 1
# while True:
#     numero = int(input('Digite um número [para sair, digite 0]: '))
#     if numero == 0:
#         break
#     numeros.append(numero)
#
# for x in numeros:
#     mult *= x
#
# print(f'Soma: {sum(numeros)}')
# print(f'Multiplicação {mult}')
# print(f'Maior número: {max(numeros)}')
# print(f'Menor número: {min(numeros)}')


# Versão 2

# numeros = []
# mult = 1
# soma = 0
# maior = 0
# menor = 0
# marc = 1
# while True:
#     numero = int(input('Digite um número [para sair, digite 0]: '))
#     if numero == 0:
#         break
#     numeros.append(numero)
#
# for x in numeros:
#     mult *= x
#     soma += x
#     if marc == 1:
#         menor = x
#     if x < menor:
#         menor = x
#     if x > maior:
#         maior = x
#     marc += 1
#
# print(f'Soma: {soma}')
# print(f'Multiplicação {mult}')
# print(f'Maior número: {maior}')
# print(f'Menor número: {menor}')

# Contar palavras

# palavras = []
#
# while True:
#     palavra = input('Digite uma palavra: ')
#     if palavra == '0':
#         break
#     palavras.append(palavra.lower())
#
# opcao = input('Qual palavra quer contar: ')
# contagem = palavras.count(opcao.lower())
#
# print(f'Ocorrência da palavra {opcao.upper()}: {contagem}')

# Numeros repetidos

# numeros_informados = []
# numeros_sem_repeticao = []
# numeros_repetidos = []
#
# while True:
#     numero = int(input('Digite um número: '))
#     if numero == 0:
#         break
#     numeros_informados.append(numero)
#     if numero not in numeros_sem_repeticao:
#         numeros_sem_repeticao.append(numero)
#     if numeros_informados.count(numero) > 1 and numero not in numeros_repetidos:
#         numeros_repetidos.append(numero)
#
# print(f'Números informados: {numeros_informados}')
# print(f'Números sem repetição: {numeros_sem_repeticao}')
# print(f'Números repetidos: {numeros_repetidos}')

# Número par ou ímpar

# numeros = []
# par = []
# impar = []
#
# while True:
#     numero = int(input('Digite um número: '))
#     if numero == 0:
#         break
#     if numero % 2 == 0:
#         par.append(numero)
#     else:
#         impar.append(numero)
#
# print(f'Pares: {par}')
# print(f'Ímpares: {impar}')

# Is super set

# linguagens = {'python', 'java', 'c++'}
# linguagem = {'python'}
#
# if linguagens.issuperset(linguagem):
#     print('linguagens contém linguagem')
# else:
#     print('lingaguens não contém linguagem')
#
# if linguagem.issubset(linguagens):
#     print('linguagem está contida em liguagens')
# else:
#     print('linguagem não está contida em linguagens')

# palavras =[]
# while True:
#     palavra = input('Digite uma palavra: ')
#     if palavra == '0':
#         break
#     palavras.append(palavra)
#
# conjunto = set(palavras)
#
# for x in conjunto:
#     if palavras.count(x) == 1:
#         print(f'"{x}" foi digitada uma única vez.')

# produtos = {
#     "1": ['Teclado', 300, 166.71],
#     "2": ['Mouse', 125, 80.57],
#     "3": ['Processador', 25, 875.64],
#     "4": ['Cooler', 70, 35.14]
# }
#
# print('Código do produto, produto, quantidade e valor.')
# for x, y in produtos.items():
#     print(f'{x} - {y[0]} - {y[1]} - {y[2]}')
#
# while True:
#     opcao = input('Opções:\n'
#                   '1 - Registrar entrada de produto\n'
#                   '2 - Registrar saída de profuto\n'
#                   '3 - Sair do sistema\n'
#                   'Qual opcação (digite o número): ')
#     if opcao == '3':
#         break
#     if opcao == '1':
#         codigo = input('Qual o código do produto: ')
#         qtd = int(input('Qual a quantidade: '))
#         produtos[codigo][1] += qtd
#     if opcao == '2':
#         codigo = input('Qual o código do produto: ')
#         qtd = int(input('Qual a quantidade: '))
#         if qtd > produtos[codigo][1]:
#             print('Quantidade insuficiente no estoque.')
#         else:
#             produtos[codigo][1] -= qtd
#
#
# print(produtos)

# Funções

# def soma(valor1, valor2):
#     return valor1 + valor2
#
# total = soma(36, 47)
# print(total)
#
# total1 = soma(36)
# print(total)

# def soma(valor1, valor2, imprime=False):
#     resultado = valor1 + valor2
#     if imprime:
#         print(f'Soma: {resultado}')
#     return resultado
#
# total = soma(10,84)
# print(total)
# total1 = soma(10, 84, True)

# def soma(valor1, valor2):
#     return valor1 + valor2
#
# def multiplicacao(valor1, valor2):
#     return valor1 * valor2
#
# def calcular(x, valor1, valor2):
#     return x(valor1, valor2)
#
# print(calcular(multiplicacao, 3, 2))


# lista = [49, 42, True]
# def soma(valor1, valor2, imprime=False):
#     resultado = valor1 + valor2
#     if imprime:
#         print(f'Soma: {resultado}')
#     return valor1 + valor2
#
# soma(*lista)

def soma(imprime, *valores):
    total = 0
    for valor in valores:
        total += valor
    if imprime:
        print(f'Soma: {total}')
    return total

soma(True, 10, 20, 30, 78)
print(soma(False, 10, 50))