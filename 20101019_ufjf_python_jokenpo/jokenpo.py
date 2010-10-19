def avalia_jogo(jogada_1, jogada_2):
    vetor = {
        "pedra":
            {"pedra":"empate","papel":"papel","tesoura":"pedra"},
        "papel":
            {"pedra":"papel","papel":"empate","tesoura": "tesoura"},
        "tesoura":
            {"pedra":"pedra", "papel":"tesoura", "tesoura":"empate"}
    }
    return vetor[jogada_1][jogada_2]
