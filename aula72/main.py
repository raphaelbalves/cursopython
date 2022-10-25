from pessoa import Pessoa

p1 = Pessoa('rphl', 38, False, False)
p2 = Pessoa('iana', 36, False, False)

p1.comer()
p1.falar('sapato')
p1.parar_comer()
p1.parar_comer()
p1.falar('cachoeira')
p1.falar('comida mineira')
p1.calar()
p1.calar()
print(p1.ano_atual)
print(Pessoa.ano_atual)
print(p1.get_ano_de_nascimento())