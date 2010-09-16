class NumeroRomano(object):

    def __init__(self, valor):
        self.valor = valor

    def to_int(self):
        valor = len(self.valor)
        if self.valor[-1] == 'V':
            valor = 6 - valor
        return valor
