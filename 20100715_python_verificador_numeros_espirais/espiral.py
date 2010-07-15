class Matriz:
    matriz = [[]]
    def elemento(self, i, j):
        return matriz[i][j]

    def define_matriz(nova_matriz):
        matriz = nova_matriz

    def e_matriz_espiral(self):
        if len(matriz[0]) == 2:
            return matriz[0][1] == matriz[0][0] + 1
        return True
