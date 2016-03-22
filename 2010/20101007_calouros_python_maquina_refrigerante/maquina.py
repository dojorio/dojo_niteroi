REFRI_1 = 'refri 1'
REFRI_2 = 'refri 2'

class Maquina(object):

    def __init__(self):
        self.moedas = []
        self.precos = {
            REFRI_1: 0.65,
            REFRI_2: 1.00,
        }

    def insere_moedas(self, moedas):
        self.moedas = moedas

    def cancela(self):
        return self.moedas

    def __troco(self, preco):
        troco = self.moedas[:]
        troco.remove(preco)
        return troco

    def comprar_refri(self, refri):
        dinheiro = sum(self.moedas)
        preco = self.precos[refri]
        if dinheiro < preco:
            return self.moedas
        elif dinheiro == preco:
            return refri
        retorno = [refri]
        retorno.extend(self.__troco(preco))
        return retorno


    def comprar_refri_1(self):
        return self.comprar_refri(REFRI_1)

    def comprar_refri_2(self):
        return self.comprar_refri(REFRI_2)
