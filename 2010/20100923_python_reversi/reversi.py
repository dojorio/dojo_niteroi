class Reversi(object):


    def __init__(self):
        self.tabuleiro = [
            [' ', ' ', ' ', ' '],
            [' ', 'P', 'B', ' '],
            [' ', 'B', 'P', ' '],
            [' ', ' ', ' ', ' '],
        ]

    def jogada(self, jogador, posicao):
        linha  = posicao[0]
        coluna = posicao[1]
        self.tabuleiro[linha][coluna] = jogador
        if coluna == 0:
            self.tabuleiro[linha][coluna + 1] = jogador
        elif coluna == 3:
            self.tabuleiro[linha][coluna - 1] = jogador

        if linha == 0:
            self.tabuleiro[linha + 1][coluna] = jogador
        elif linha == 3:
            self.tabuleiro[linha - 1][coluna] = jogador
