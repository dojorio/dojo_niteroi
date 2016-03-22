class Carta():
    

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        self.valores = ['A'] + [str(x) for x in range(2,11)] + ['J', 'Q', 'K', 'A'] 
           
    def __eq__ (self,outra):
        return self.valor == outra.valor
     
    def __gt__(self, outra):
        return self.valores[self.valores.index(self.valor)] > self.valores[self.valores.index(outra.valor)]
    
    def proximo(self):
       return self.valores[self.valores.index(self.valor)+1]


def has_pair(cartas):
    for carta in cartas:
        if cartas.count(carta) == 2:
            return True
    return False    

def has_three(cartas):
    for carta in cartas:
        if cartas.count(carta) == 3:
            return True
    return False    

def has_four(cartas):
    for carta in cartas:
        if cartas.count(carta) == 4:
            return True
    return False    

def has_flush(cartas):
    for carta in cartas: 
        if carta.naipe != cartas[0].naipe:
            return False
    return True

def has_straight(cartas):
    cartas = sorted(cartas)
    for indice in range(len(cartas)-1):
        if cartas[indice].proximo() != cartas[indice+1].valor:
            return False
    return True
    
def poker(cartas):
    
    if has_pair(cartas) and has_three(cartas):
        return "Full House"
    if has_pair(cartas):
        return "Pair"
    if has_three(cartas):
        return "Three of a Kind"
    if has_four(cartas):
        return "Four of a Kind"
    if has_flush(cartas):
        return "Flush"
    if has_straight(cartas):
        return "Straight"

    return "High Card"

    
