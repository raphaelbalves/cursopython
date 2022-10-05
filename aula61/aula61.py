# try:
#     numero = float(input('Digite um número: '))
#     print(numero * 5)
# except:
#     print('Você precisa digitar números.')

def converte_numero(entrada):
    try:
        return int(entrada)
    except ValueError:
        try:
            return float(entrada)
        except ValueError:
            return None


numero = converte_numero(input('Digite um número: '))

if numero is not None:
    print(numero * 5)
else:
    print('Isso não é um número.')

