'''
Formatando valores com modificadores
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(número)f - Quantidade de casas decimais (float)
:(caractere) (> ou < ou ^) (quantidade) (tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
'''

numero = 3.333333344594493023
print(f'{numero:.2f}')

numero2 = 1150
print(f'{numero2:0>5}')

numero3 = 4303
print(f'{numero3:0>10.2f}')

nome = 'rba'
print(f'{nome:#^50}')
