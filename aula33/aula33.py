from random import randint

print('### GERADOR DE CPF VÁLIDO ###')

while True:
    cpf = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}.{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}.{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}-{randint(0, 9)}{randint(0, 9)}'
    separar = cpf.split('.')
    juntar = ''.join(separar)

    # Número do CPF digitado pelo usuário sem . e -
    numero_cpf = int(juntar[:9] + juntar[10:])

    # Os nove primeiros números do CPF
    nove_primeiros_numeros = juntar[:9]

    # Aqui estão as variáveis que vão ser usadas para fazer as somas e multiplicações dos nove primeiros digitos do CPF.
    primeira_soma = 0
    primeira_multi = 10

    for x in nove_primeiros_numeros:
        primeira_soma += (int(x) * primeira_multi)
        primeira_multi -= 1

    # Cálculo para saber se o primeiro dígito após o hífen é 0 ou não
    primeiro_calculo = 11 - (primeira_soma % 11)
    digito1 = 0

    if primeiro_calculo > 9:
        digito1 = 0
    else:
        digito1 = primeiro_calculo

    # Os 10 primeiros números do CPF
    dez_primeiros_numeros = nove_primeiros_numeros + str(digito1)

    # Aqui estão as variáveis que vão ser usadas para fazer as somas e multiplicações dos 10 primeiros digitos do CPF.
    segunda_soma = 0
    segunda_multi = 11

    for x in dez_primeiros_numeros:
        segunda_soma += (int(x) * segunda_multi)
        segunda_multi -= 1

    # Cálculo para saber se o segundo dígito após o hífen é 0 ou não
    segundo_calculo = 11 - (segunda_soma % 11)
    digito2 = 0

    if segundo_calculo > 9:
        digito2 = 0
    else:
        digito2 = segundo_calculo

    # Número do CPF que deve ser igual ao número digitado pelo usuário.
    novo_cpf = int(dez_primeiros_numeros + str(digito2))

    # Veredito do validador.
    if numero_cpf == novo_cpf:
        print(f'CPF: {cpf} válido.')
        break
