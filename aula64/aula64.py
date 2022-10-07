import vendas.calc_precos
from vendas import calc_precos
from vendas.calc_precos import aumento, reducao
from vendas.formato.preco import real
valor = 10
porcentagem = 5



print(real(vendas.calc_precos.aumento(valor, porcentagem)))
