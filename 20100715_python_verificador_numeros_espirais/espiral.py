class Matriz:
    matriz = [[]]
    def elemento(self, i, j):
        return self.matriz[i][j]

    def __init__(self, nova_matriz):
        self.matriz = nova_matriz

    def e_matriz_espiral(self):
        if len(self.matriz[0]) == 2:
            return self.matriz[0][1] == self.matriz[0][0] + 1
        return True
