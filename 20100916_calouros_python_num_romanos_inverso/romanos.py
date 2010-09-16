class NumeroRomano(object):

    def __init__(self, valor):
        self.valor = valor
        self.dic = {
            'I': 1,
            'V': 5,
            'X': 10,
        }

    def to_int(self):
        resultado = 0
        for i, caractere in enumerate(self.valor):
            resultado += self.dic[caractere]
        return resultado


        tamanho = len(self.valor)
        ultimo = self.valor[-1]
        primeiro = self.valor[0]

        if ultimo == 'V' and primeiro == 'X':
            tamanho = 17 - tamanho
        elif ultimo == 'X' or ultimo == 'V':
            tamanho = self.dic[ultimo] - tamanho + 1
        elif primeiro == 'X' or primeiro == 'V':
            tamanho = self.dic[primeiro] + tamanho - 1

        return tamanho
