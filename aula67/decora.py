# def fala_oi():
#     print('oi')
#
# variavel = fala_oi
#
# variavel()
# fala_oi()

# def primeira():
#     def segunda():
#         print('oi')
#     return segunda
#
# variavel = primeira()
# variavel()

# def primeira(funcao):
#     def segunda(*args, **kwargs):
#         print('Agora estou decorada.')
#         funcao(*args, **kwargs)
#     return segunda
#
# # @primeira
# # def fala_oi():
# #     print('Oi')
#
# @primeira
# def outra_funcao(msg):
#     print(msg)
#
# # variavel = primeira(fala_oi)
# # fala_oi()
# outra_funcao('oi, bb')

from time import time
from time import sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo}ms para executar.')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(5):
        sleep(1)

demora()