# Versão 1

string = '012345678901234567890123456789012345678901234567890123456789'
lista = [x + '9' for x in string.split('9') if x != string.split('9')[-1]]
print('.'.join(lista))

# Versão 2

def decompor_string(string):
    lista = [x + '9' for x in string.split('9') if x != string.split('9')[-1]]
    return '.'.join(lista)

print(decompor_string(string))

# Versão 3

def decompor_string2(string):
    teste = [string[string.index(x): string.index(x) + 10] for x in string if x == '0']
    return '.'.join(teste)

print(decompor_string2(string))



