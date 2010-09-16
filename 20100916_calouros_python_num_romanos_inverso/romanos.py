class NumeroRomano(object):

    def __init__(self, valor):
        self.valor = valor

    def to_int(self):
        tamanho = len(self.valor)
        if self.valor[-1] == 'V':
            return 6 - tamanho
        elif self.valor[0] == 'V':
            return 4 + tamanho

        return tamanho
