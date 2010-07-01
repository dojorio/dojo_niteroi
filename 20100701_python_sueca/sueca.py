valores = { '2':0,
            '3':0,
            '4':0,
            '5':0,
            'A':11}

class Carta(object):

    def __init__(self, naipe, nome):
        self.naipe = naipe
        self.nome = nome
        self.valor = valores[self.nome]


def somatorio(cartas):
    return sum([carta.valor for carta in cartas])

def pontuacao():
    return ''
