print(2 == '2')
print(2 == 2)

nome = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade: '))


if idade >= 20 and idade <= 30:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')