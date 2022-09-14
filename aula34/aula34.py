# def funcao(msg='Olá,', nome='usuário'):
#     print(msg, nome)
#
# funcao()
# funcao('carlinhos')
# funcao(nome='carlinhos')

# mult = 1
# espaco = 9
# for x in range(13):
#     if x <= 9:
#         print((' ' * espaco) + '*' * mult)
#         mult += 2
#         espaco -= 1
#     else:
#         print(' ' * 8 + '***')

# salario_atual = float(input('Digite o salário atual: R$'))
# percentual_aumento = float(input('Quantos por cento de aumento sem o sinal de %: '))
# aumento = salario_atual * percentual_aumento / 100
# novo_salario = salario_atual + aumento
# print(f'Seu novo salário: R${novo_salario:,.2f}')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
resultado1 = float(input(f'{num1} + {num2} = '))
if resultado1 == float(num1 + num2):
    print(f'Você acertou, o resultado é: {resultado1}')
else:
    print(f'Você errou, o resultado é: {num1 + num2}')

resultado2 = float(input(f'{num1} - {num2} = '))
if resultado2 == float(num1 - num2):
    print(f'Você acertou, o resultado é: {resultado2}')
else:
    print(f'Você errou, o resultado é: {num1 - num2}')

resultado3 = float(input(f'{num1} * {num2} = '))
if resultado3 == float(num1 * num2):
    print(f'Você acertou, o resultado é: {resultado3}')
else:
    print(f'Você errou, o resultado é: {num1 * num2}')

resultado4 = float(input(f'{num1} / {num2} = '))
if resultado4 == float(num1 / num2):
    print(f'Você acertou, o resultado é: {resultado4}')
else:
    print(f'Você errou, o resultado é: {num1 / num2}')



