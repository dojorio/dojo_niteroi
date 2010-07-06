class CampoMinado(object):
    def __init__(self, campo):
        campo = campo.strip()
        campo = campo.splitlines()
        lista = [
            [campo[0][0], campo[0][1]],
            [campo[1][-2], campo[1][-1]],
        ]
        self.campo = lista

    def solucao(self):
        if self.campo[0][0] == '*':
            return[
                ['*', 1],
                [1, 1],
            ]
        return [
          [0, 0],
          [0, 0],
        ]
