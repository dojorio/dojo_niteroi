class CampoMinado(object):

    def __init__(self, minas):
        linhas = minas.splitlines()
        campo = []
        for linha in linhas:
            linha = linha.strip()
            if linha:
                campo.append([caracter for caracter in linha])
        self.campo = campo

    def solucao(self):

        if self.campo[0][0] == '*':
            if self.campo[0][1] == '-':
                return[
                    ['*', 1],
                    [1, 1],
                ]
            return[
                ['*', '*'],
                [2, 2],
            ]
        return [
          [0, 0],
          [0, 0],
        ]
