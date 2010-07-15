class Matriz(object):

    def __init__(self, nova_matriz):
        self.matriz = nova_matriz

    def elemento(self, i, j):
        return self.matriz[i][j]

    @property
    def num_colunas(self):
        return len(self.matriz[0])

    def ultima_linha(self):
        return self.matriz[-1]

    def e_matriz_espiral(self):
        if self.num_colunas == 2:
            return self.elemento(0, 1) == self.elemento(0, 0) + 1
        return True

def lista_ordenada(lista):
    return lista == sorted(lista)
