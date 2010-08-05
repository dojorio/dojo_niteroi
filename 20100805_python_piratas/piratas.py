def divide_tesouro(tesouro, numero_piratas):
    moedas_do_pirata = [quantidade * moeda for moeda, quantidade in tesouro.items()]
    return sum(moedas_do_pirata)
