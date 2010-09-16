class NumeroRomano(object):

    def __init__(self, valor):
        self.valor = valor
        self.dic = {
            'I': 1,
            'V': 5,
            'X': 10,
        }

    def to_int(self):
        resultado = 0
        pilha = list(self.valor)
        ultimo = ''
        while pilha:
            atual = pilha.pop()
            if atual == 'I' and ultimo in ['X', 'V']:
                resultado -= self.dic[atual]
            else:
                resultado += self.dic[atual]
            #resultado += self.dic[pilha.pop()]
        return resultado







        for i, caractere in enumerate(self.valor):
            if i<len(self.valor)-1 and self.dic[self.valor[i+1]] > self.dic[caractere]:
                resultado -= self.dic[caractere]
            else:
                resultado += self.dic[caractere]
        return resultado
