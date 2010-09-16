class NumeroRomano(object):

    def __init__(self, valor):
        self.valor = valor

    def to_int(self):
        tamanho = len(self.valor)
        if self.valor[-1] == 'V':
            tamanho = 6 - tamanho
        return tamanho
