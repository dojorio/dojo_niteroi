def divide_tesouro(tesouro, numero_piratas):
    moedas_do_pirata = [quantidade * moeda for moeda, quantidade in tesouro.items()]
    valor_por_pirata = sum(moedas_do_pirata)

    return valor_por_pirata
