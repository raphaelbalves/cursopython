from funcoes_cnpj import validar

cnpj = input('Digite o CNPJ: ')
if validar(cnpj):
    print(f'CNPJ válido: {cnpj}')
else:
    print(f'CNPJ inválido: {cnpj}')

