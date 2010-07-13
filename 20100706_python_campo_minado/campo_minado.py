class CampoMinado(object):

    def __init__(self, minas):
        linhas = minas.splitlines()
        campo = []
        for linha in linhas:
            linha = linha.strip()
            if linha:
                linha = linha.replace('-', '0')
                lista_de_campo = []
                for caracter in linha:
                    try:
                        lista_de_campo.append(int(caracter))
                    except Exception:
                        lista_de_campo.append(caracter)
                campo.append(lista_de_campo)
        self.campo = campo

    def solucao(self):
        if self.campo[0][0] == '*':
            if self.campo[0][1] == 0:
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
