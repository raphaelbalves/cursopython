contador = 1
acumulador =1

while contador <= 10:
    print(contador, acumulador)
    contador += 1
    acumulador += contador
    # if contador > 5:
    #     break
else:
    print('Entra o else como uma expressão falsa.')
print('Essa entrada sempre vai existir, caso while seja'
      'falso ou não.')