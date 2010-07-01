valores = {
    'A':11,
    '7':10,
    'K':4,
    'J':3,
    'Q':2,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
}

class Carta(object):

    def __init__(self, naipe, nome):
        self.naipe = naipe
        self.nome = nome
        self.valor = valores[self.nome]

def somatorio(cartas):
    return sum([carta.valor for carta in cartas])

def rodada(cartas, trunfo):
    return cartas[0][0], somatorio(cartas)
