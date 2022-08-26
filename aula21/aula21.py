frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
nova_frase = ''
cont = 0
while cont < tamanho_frase:
    if frase[cont] == 'r':
        nova_frase += 'R'
    else:
        nova_frase += frase[cont]
    cont += 1

print(nova_frase)