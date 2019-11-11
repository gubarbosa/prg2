from termcolor import colored

class Retangulo():
    def __init__(self, ladoA, ladoB):
        self.ladoA = int(ladoA)
        self.ladoB = int(ladoB)

    def mostraLadoAtual(self):
        print(colored('Lado A atual: {}m \n'
                      'Lado B atual: {}m'.format(self.ladoA, self.ladoB), 'red'))

    def trocaLados(self):
        self.ladoA = int(input('Novo valor do lado A: '))
        self.ladoB = int(input('Novo valor do lado B: '))

    def retornaLados(self):
        print(colored('Novo valor lado A: {}m \n'
                      'Novo valor lado B: {}m'.format(self.ladoA, self.ladoB), 'yellow'))

    def calculaArea(self):
        area = self.ladoA * self.ladoB
        print(colored('A área do retângulo é de {}m²'.format(area), 'magenta'))

    def perimetro(self):
        perimetro = (self.ladoA * 2) + (self.ladoB * 2)
        print(colored('O perímetro do retângulo é de {}m'.format(perimetro), 'magenta'))


retangulo = Retangulo(5, 4)
retangulo.mostraLadoAtual()
retangulo.trocaLados()
retangulo.retornaLados()
retangulo.calculaArea()
retangulo.perimetro()
