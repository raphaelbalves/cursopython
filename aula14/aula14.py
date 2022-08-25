num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(f'A soma dos dois números: {num1 + num2}')
except:
    print('Você digitou algo que não é um numeral.')

