frase = 'O Brasil é o país do futebol, o Brasil é penta.'
dividido = frase.lower().split()
lista = []

palavra = ''
contagem = 0

for x in dividido:
    maior = dividido.count(x)
    if maior > contagem:
        contagem = maior
        palavra = x

    if x not in lista:
        lista.append(x.)
        print(f'"{x}" aparece {dividido.count(x)}x na frase.')

print(f'A palavra que mais apareceu no texto foi "{palavra}": {contagem} vezes.')
