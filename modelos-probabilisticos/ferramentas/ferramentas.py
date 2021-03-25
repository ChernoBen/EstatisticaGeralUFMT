import math

#recebe um array p/ calcular desvio padrão
class Desvio:

    def __init__(self, arr):
        self.arr = arr
        self.ma = 0
        self.somatoria = 0
        self.dp = 0
        self.total = 0

    def Dp(self):

        #obter a somatoria
        for item in self.arr:
            self.somatoria += item

        #obter a media aritimética
        self.ma = self.somatoria / len(self.arr)

        #subtrair itens - media Arit elevado ao quadrado
        for item in self.arr:
            self.total += math.pow((item - self.ma), 2)

        #dividir resultado p/ quantidade de itens
        self.total = self.total / len(self.arr)
        #obter a raiz para obter desvio padrão
        self.dp = math.sqrt(self.total)


