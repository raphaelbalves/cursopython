def numeros_com_digitos(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('-', '')
    return cnpj


def apenas_numeros_sem_digitos(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('-', '')
    return cnpj[:12]


def primeiro_digito(cnpj):
    cnpj = list(cnpj)
    multiplicador = 5
    for indice in range(4):
        cnpj[indice] = int(cnpj[indice]) * multiplicador
        multiplicador -= 1
    multiplicador = 9
    for indice in range(4, 12):
        cnpj[indice] = int(cnpj[indice]) * multiplicador
        multiplicador -= 1
    primeiro_digito = 11 - (sum(cnpj) % 11)
    if primeiro_digito > 9:
        return 0
    else:
        return primeiro_digito

def segundo_digito(cnpj, primeiro_digito):
    cnpj = list(cnpj) + [primeiro_digito]
    multiplicador = 6
    for indice in range(5):
        cnpj[indice] = int(cnpj[indice]) * multiplicador
        multiplicador -= 1
    multiplicador = 9
    for indice in range(5, 13):
        cnpj[indice] = int(cnpj[indice]) * multiplicador
        multiplicador -= 1
    segundo_digito = 11 - (sum(cnpj) % 11)
    if segundo_digito > 9:
        return 0
    else:
        return segundo_digito

def validar(cnpj):
    cnpj_com_digitos = numeros_com_digitos(cnpj)
    cnpj_sem_digitos = apenas_numeros_sem_digitos(cnpj)
    primeiro_digito_numero = primeiro_digito(cnpj_sem_digitos)
    segundo_digito_numero = segundo_digito(cnpj_sem_digitos, primeiro_digito_numero)
    cnpj_mais_digitos = cnpj_sem_digitos+str(primeiro_digito_numero)+str(segundo_digito_numero)
    if cnpj_com_digitos == cnpj_mais_digitos:
        return f'CNPJ válido: {cnpj}'
    else:
        return f'CNPJ inválido: {cnpj}'







