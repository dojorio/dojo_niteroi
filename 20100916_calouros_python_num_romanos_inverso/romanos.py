class NumeroRomano(object):

    def __init__(self, valor):
        self.valor = valor

    def to_int(self):
        if self.valor == 'X':
            return 10
        tamanho = len(self.valor)
        if self.valor[-1] == 'V':
            tamanho = 6 - tamanho
        elif self.valor[0] == 'V':
            tamanho = 4 + tamanho

        return tamanho
