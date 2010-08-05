def divide_tesouro(tesouro, numero_piratas):
    valor_por_pirata = sum([quantidade * moeda for moeda, quantidade in tesouro.items()])

    for moeda, quantidade in tesouro.items():
        valor_por_pirata += quantidade * moeda

    return valor_por_pirata
