class Servico:
    def __init__(self, km_rodado):
        self.km_rodado = km_rodado
        self.centavos = 0.80 #fixo

    def calc_custo(self):
        self.custo = self.km_rodado * self.centavos
        return self.custo