# def divide(n1, n2):
#     try:
#         return n1/n2
#     except ZeroDivisionError as error:
#         print(error)
#         raise
#
# try:
#     print(divide(1, 0))
# except:
#     print('opa eu aqui')

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.")
    return n1/n2

try:
    print(divide(2, 0))
except ValueError as error:
    print('Você está tentando dividir por 0.')
    print(f'Log: {error}')



