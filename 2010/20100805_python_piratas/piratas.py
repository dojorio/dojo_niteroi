def divide_tesouro(tesouro, numero_piratas):
    if sum(tesouro.values()) < numero_piratas:
        return False

    valor_das_moedas = [
        quantidade * moeda for moeda, quantidade in tesouro.items()
    ]
    total_das_moedas = sum(valor_das_moedas)

    if total_das_moedas % numero_piratas:
        return False

    valor_dividido = sum(valor_das_moedas) / numero_piratas
    if max(tesouro.keys()) > valor_dividido:
        return False

    lista_de_moedas = []
    for k,v in tesouro.items():
        lista_de_moedas.extend([k] * v)


    #moedas_possiveis = sorted(tesouro.keys(), reverse=True)

    for pirata in range(numero_piratas):
        valor_desse_pirata = 0
        while valor_desse_pirata < valor_dividido:
            i = 0
            while valor_desse_pirata + lista_de_moedas[i] < valor_dividido:
                valor_desse_pirata += lista_de_moedas[i].pop(i)
                i+=1

    return valor_dividido
