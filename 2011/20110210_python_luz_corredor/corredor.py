import itertools

class Lampada(object):

    def __init__(self, ligada=False):
        self.ligada = ligada

    @property
    def estado(self):
        return 'on' if self.ligada else 'off'

    def aberta_botao(self):
        self.ligada = not self.ligada

def anda_corredor(numero_de_lampadas):
    lista_de_numero_de_lampadas = range(numero_de_lampadas)

    lampadas = []
    for i in lista_de_numero_de_lampadas:
        lampadas.append(Lampada())

    caminhada_lampada = itertools.product(
        lista_de_numero_de_lampadas, lista_de_numero_de_lampadas
    )

    for caminhada, lampada in caminhada_lampada:
        if not ((lampada + 1) % (caminhada + 1)):
            lampadas[lampada].aberta_botao()

    return [l.estado for l in lampadas]
