carrinho = []

while True:
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input('Digite o preço do produto: '))
    carrinho.append((nome_produto, preco_produto))
    sair = input('Para finazilar, digite 0: ')
    if sair == '0':
        break

preco_total = sum([y for x, y in carrinho])
print(preco_total)

