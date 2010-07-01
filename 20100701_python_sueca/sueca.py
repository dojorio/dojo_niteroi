class Carta(object):
    def __init__(self, naipe, nome):
        self.naipe = naipe
        self.nome = nome
        self.valor = 0
        calcula_valor()

    def calcula_valor():
        valores = { '2':0,
                    '3':0,
                    '4':0,
                    '5':0}
        self.valor = valores[self.nome]


def somatorio(cartas):
    return 0

def pontuacao():
    return ''
