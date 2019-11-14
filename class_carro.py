class Carro():
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel_disp = 0

    def andar(self, km):
        gasto = km / self.consumo
        self.combustivel_disp -= gasto

    def obterGasolina(self):
        print(self.combustivel_disp)

    def adicionarGasolina(self, gasolina):
        self.combustivel_disp += gasolina

geforce = Carro(10)
geforce.adicionarGasolina(100)
geforce.obterGasolina()
geforce.andar(10)
geforce.obterGasolina()
