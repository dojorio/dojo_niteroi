def jokenpo(jogada_1, jogada_2):
    if jogada_1 == jogada_2:
        return 'empate'
    if 'tesoura' in [jogada_1, jogada_2]:
        return 'tesoura'
    if 'papel' in [jogada_1, jogada_2]:
        return 'papel'
