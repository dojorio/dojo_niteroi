class NumeroRomano(object):

    def __init__(self, valor):
        self.valor = valor

    def to_int(self):
        return len(self.valor)
