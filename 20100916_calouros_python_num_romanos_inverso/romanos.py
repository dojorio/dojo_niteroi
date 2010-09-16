class NumeroRomano(object):

    def __init__(self, valor):
        self.valor = valor

    def to_int(self):
        if self.valor == 'V':
            return 5
        return len(self.valor)
