class NumeroRomano(object):

    def __init__(self, valor):
        self.valor = valor

    def to_int(self):
        if self.valor[-1] == 'V':
            return 6 - len(self.valor)
        return len(self.valor)
