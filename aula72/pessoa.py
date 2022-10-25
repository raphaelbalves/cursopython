from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'Ele já está falando.')
            return
        print(f'Quero falar sobre: {assunto}')
        self.falando = True

    def calar(self):
        if not self.falando:
            print(f'{self.nome} já está calado.')
            return
        print(f'{self.nome} calou-se')
        self.falando = False

    def comer(self):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        print(f'{self.nome} está comendo.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_de_nascimento(self):
        return self.ano_atual - self.idade

