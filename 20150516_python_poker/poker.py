from collections import Counter

ORDEM = [
        '2', '3', '4', '5', '6', '7', '8', 
        '9', '10', 'J', 'Q', 'K', 'A',]

def poker(mao):
    numeros = [carta[:-1] for carta in mao]
    naipes = {carta[-1] for carta in mao}
    isSequencia = False

    numeros.sort(key=lambda x: ORDEM.index(x))

    if numeros == ['10', 'J', 'Q', 'K', 'A'] and len(naipes)==1:
        return 'royal'

    for i in range(len(ORDEM) - 5):
        if numeros == ORDEM[i:i + 5]:
            isSequencia = True

    if numeros == ['2', '3', '4', '5', 'A']:
        isSequencia = True

    if isSequencia == True:
        return 'straight flush' if len(naipes) == 1 else 'sequencia' 
            
    if len(naipes) == 1:
        return 'flush'

    c = Counter(numeros)

    if 4 in c.values():
        return 'quadra'  

    if 2 in c.values() and 3 in c.values():
        return 'full hand'

    if 3 in c.values():
        return 'trinca'  

    if c.values().count(2) == 2:
        return 'dois pares'

    if 2 in c.values():
        return 'um par'    

    return 'maior carta'

