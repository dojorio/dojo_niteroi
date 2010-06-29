class Pais (object):
    nome = ""
    ouro = 0
    prata = 0
    bronze = 0

    def __init__(self, nome, ouro, prata, bronze):
        self.nome = nome
        self.ouro = ouro
        self.prata = prata
        self.bronze = bronze

    def __lt__(self, pais):
        return self.ouro < pais.ouro

def calcula_ranking(paises):
    ordenada = sorted(paises, reverse = True)
    return [pais.nome for pais in ordenada]
