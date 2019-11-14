class Macaco():
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
    
    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        print(self.bucho)

    def digerir(self):
        self.bucho = []

macaco1 = Macaco('KAKO')
macaco2 = Macaco('Elian')

print('Macaco 1: ')
macaco1.comer('uva')
macaco1.comer('abacaxi')
macaco1.comer('laranja')
macaco1.verBucho()
macaco1.digerir()
macaco1.verBucho()

print('Macaco 2: ')
macaco2.comer('banana')
macaco2.comer('árvore')
macaco2.comer('batata')
macaco2.verBucho()
macaco2.digerir()
macaco2.verBucho()

print('Macaco 1 come macaco 2')
macaco1.comer('Elian')
macaco1.verBucho()
macaco1.digerir()
macaco1.verBucho()
