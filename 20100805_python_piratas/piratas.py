def divide_tesouro(tesouro, numero_piratas):
    valor_das_moedas = [quantidade * moeda for moeda, quantidade in tesouro.items()]
    total_das_moedas = sum(valor_das_moedas)
    if total_das_moedas % numero_piratas == 0:
        return sum(valor_das_moedas) / numero_piratas
    return False
