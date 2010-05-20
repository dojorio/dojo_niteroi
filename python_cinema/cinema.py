#coding: utf-8
def bilheteria(ingressos, especiais = []):

    preco = {'Normal':11.0, 'Estudante':8.0, 'Idoso':6.0, 'Criança':5.50, 'Grupo' : 6.0}
    tabela_especial = {'3D':3.0, '2h':1.50, 'quinta':-2.0, 'fds':1.50, 'cabine':2.00}

    resultado = 0


    lista_quantidade = ingressos.values()
    quantidade = sum(lista_quantidade)
    if quantidade >= 20:
        return quantidade * preco['Grupo']

    if not especiais:    
        for tipo, quantidade in ingressos.items():
            resultado += preco[tipo] * quantidade 
    else:
        for tipo, quantidade in ingressos.items():
            for especial in especiais:
                resultado += preco[tipo] * quantidade + tabela_especial[especial]
    return resultado
