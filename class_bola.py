from termcolor import colored

class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mostraCorAtual(self):
        return print(colored('Cor atual: {}'.format(self.cor), 'blue'))

    def trocaCor(self):
        self.cor = str(input('Nova cor: '))
        print(colored('Nova cor: {}'.format(self.cor), 'grey'))

bola = Bola('azul', 5, 'couro')

bola.mostraCorAtual()
bola.trocaCor()



