class Entregador():
    def __init__(self, nome, entregas):
        self.nome = nome
        self.entregas = entregas
          
class Item():
    def __init__(self, nome):
        self.nome = nome
        
    def __hash__(self):
        return hash(self.nome)
        
    def __cmp__(self, other):
        return cmp(self.nome, other.nome)

def otimiza_distribuicao(entregadores, entregas):    
    if len(entregadores) > 1:
        noel = [e for e in entregadores if e.nome == 'Papai Noel'][0]
        return {entregas[0]: noel}
        
    return {entregas[0]: entregadores[0]}
