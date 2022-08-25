numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)
    if numero % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
except:
    print('O número que você digitou não é inteiro.')

hora = input('Que horas são (apenas horas): ')
try:
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora <= 17:
        print('Boa tarde')
    elif hora <= 23:
        print('Boa noite')
    else:
        print('Hora inexistente')
except:
    print('Você não digitou um número inteiro.')


nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto, tem quatro letras ou menos.')
elif len(nome) <= 6:
    print('Seu nome é normal, tem entre cinco e seis letras.')
else:
    print('Seu nome é muito grande, tem mais do que seis letra.')
