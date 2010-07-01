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

    def __gt__(self, carta):
        return self.valor > carta.valor

def somatorio(cartas):
    return sum([carta.valor for carta in cartas])

def rodada(jogadas, trunfo):
    lista_de_cartas = [carta[1] for carta in jogadas]

    pontos_vencedor = somatorio(lista_de_cartas)


    maior_carta = max(lista_de_cartas)
    indice_do_vencedor = lista_de_cartas.index(maior_carta)
    vencedor = jogadas[indice_do_vencedor][0]
   # for dupla in jogadas:
       # if dupla[1].valor == pontos_vencedor:
        #    vencedor = dupla[0]


    return (vencedor, pontos_vencedor)
