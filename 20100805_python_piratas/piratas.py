def divide_tesouro(tesouro, numero_piratas):
    moedas_do_pirata = [quantidade * moeda / numero_piratas for moeda, quantidade in tesouro.items()]

    return sum(moedas_do_pirata)
