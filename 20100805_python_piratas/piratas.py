def divide_tesouro(tesouro, numero_piratas):
    valor_por_pirata = 0
    moeda = tesouro.keys()[0]
    for moeda, quantidade in tesouro.items():
        valor_por_pirata += quantidade * moeda
    return valor_por_pirata
