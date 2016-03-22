class Matriz(object):

    def __init__(self, nova_matriz):
        self.matriz = nova_matriz

    def elemento(self, i, j):
        return self.matriz[i][j]

    @property
    def num_colunas(self):
        return len(self.matriz[0])

    @property
    def num_linhas(self):
        return len(self.matriz)

    def ultima_linha(self):
        return self.linha(-1)

    def linha(self, i):
        return self.matriz[i]

    def e_matriz_espiral(self):
        eh_espiral = lista_ordenada_sequencialmente(self.linha(0))
        if self.num_linhas != 1:
            eh_espiral = eh_espiral and lista_ordenada_sequencialmente(self.ultima_linha(), reverso=True)

        return eh_espiral

def lista_ordenada_sequencialmente(lista, reverso = False):
    if not reverso:
        return lista == range(lista[0], 1 + len(lista))
    return lista == range(lista[0], lista[-1] -1, -1)
