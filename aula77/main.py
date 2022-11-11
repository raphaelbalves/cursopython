from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor1 = Escritor('Raphael')
caneta1 = Caneta('bic')
maquina1 = MaquinaDeEscrever('Olivetti')

print(escritor1.nome)
print(caneta1.marca)
print(maquina1.marca)

escritor1.ferramenta = caneta1
escritor1.ferramenta.escrever()