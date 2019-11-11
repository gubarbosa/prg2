from termcolor import colored
class Quadrado():
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudarLado(self):
        self.tamanho_lado = int(input('Novo valor de lado: '))

    def retornarLadoPrimario(self):
        return print(colored('Lado primário: {}m'.format(self.tamanho_lado), 'red'))

    def retornarNovoLado(self):
        return print(colored('Novo lado: {}m'.format(self.tamanho_lado), 'yellow'))

    def calcularArea(self):
        area = self.tamanho_lado ** 2
        return area

    def mostrarArea(self):
        return print(colored('Área igual a: {} m²'.format(self.calcularArea()), 'blue'))

quadrado = Quadrado(5)

quadrado.retornarLadoPrimario()
quadrado.mudarLado()
quadrado.retornarNovoLado()
quadrado.calcularArea()
quadrado.mostrarArea()
