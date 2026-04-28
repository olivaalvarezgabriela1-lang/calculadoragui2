class Calculadora(object):
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.resultado = 0

    def calcularSuma(self):
        self.resultado = self.numero1 + self.numero2
