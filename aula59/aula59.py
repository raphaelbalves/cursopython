try:
    a = 1/0
except (NameError, IndexError) as error:
    print(f'Deu erro: {error}')
except Exception as error2:
    print(f'Deu um erros inesperado: {error2}')
else:
    print('Isso sempre vai ser mostrado quando não houver erro.')
finally:
    a = None

# print('Isso sempre vai ser mostrado, mesmo com erro.')



print('Resto do programa sem dar pau, porque os erros foram tratados.')
