def divide_tesouro(tesouro, numero_piratas):
    valor_por_pirata = sum([quantidade * moeda for moeda, quantidade in tesouro.items()])

    return valor_por_pirata
