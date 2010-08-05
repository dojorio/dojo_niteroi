def divide_tesouro(tesouro, numero_piratas):
    total_das_moedas = [quantidade * moeda for moeda, quantidade in tesouro.items()]

    return sum(total_das_moedas) / numero_piratas
