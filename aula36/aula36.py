def funcao1(saudacao='Olá, ', nome='usuário'):
    print(saudacao, nome)

funcao1('Seja bem-vindo, ', 'minha flor')
funcao1()

def funcao2(a=0, b=0, c=0):
    print(a+b+c)

funcao2(1, 2, 3)
funcao2()

def funcao3(valor, percentual):
    return valor + (valor*percentual/100)

teste = funcao3(50, 10)
print(teste)

def funcao4(valor):
    if valor % 2 == 0:
        return 'fizz'
    elif valor % 5 == 0 and valor % 3 == 0:
        return 'FizzBuzz'
    elif valor % 5 == 0:
        return 'buzz'
    else:
        return valor

print(funcao4(2))
print(funcao4(5))
print(funcao4(15))
print(funcao4(11))
