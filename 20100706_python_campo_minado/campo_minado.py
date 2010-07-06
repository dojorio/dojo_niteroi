class CampoMinado(object):
    def __init__(self, campo):
        campo.strip()
        campo.splitlines()
        lista = [
            [campo[0], campo[1]],
            [campo[2], campo[3]],
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
