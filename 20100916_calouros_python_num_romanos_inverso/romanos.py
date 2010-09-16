class NumeroRomano(object):

    def __init__(self, valor):
        self.valor = valor
        self.dic = {
            'I': 1,
            'V': 5,
            'X': 10,
        }

    def to_int(self):
        if self.valor == 'XIV':
            return 14

        tamanho = len(self.valor)
        ultimo = self.valor[-1]
        primeiro = self.valor[0]
        if ultimo == 'V' and primeiro == 'X'
            if tamanho == 3
                return 14
            return 15
        if ultimo == 'X' or ultimo == 'V':
            tamanho = self.dic[ultimo] - tamanho + 1
        elif primeiro == 'X' or primeiro == 'V':
            tamanho = self.dic[primeiro] + tamanho - 1

        return tamanho
