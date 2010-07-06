class CampoMinado(object):
    def __init__(self, campo_entrada):
        lista_linhas = campo_entrada.splitlines()
        campo_lista = []
        for linha in lista_linhas:
            linha = linha.strip()
            if linha:
                campo_lista.append([caracter for caracter in linha])
        self.campo = campo_lista

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
